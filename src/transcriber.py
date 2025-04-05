"""Core functionality for transcribing audio files using OpenAI's Whisper API."""

import os
import openai
from dotenv import load_dotenv
import tempfile
import subprocess
import glob

def setup_openai():
    """Configure OpenAI client with API key from environment."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    return openai.OpenAI(api_key=api_key)

def transcribe_audio(file_path, model="whisper-1"):
    """
    Transcribe an audio file using OpenAI's Whisper API.
    If the file is larger than the API limit, splits it into 30-second segments,
    transcribes each, and appends the results.
    
    Args:
        file_path: Path to the audio file
        model: Whisper model to use (default: whisper-1)
        
    Returns:
        The transcription text
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
    
    # API content size limit (approximate): 26214400 bytes
    MAX_SIZE = 26214400
    file_size = os.path.getsize(file_path)
    
    client = setup_openai()
    
    # If file size is within limits, use the simple transcription flow.
    if file_size <= MAX_SIZE:
        try:
            with open(file_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model=model,
                    file=audio_file
                )
            return transcription.text
        except Exception as e:
            raise Exception(f"Error during transcription: {e}")
    
    # Otherwise, split the audio into 30-second segments, transcribe each, and append.
    transcription_combined = ""
    try:
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Split audio into 30-second segments using ffmpeg.
            segment_pattern = os.path.join(tmp_dir, "segment_%03d.mp3")
            split_command = [
                "ffmpeg", "-i", file_path,
                "-f", "segment", "-segment_time", "30",
                "-c", "copy", segment_pattern
            ]
            subprocess.run(split_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Process segments in sorted order.
            segments = sorted(glob.glob(os.path.join(tmp_dir, "segment_*.mp3")))
            if not segments:
                raise Exception("No segments were created during splitting.")
            
            for segment in segments:
                with open(segment, "rb") as audio_segment:
                    seg_transcription = client.audio.transcriptions.create(
                        model=model,
                        file=audio_segment
                    )
                transcription_combined += seg_transcription.text + "\n"
        return transcription_combined.strip()
    except Exception as e:
        raise Exception(f"Error during transcription: {e}")

"""Command line interface for the MP3 transcriber."""

import argparse
import os
import sys
import datetime
from pathlib import Path
from .transcriber import transcribe_audio, transcribe_audio_local

def main():
    """
    Main entry point for the MP3 transcriber.
    """
    parser = argparse.ArgumentParser(description="Transcribe MP3 files using OpenAI's Whisper")
    parser.add_argument("input_file", help="Path to the audio file to transcribe")
    parser.add_argument("--output-dir", default="output", help="Output directory for transcription files")
    parser.add_argument("--name", default="transcript", help="Name prefix for the transcription file")
    parser.add_argument("--model", default="whisper-1", help="Model to use (for local mode, try 'tiny', 'base', etc.)")
    parser.add_argument("--mode", choices=["local", "api"], default="local", help="Transcription mode: local uses the open-source Whisper model (default), api uses OpenAI's API")
    
    args = parser.parse_args()
    
    try:
        # Ensure output directory exists
        os.makedirs(args.output_dir, exist_ok=True)
        
        # Generate timestamp
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Set output file path
        output_filename = f"transcript-{args.name}-{current_date}.txt"
        output_path = os.path.join(args.output_dir, output_filename)
        
        print(f"Transcribing audio file: {args.input_file}")
        if args.mode == "local":
            transcription = transcribe_audio_local(args.input_file, model=args.model)
        else:
            transcription = transcribe_audio(args.input_file, model=args.model)
        
        # Save transcription to file
        with open(output_path, "w") as f:
            f.write(transcription)
            
        print(f"Transcription saved to {output_path}")
        print("\nPreview:")
        print("------------------------------")
        # Show preview (first 200 chars)
        preview = transcription[:200] + "..." if len(transcription) > 200 else transcription
        print(preview)
        print("------------------------------")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

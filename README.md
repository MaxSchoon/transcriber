# MP3 Transcriber

A minimal command-line tool for transcribing MP3 files to text using OpenAI's Whisper API.

## Prerequisites

1. Python 3.7 or higher
2. FFmpeg installed on your system
   - For macOS: `brew install ffmpeg`
   - For Ubuntu/Debian: `sudo apt-get install ffmpeg`
   - For Windows: Download from [FFmpeg website](https://www.ffmpeg.org/download.html)

## Setup

1. Clone this repository
2. Run the setup script to install dependencies and FFmpeg:
   ```
   bash install_dependencies.sh
   ```
   
   Or install dependencies manually:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```
   cp .env.example .env
   # Edit .env with your API key
   ```
4. Create an output folder for transcriptions:
   ```
   mkdir -p output
   ```
5. (Optional) Install as a CLI tool:
   ```
   pip install -e .
   ```

## Usage

Basic usage:
```bash
python3 -m src.main /path/to/your/audio.mp3
```

With custom name and output folder:
```bash
python3 -m src.main /path/to/your/audio.mp3 --name interview --output-dir ./my-transcripts
```

Use a different Whisper model:
```bash
python3 -m src.main /path/to/your/audio.mp3 --model whisper-1
```

If installed as a CLI tool:
```bash
transcribe /path/to/your/audio.mp3
```

## Notes

- Supports common audio formats compatible with the Whisper API
- For large audio files, the transcription might take longer
- The free tier of OpenAI API has file size limitations
- Transcripts are saved as transcript-[name]-[date].txt by default

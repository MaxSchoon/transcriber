#!/bin/bash

echo "Installing Python dependencies..."
pip install -r requirements.txt

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "Detecting macOS. Installing FFmpeg using Homebrew..."
    if ! command -v brew &>/dev/null; then
        echo "Homebrew not found. Please install Homebrew first: https://brew.sh/"
        exit 1
    fi
    brew install ffmpeg
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    echo "Detecting Linux. Installing FFmpeg using apt..."
    sudo apt-get update
    sudo apt-get install -y ffmpeg
else
    echo "Your OS is not directly supported by this script."
    echo "Please install FFmpeg manually: https://www.ffmpeg.org/download.html"
fi

echo "Setup complete! Make sure to create a .env file with your OpenAI API key."
echo "You can copy the example file: cp .env.example .env"

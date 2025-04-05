from setuptools import setup, find_packages

setup(
    name="mp3-transcriber",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "openai-whisper>=20231117",  # provides local transcription via Whisper
        "ffmpeg-python>=0.2.0",
    ],
    entry_points={
        "console_scripts": [
            "transcribe=src.main:main",
        ],
    },
    author="User",
    description="A minimal MP3 transcriber supporting local (open-source Whisper) and API modes",
    python_requires=">=3.7",
)

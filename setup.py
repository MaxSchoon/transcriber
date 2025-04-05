from setuptools import setup, find_packages

setup(
    name="mp3-transcriber",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "transcribe=src.main:main",
        ],
    },
    author="User",
    description="A minimal MP3 transcriber using OpenAI's Whisper API",
    python_requires=">=3.7",
)

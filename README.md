# TubeMixr

## Overview

TubeMixr is a command-line tool that allows users to create a custom mix of songs by extracting specific segments from YouTube videos. The software downloads audio from given YouTube URLs, extracts specified portions based on user-defined start and end times, and merges the selected segments into a single audio file. This is particularly useful for creating dance mixes, mashups, or curated playlists from YouTube sources.

## Problem Statement

Often, users want to create a seamless mix of their favorite tracks without having to manually download, edit, and merge audio clips. Traditional methods require multiple tools for downloading, trimming, and merging audio files, which can be time-consuming and complex. TubeMixr simplifies this process by automating the entire workflow in a single script, making it accessible for DJs, choreographers, and music enthusiasts.

## Features

- Download audio from YouTube videos.
- Extract specific portions of audio based on user-defined timestamps.
- Merge multiple extracted segments into a single audio file.
- Support for command-line input and CSV file input.
- Automated cleanup of temporary files.

## Installation

To use TubeMixr, ensure you have the following installed:

- Python 3.x
- Required dependencies (install using `pip install -r requirements.txt`)

## Usage

### 1. Run the script

```sh
python main.py
```

### 2. Choose an input method

Upon running, TubeMixr prompts the user to select an input method:

- **Command Line Input**: Manually enter YouTube URLs along with start and end timestamps.
- **CSV File Input**: Provide a CSV file (`csv/tubemixr.csv`) with YouTube URLs and corresponding timestamps.

### 3. Audio Processing

- TubeMixr downloads the audio files from the provided URLs.
- It then extracts the specified portions.
- The extracted segments are merged into a single audio file.

### 4. Output

The final merged audio file will be stored in the output directory.

## Folder Structure

```
TubeMixr/
│── features/
│   ├── audio_download.py
│   ├── audio_split.py
│   ├── audio_merge.py
│   ├── read_csv.py
│── temp/
│   ├── split/
│── output/
│── csv/
│   ├── tubemixr.csv
│── main.py
│── requirements.txt
```

## Dependencies

`ffmpeg` must be installed on the system and added to PATH.

Ensure the following Python libraries are installed:

- `pytubefix` (for downloading audio)
- `pydub` (for splitting and merging audio)
- `csv` (for reading CSV input)

## Future Enhancements

- Add GUI support for easier interaction.
- Support for additional audio formats.
- Cloud storage integration for processing and storing files online.

## License

TubeMixr is an open-source project. Feel free to modify and improve it!
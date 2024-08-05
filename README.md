# YouTube Playlist Downloader

A comprehensive YouTube playlist downloader built with Python, allowing users to select and download video and audio streams from YouTube playlists, and optionally merge them into a single file. The application provides a graphical user interface (GUI) for ease of use.

## Features

- **Video and Audio Selection**: Lists available video resolutions and audio bitrates for user selection.
- **Concurrent Downloads**: Downloads video and audio streams concurrently to optimize performance.
- **Merging**: Uses `ffmpeg` to merge video and audio files into a single output file.
- **Graphical User Interface**: Built with `tkinter` for an intuitive user experience.

## Requirements

- Python 3.6 or higher
- `pytube`
- `ffmpeg-python`
- `tkinter` (comes pre-installed with standard Python installations)
- `ffmpeg` (must be installed separately and added to your system's PATH)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/youtube-playlist-downloader.git
    cd youtube-playlist-downloader
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install `ffmpeg`**:
    - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html), extract, and add the `bin` folder to your system's PATH.
    - **Mac**: Use Homebrew:
        ```bash
        brew install ffmpeg
        ```
    - **Linux**: Use your package manager, for example:
        ```bash
        sudo apt-get install ffmpeg
        ```

## Usage

### Command-Line Interface (CLI)

1. **Run the CLI script**:
    ```bash
    python youtube_downloader.py
    ```

2. **Follow the prompts** to input the playlist URL, select download path, and choose video resolutions and audio bitrates.

### Graphical User Interface (GUI)

1. **Run the GUI script**:
    ```bash
    python gui_app.py
    ```

2. **Use the GUI** to input the playlist URL, select the download path, and start the download process with optional merging.

## How It Works

### `youtube_downloader.py`

- **VideoManager**: Manages video download operations, listing available resolutions, and downloading selected resolution.
- **AudioManager**: Manages audio download operations, listing available bitrates, and downloading selected bitrate.
- **Merger**: Uses `ffmpeg` to merge downloaded video and audio files.
- **PlaylistDownloader**: Orchestrates the download process for all videos in a playlist, allowing user selections and handling concurrent downloads.

### `gui_app.py`

- **App Class**: Handles the GUI using `tkinter`, providing fields for playlist URL, download path, and options for merging.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [pytube](https://github.com/pytube/pytube)
- [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
- [ffmpeg](https://ffmpeg.org/)

---

**Author**: Samarth Rawat

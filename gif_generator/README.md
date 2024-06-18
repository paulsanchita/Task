# GIF Generator

This project automatically generates GIFs from video content with captions.

## Project Structure
gif_generator/
│
├── input_videos/
│ └── your_video.mp4
│
├── generated_gifs/
│ └── (GIFs will be saved here)
│
├── scripts/
│ └── gif_generator.py
│
├── README.md
└── requirements.txt

## Setup

1. Clone the repository.
2. Navigate to the project directory: `cd gif_generator`
3. Install the dependencies: `pip install -r requirements.txt`
4. Place the video in the `input_videos` directory.
5. Run the script: `python scripts/gif_generator.py`

## Usage

- The script will generate GIFs from the input video and save them in the `generated_gifs` directory.
- Adjust the script as needed for different segmentation logic or caption styles.

## Dependencies


- `openai-whisper`
- `moviepy`


## Author
Sanchita Paul
Email: sanchita.paul0411@gmail.com

## The video provided for this project is my own video recording. So the quality maynot be up to mark. But my task here was to generated gifs from videos.
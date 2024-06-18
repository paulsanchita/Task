import os
import whisper
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def transcribe_video(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    return result

def create_gif_segment(video_path, start_time, end_time, caption, output_path):
    clip = VideoFileClip(video_path).subclip(start_time, end_time)
    txt_clip = TextClip(caption, fontsize=24, color='white')
    txt_clip = txt_clip.set_position('bottom').set_duration(clip.duration)
    
    video = CompositeVideoClip([clip, txt_clip])
    video.write_gif(output_path)

def main(video_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    transcription = transcribe_video(video_path)
    segments = transcription['segments']
    
    for i, segment in enumerate(segments):
        start_time = segment['start']
        end_time = segment['end']
        text = segment['text']
        output_path = os.path.join(output_dir, f"segment_{i+1}.gif")
        create_gif_segment(video_path, start_time, end_time, text, output_path)
        print(f"Created GIF: {output_path}")

if __name__ == "__main__":
    video_path = "../input_videos/video.mp4"  # Update this with the correct path to your video
    output_dir = "../generated_gifs/"  # Directory to save GIFs
    main(video_path, output_dir)

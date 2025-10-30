import os
import ffmpeg

def list_video_files(video_folder):
    return [f for f in os.listdir(video_folder) if f.lower().endswith(('.mp4', '.mov', '.avi', '.mkv'))]

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    video_folder = os.path.join(base_dir, 'video')
    audio_folder = os.path.join(base_dir, 'audio')
    os.makedirs(audio_folder, exist_ok=True)

    videos = list_video_files(video_folder)
    if not videos:
        print('No video files found in the video folder.')
        return

    print('Processing all video files:')
    for vid in videos:
        video_path = os.path.join(video_folder, vid)
        audio_filename = os.path.splitext(vid)[0] + '.mp3'
        audio_path = os.path.join(audio_folder, audio_filename)
        if os.path.exists(audio_path):
            print(f'Audio file already exists for {vid}, skipping.')
            continue
        print(f'Extracting audio from {vid}...')
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, format='mp3', acodec='libmp3lame')
            .run(overwrite_output=True)
        )
        print(f'Audio saved to {audio_path}')

if __name__ == '__main__':
    main()

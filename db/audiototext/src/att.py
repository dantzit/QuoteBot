import os
import whisper

def transcribe_audio_to_md():
    # Copy audio files from videotoaudio/audio to audiototext/audio
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_audio_dir = os.path.join(base_dir, '..', 'videotoaudio', 'audio')
    dest_audio_dir = os.path.join(base_dir, 'audio')
    os.makedirs(dest_audio_dir, exist_ok=True)
    if os.path.exists(src_audio_dir):
        for f in os.listdir(src_audio_dir):
            if f.lower().endswith('.mp3'):
                src_path = os.path.join(src_audio_dir, f)
                dest_path = os.path.join(dest_audio_dir, f)
                if not os.path.exists(dest_path):
                    import shutil
                    shutil.copy2(src_path, dest_path)
        print(f"✅ Copied audio files from {src_audio_dir} to {dest_audio_dir}")
    # Prepare text folder
    text_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'text')
    os.makedirs(text_folder, exist_ok=True)

    # Load Whisper model
    print("⏳ Loading Whisper model (this may take a minute the first time)...")
    model = whisper.load_model("base")  # Options: tiny, base, small, medium, large

    # Transcribe all audio files in the audio folder
    audio_files = [f for f in os.listdir(dest_audio_dir) if f.lower().endswith('.mp3')]
    if not audio_files:
        print("❌ No audio files found in the audio folder.")
        return
    for audio_file in audio_files:
        audio_path = os.path.join(dest_audio_dir, audio_file)
        print(f"🎧 Transcribing {audio_file}, please wait...")
        result = model.transcribe(audio_path)
        text = result["text"].strip()
        md_filename = os.path.splitext(audio_file)[0] + ".md"
        md_path = os.path.join(text_folder, md_filename)
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(f"# Transcription of {audio_file}\n\n")
            md_file.write(text + "\n")
        print(f"✅ Transcription saved as: {md_path}")

if __name__ == "__main__":
    transcribe_audio_to_md()

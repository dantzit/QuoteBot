import os
import json

def combine_md_to_json(md_folder, json_path):
    # Load existing data if json file exists
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}

    # Go through all md files in the folder
    for md_file in os.listdir(md_folder):
        if md_file.lower().endswith('.md'):
            md_path = os.path.join(md_folder, md_file)
            with open(md_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            # Remove header line (starts with '# Transcription of') and join the rest
            text_lines = [line for line in lines if not line.strip().startswith('# Transcription of')]
            text = ''.join(text_lines).strip()
            key = os.path.splitext(md_file)[0]
            if key not in data or data[key] != text:
                data[key] = text

    # Save combined data to json
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Combined markdown files into {json_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    md_folder = os.path.join(base_dir, 'audiototext', 'text')
    json_path = os.path.join(base_dir, 'combine', 'combined_transcriptions.json')
    combine_md_to_json(md_folder, json_path)

import os
import subprocess
import sys

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VTA_PATH = os.path.join(BASE_DIR, 'videotoaudio', 'src', 'vta.py')
ATT_PATH = os.path.join(BASE_DIR, 'audiototext', 'src', 'att.py')
COMBINE_PATH = os.path.join(BASE_DIR, 'combine', 'src', 'combine.py')

# Helper to run a Python script and stream output
def run_script(script_path):
    print(f"\n▶ Running: {script_path}")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode != 0:
        print(f"❌ Error running {script_path}")
        sys.exit(result.returncode)

if __name__ == "__main__":
    # Step 1: Extract audio from videos
    run_script(VTA_PATH)
    # Step 2: Transcribe audio to markdown
    run_script(ATT_PATH)
    # Step 3: Combine markdown files into JSON
    run_script(COMBINE_PATH)
    print("\n✅ Dataflow complete!")

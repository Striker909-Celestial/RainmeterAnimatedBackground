import random
import os
from datetime import datetime
import json
import sys
import logging
from pathlib import Path

# Get the directory containing the script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

FPS = 1

def recursive_data_load(root):
    out = []
    data_in = {}

    # Get the directory name without changing working directory
    dir_name = os.path.basename(root).lower()
    json_file = os.path.join(root, f"{dir_name}.json")

    logging.info(f'Loading JSON from: {json_file}')

    with open(json_file, 'r') as file:
        data_in = json.load(file)

    if data_in["type"] == "ordered":
        out.append("o")
        for f in data_in["frames"]:
            if os.path.splitext(f)[1]:  # if has file extension
                out.append(f)
            else:
                out.append(recursive_data_load(f))
    elif data_in["type"] == "random":
        out.append("r")
        for f in data_in["frames"]:
            if os.path.splitext(f["path"])[1]:  # if has file extension
                for i in range(f["weight"]):
                    out.append(f["path"])
            else:
                for i in range(f["weight"]):
                    out.append(recursive_data_load(f["path"]))

    return out

def recursive_choose_frames(arr):
    out = []
    if arr[0] == "r":
        f = random.choice(arr[1:])
        if type(f) == list:
            for n in recursive_choose_frames(f):
                out.append(n)
        else:
            out.append(f)
    elif arr[0] == "o":
        for f in arr[1:]:
            if type(f) == list:
                for n in recursive_choose_frames(f):
                    out.append(n)
            else:
                out.append(f)
    return out

# Setup logging
log_file = os.path.join(SCRIPT_DIR, 'python_script.log')
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    logging.info('Script started')
    logging.info(f'Script directory: {SCRIPT_DIR}')

    # Ensure we're working in the script's directory
    os.chdir(SCRIPT_DIR)

    # Use absolute paths
    resources_path = os.path.join(SCRIPT_DIR, "Resources")
    current_hour = str(datetime.now().hour)
    hour_path = os.path.join(resources_path, current_hour)

    logging.info(f'Resources path: {resources_path}')
    logging.info(f'Hour path: {hour_path}')

    # Rest of your existing code, but modified to use absolute paths
    dirc = recursive_data_load(hour_path)
    frames = []

    while len(frames) < 4000 * FPS:
        for f in recursive_choose_frames(dirc):
            frames.append(f)

    # Write to frames.txt in the Resources directory
    frames_file = os.path.join(resources_path, "frames.txt")
    data = "\n".join(frames)

    with open(frames_file, 'w') as f:
        f.write(data)

    logging.info(f'Successfully wrote {len(frames)} frames to {frames_file}')

except Exception as e:
    logging.error(f'An error occurred: {str(e)}')
    logging.error(f'Python executable: {sys.executable}')
    logging.error(f'Working directory: {os.getcwd()}')
    sys.exit(1)

def write_to_txt(filename, data):
    with open(filename, 'w') as f:
        f.seek(0)
        f.truncate()
        f.write(data)

dirc = recursive_data_load(os.getcwd() + "\\Resources\\" + str(datetime.now().hour))
frames = []

while len(frames) < 4000 * FPS:
    for f in recursive_choose_frames(dirc):
        frames.append(f)

# while os.getcwd()[-9:].lower() != "resources":
#     os.chdir("..")

data = ""
for frame in frames:
    data += frame + "\n"

write_to_txt("frames.txt", data)
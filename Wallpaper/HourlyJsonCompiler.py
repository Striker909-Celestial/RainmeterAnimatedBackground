import random
import os
from datetime import datetime
import json

FPS = 1

def write_to_txt(filename, data):
    with open(filename, 'w') as f:
        f.write(data)


def recursive_data_load(root):
    out = []
    data_in = {}
    os.chdir(root)
    s = root.split("\\")[-1].lower()
    with open(root + "\\" + s + ".json", 'r') as file:
        data_in = json.load(file)

    if data_in["type"] == "ordered":
        out.append("o")
        for f in data_in["frames"]:
            if f.__contains__("."):
                out.append(f)
            else:
                out.append(recursive_data_load(f))
    elif data_in["type"] == "random":
        out.append("r")
        for f in data_in["frames"]:
            if f["path"].__contains__("."):
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


dirc = recursive_data_load(os.getcwd() + "\\Resources\\" + str(datetime.now().hour))
frames = []

while len(frames) < 4000 * FPS:
    for f in recursive_choose_frames(dirc):
        frames.append(f)

while os.getcwd()[-9:].lower() != "resources":
    os.chdir("..")

data = ""
for frame in frames:
    data += frame + "\n"

write_to_txt("frames.txt", data)
import os
import json

def write_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

root = os.getcwd()
data = {}
data.update({"type": input("Is this directory an ordered loop (o) or random (r)? ")})
if data["type"] == "r":
    data.update({"type": "random"})
    dir = os.listdir(root)
    frames = []
    print("\033[3m(A file with weight 3 is 3 times or likely to be selected than a file with weight 1)\033[0m")
    for f in dir:
        if not f[-2:] == "py":
            d = {}
            d.update({"path": root + "\\" + f})
            d.update({"weight": int(input("Input a weight for " + f + ": "))})
            frames.append(d)
    data.update({"frames": frames})
else:
    data.update({"type": "ordered"})
    frames = []
    i = ""
    while i != "end":
        i = input("Input a file name or \'end\' to end: ")
        frames.append(root + "\\" + i)
    frames.remove(root + "\\end")
    data.update({"frames": frames})

write_json(root + "\\" + root.split("\\")[-1].lower() + ".json", data)
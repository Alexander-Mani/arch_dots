import os
import random

directory = "/home/lexman/images/hyprpapers/"
output_file = "/home/lexman/.config/hypr/hyprpaper.conf"

files = []
for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        files.append(filename)

if not files:
    print("No files found.")
else:
    chosen = random.choice(files)
    full_path = os.path.abspath(os.path.join(directory, chosen))

    with open(output_file, "w") as f:
        f.write("preload = " + full_path + "\n")
        f.write("wallpaper = , " + full_path + "\n")

    print("Written hyprpaper.conf with wallpaper:", full_path)


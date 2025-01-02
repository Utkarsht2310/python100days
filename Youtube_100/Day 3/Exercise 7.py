import os

path = r'/Youtube_100/ExampleFolder'
files = os.listdir(path)
i = 1

for file in files:
    if file.endswith(".png"):
        print(file)

        os.rename(os.path.join(path, file), os.path.join(path, f"{i}.png"))
        i += 1

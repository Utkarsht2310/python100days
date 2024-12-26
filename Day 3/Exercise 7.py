import os

path = r'D:\Onelogica\Python course\Yt_Python\ExampleFolder'
files = os.listdir(path)
i = 1

for file in files:
    if file.endswith(".png"):
        print(file)

        os.rename(os.path.join(path, file), os.path.join(path, f"{i}.png"))
        i += 1

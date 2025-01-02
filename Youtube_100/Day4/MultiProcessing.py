import multiprocessing
import requests
import os


def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    os.makedirs("files", exist_ok=True)  # Ensure the "files" directory exists
    with open(f"files/file{name}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Finished Downloading {name}")


if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    processes = []

    for i in range(50):
        process = multiprocessing.Process(target=downloadFile, args=(url, i))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()



import requests
import time

def download_file(url):
    print(f"Started downloading {url}...")
    response = requests.get(url)
    print(f"Finished downloading {url}...")
    return response.content

def write_to_file(n, content):
    filename = f"results/sync_{n}.html"
    with open(filename, "wb") as f:
        print(f"Started writing to {filename}...")
        f.write(content)
        print(f"Finished writing to {filename}...")

if __name__ == "__main__":
    t = time.perf_counter()
    for n, url in enumerate(open('../http/urls.txt', "r").readlines()):
        write_to_file(n, download_file(url))
    t2 = time.perf_counter() - t
    print(f"Downloading the web pages took {t2} seconds")
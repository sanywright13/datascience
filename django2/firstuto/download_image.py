import requests
import sys

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        sys.exit(1)

    with open(filename, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=8192):
            fd.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download_image.py [url] [filename]")
        sys.exit(1)

    url = sys.argv[1]
    filename = sys.argv[2]
    download_image(url, filename)
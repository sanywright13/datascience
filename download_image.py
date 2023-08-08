import requests
import argparse
import sys

def download_image(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
    except (requests.HTTPError, requests.ConnectionError) as err:
        print(f"Error occurred: {err}")
        sys.exit(1)

    with open('image.jpg', 'wb') as out_file:
        out_file.write(response.content)
    print("Image successfully downloaded.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download an image from a URL.')
    parser.add_argument('url', help='The URL of the image to download.')
    args = parser.parse_args()
    download_image(args.url)
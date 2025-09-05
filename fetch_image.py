import requests
import os
from urllib.parse import urlparse
from pathlib import Path
import hashlib

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        filename = "downloaded_image.jpg"
    return filename

def file_hash(filepath):
    """Compute SHA256 hash for a file to detect duplicates"""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def is_duplicate(new_image_content, directory):
    """Check if an image with identical content already exists"""
    new_hash = hashlib.sha256(new_image_content).hexdigest()
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            if file_hash(path) == new_hash:
                return True
    return False

def save_image(content, directory, filename):
    filepath = os.path.join(directory, filename)
    # Avoid overwriting existing files by appending a counter
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(filepath):
        filepath = os.path.join(directory, f"{base}_{counter}{ext}")
        counter += 1
    with open(filepath, 'wb') as f:
        f.write(content)
    return filepath

def fetch_image(url, directory):
    try:
        # Custom headers for respectful requests
        headers = {
            "User-Agent": "Ubuntu-Image-Fetcher/1.0 (+https://github.com/yourusername/Ubuntu_Requests)"
        }

        # Fetch the image content with timeout and headers
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check content-type header to confirm it's an image
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            print(f"✗ Skipping URL (content-type not image): {url}")
            return None

        # Prevent duplicates
        if is_duplicate(response.content, directory):
            print(f"✗ Duplicate image detected, skipping download: {url}")
            return None

        filename = get_filename_from_url(url)
        saved_path = save_image(response.content, directory, filename)

        print(f"✓ Successfully fetched: {os.path.basename(saved_path)}")
        print(f"✓ Image saved to {saved_path}")
        return saved_path

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for URL '{url}': {e}")
    except Exception as e:
        print(f"✗ An error occurred for URL '{url}': {e}")
    return None

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory if it doesn't exist
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)

    # Multiple URLs input separated by commas
    urls = input("Please enter one or more image URLs separated by commas:\n")
    url_list = [url.strip() for url in urls.split(",") if url.strip()]

    if not url_list:
        print("No valid URLs provided. Exiting.")
        return

    for url in url_list:
        fetch_image(url, directory)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()


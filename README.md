
# Ubuntu_Requests

![License](https://img.shields.io/badge/License-MIT-green)

## 🌱 About the Project

**Ubuntu_Requests** is a mindful Python tool inspired by the philosophy of Ubuntu: "I am because we are." It connects to the global web community by respectfully fetching and organizing shared image resources for later appreciation and sharing.

This script allows users to download images from the internet, handles errors gracefully, prevents duplicates, and organizes images in a structured directory — promoting the principles of **Community**, **Respect**, **Sharing**, and **Practicality**.

---

## 🚀 Features

- Prompts the user for one or more image URLs.
- Creates a directory (`Fetched_Images`) if it does not exist.
- Downloads images using the `requests` library.
- Checks HTTP response headers to confirm image content type before saving.
- Prevents saving duplicate images by hashing and comparing content.
- Respects network etiquette by sending custom headers.
- Handles errors gracefully without crashing.
- Avoids overwriting files by appending incremental suffixes.

---

## 🛠️ Tech Stack

- Python 3.x
- `requests` library

---

## 📥 Installation & Usage

### Prerequisites

Make sure you have Python 3.x installed. Install the required dependencies with:

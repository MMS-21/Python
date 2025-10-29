# 🗂️ Python File Organizer

A simple, command-line utility to **automatically organize files** in a directory into categorized subfolders (e.g., Images, Documents, Videos, etc.).

---

## 🚀 Features
- Categorizes files by extension
- Customizable categories via `categories.json`
- Displays progress and summary of moved files
- Gracefully handles duplicates and permission issues
- Cross-platform (Windows, macOS, Linux)
- Follows PEP8 and modular design

---

## 📦 Installation
```bash
git clone https://github.com/MMS-21/file-organizer.git
cd file-organizer
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

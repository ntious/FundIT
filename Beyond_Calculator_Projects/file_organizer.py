"""
File Organizer (by extension)
Author: (Your Name)    Date: 2025-10-16

Moves files into subfolders based on extension.
Inputs → Storage → Processing → Output
"""

import os, shutil, pathlib

# ---------- STORAGE ----------
DEFAULT_MAP = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".txt": "Text",
}

# ---------- INPUTS ----------
def get_folder(prompt="Folder to organize (default=.): "):
    raw = input(prompt).strip()
    return raw or "."

# ---------- PROCESSING ----------
def organize(path: str, mapping=DEFAULT_MAP):
    base = pathlib.Path(path)
    for item in base.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            target_dir = mapping.get(ext, "Other")
            dest = base / target_dir
            dest.mkdir(exist_ok=True)
            shutil.move(str(item), str(dest / item.name))

# ---------- OUTPUT ----------
def main():
    print("=== File Organizer ===")
    folder = get_folder()
    try:
        organize(folder)
        print("Files organized successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

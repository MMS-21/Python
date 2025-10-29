"""
File Organizer Script
---------------------
Automatically organizes files in a target directory into categorized subfolders
based on file extensions. Categories can be customized in categories.json.

Modules used: os, shutil, json, pathlib, sys
"""
import os
import shutil
import json
import sys
from pathlib import Path
from typing import Dict, List


def load_categories(config_path: Path) -> Dict[str, List[str]]:
    """
    Load file type categories from a JSON file.
    If the file doesn't exist, use default mappings.
    """
    default_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xls", ".xlsx", ".csv"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"]
    }

    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as file:
                categories = json.load(file)
                print(f"Loaded categories from {config_path}")
                return categories
        except json.JSONDecodeError:
            print("⚠️ Error: Invalid JSON format. Using default categories.")
            return default_categories
    else:
        print("⚠️ categories.json not found. Using default categories.")
        return default_categories


def categorize_file(file_path: Path, categories: Dict[str, List[str]]) -> str:
    """
    Determine the category folder name for a file based on its extension.
    """
    ext = file_path.suffix.lower()
    for category, extensions in categories.items():
        if ext in extensions:
            return category
    return "Others"


def organize_files(target_folder: Path, categories: Dict[str, List[str]]) -> Dict[str, int]:
    """
    Organize files in the target folder into categorized subfolders.
    Returns a summary of how many files were moved to each category.
    """
    summary = {category: 0 for category in categories.keys()}
    summary["Others"] = 0

    for item in target_folder.iterdir():
        if item.is_file():
            category = categorize_file(item, categories)
            destination_folder = target_folder / category
            destination_folder.mkdir(exist_ok=True)

            try:
                shutil.move(str(item), destination_folder / item.name)
                summary[category] += 1
                print(f"✅ Moved: {item.name} → {category}")
            except shutil.Error:
                print(f"⚠️ Skipped (already exists): {item.name}")
            except PermissionError:
                print(f"🚫 Permission denied: {item.name}")
    return summary


def print_summary(summary: Dict[str, int]) -> None:
    """
    Print a summary report of files moved.
    """
    print("\n📊 Summary:")
    for category, count in summary.items():
        if count > 0:
            print(f"  {category}: {count} file(s)")


def main():
    """
    Main execution entry point.
    """
    # Allow target folder as CLI argument, else prompt
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])
    else:
        target_input = input("Enter the path of the folder to organize: ").strip()
        target_path = Path(target_input)

    if not target_path.exists() or not target_path.is_dir():
        print("❌ Invalid folder path.")
        sys.exit(1)

    categories = load_categories(Path(__file__).parent / "categories.json")
    print(f"\nOrganizing files in: {target_path}\n")

    summary = organize_files(target_path, categories)
    print_summary(summary)
    print("\n✅ Organization complete!")


if __name__ == "__main__":
    main()

# Importing libraries
import os
from dotenv import load_dotenv
from pathlib import Path  # FIXED: Imported Path since you use .mkdir() below

# Load variables from the .env file
load_dotenv()

file_extensions = {
    "Audio": [".mp3", ".wav", ".wma", ".ogg", ".m4a", ".flac", ".aac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm", ".mpeg"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".webp", ".ico"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".pdf", ".wpd"],
    "Spreadsheets": [".xlsx", ".xls", ".csv", ".ods", ".xlsm"],
    "Presentations": [".pptx", ".ppt", ".pps", ".odp"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso", ".bz2"],
    "Code_Programming": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".cs", ".go", ".php", ".sh", ".rb", ".json", ".xml"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".apk", ".bat", ".bin"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Torrents": [".torrent"],
    "Design_3D": [".psd", ".ai", ".xd", ".fig", ".blend", ".obj", ".stl"]
}

# Functions
def get_input():
    try:
        folder_location = input("Please enter the folders path you want to organize: ")
    except Exception as e:
        print(f"An error occured: {e}")
        quit() 
    if not folder_location:
        folder_location = os.getenv("DEFUALT_FOLDER_PATH")
    return folder_location

def get_folder_name(file_path, extension_dict):
    _, ext = os.path.splitext(file_path) # It splits the text into 2 variables, we only want the extension
    ext = ext.lower() # Convert it to lower for error proofing
    
    for category, extensions in extension_dict.items():
        if ext in extensions:
            return category
        
    return "Others"

# Create all the needed folders
def setup_folders(folder_path):
    folder_names = ["Audio", "Video", "Images", "Documents", "Others", "Spreadsheets", "Presentations", "Archives", "Code_Programming", "Executables", "Fonts", "Torrents", "Design_3D"]
    for folder_name in folder_names:
        target_folder = Path(folder_path) / folder_name

        target_folder.mkdir(parents=True, exist_ok=True)

def main(folder_path):
    setup_folders(folder_path)
    
    for file in os.scandir(folder_path):
        if file.is_file():
            file_path = os.path.abspath(file)

            category = get_folder_name(file_path, file_extensions)
            destination = os.path.join(folder_path, category, file.name)

            os.rename(file_path, destination)

if __name__ == "__main__":
    folder_path = get_input()
    main(folder_path)
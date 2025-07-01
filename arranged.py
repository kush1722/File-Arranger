import os
import shutil
import sys

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".avif", ".tiff", ".ico", ".gif"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "archives": [".zip", ".rar", ".7z", ".tar"],
    "others": []  # Catch-all category
}

def create_folder(base_path, categories):
    for category in categories.keys():
        folder_path = os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_file(base_path, categories):
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in categories.items():
                if file_extension in extensions:
                    target_path = os.path.join(base_path, category)
                    try:
                        shutil.move(file_path, target_path)
                        moved = True
                        break
                    except Exception as e:
                        print(f"Error moving file {file}: {e}")
                        moved = True  # Mark as handled to avoid re-processing

            if not moved:
                other_path = os.path.join(base_path, "others")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)
                try:
                    shutil.move(file_path, other_path)
                except Exception as e:
                    print(f"Error moving file {file} to 'others': {e}")

def organize_files(target_directory):
    create_folder(target_directory, file_types)
    move_file(target_directory, file_types)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the target directory.")
    else:
        target_directory = sys.argv[1]
        if os.path.exists(target_directory):
            print(f"Organizing files in {target_directory}...")
            organize_files(target_directory)
            print("File organization completed.")
        else:
            print("The specified directory does not exist.")

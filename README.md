# Arranged

A simple Python script to organize files in a directory by their type (images, videos, music, documents, archives, and others).

## Features
- Automatically creates folders for each file type.
- Moves files into their respective folders based on extension.
- Supports common image, video, music, document, and archive formats.
- Unrecognized file types are moved to an `others` folder.

## Supported File Types
- **Images:** .jpg, .jpeg, .png, .avif, .tiff, .ico, .gif
- **Videos:** .mp4, .mkv, .avi, .mov, .flv
- **Music:** .mp3, .wav, .flac, .aac, .ogg
- **Documents:** .pdf, .docx, .txt, .xlsx, .pptx
- **Archives:** .zip, .rar, .7z, .tar
- **Others:** Any file not matching the above types

## Usage

1. Make sure you have Python 3 installed.
2. Place `arranged.py` in the directory of your choice.
3. Open a terminal or command prompt.
4. Run the script with the target directory as an argument:

```bash
python arranged.py <target_directory>
```

Replace `<target_directory>` with the path to the folder you want to organize.

### Example

```bash
python arranged.py C:\Users\YourName\Downloads
```

## Notes
- The script will create folders in the target directory and move files accordingly.
- Files that cannot be moved will print an error message.

## License
This project is provided as-is for personal use. 

import os
import shutil

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

files = (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt",
         ".pptx", ".txt", ".rtf", ".odt", ".ods", ".odp",
         ".odg", ".odf", ".odc", ".odb", ".odm", ".ott",
         ".otp", ".otg", ".otf", ".oti", ".otc",
         ".otm", ".ots", ".csv", ".json", ".pem")

source_dir = (input("\n\nEnter the complete path of the folder you want to organize by select that folder and press "
                    "'shift+ctrl+c': ").replace('"', ''))

os.chdir(source_dir)
os.getcwd()


def ensure_dir_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


with os.scandir(source_dir) as entries:
    for entry in entries:
        if entry.is_file():  # Only process files, not directories
            name = entry.name
            src_path = os.path.join(source_dir, name)
            if name.endswith(audio):
                dest_dir = os.path.join(source_dir, "audios")
            elif name.endswith(video):
                dest_dir = os.path.join(source_dir, "videos")
            elif name.endswith(img):
                dest_dir = os.path.join(source_dir, "images")
            elif name.endswith(files):
                dest_dir = os.path.join(source_dir, "files")
            else:
                dest_dir = os.path.join(source_dir, "others")

            ensure_dir_exists(dest_dir)
            dest_path = os.path.join(dest_dir, name)
            print(f"Moving {src_path} to {dest_path}")
            try:
                shutil.move(src_path, dest_path)
            except Exception as e:
                print(f"Error moving file {name}: {e}")

print("File organization complete.")

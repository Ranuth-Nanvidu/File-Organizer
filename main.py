"""Some Times This Program Might Not Work Properly At The First Run Please Run Second Time It Will Works"""

# Created With Love By Ranuth Nanvidu
# To Properly Work This Program Please Put Your Folder Path In Below Variable Named "path" Inside The Double Quotations

# Import All Needed Modules And Packages
import os
import shutil

# Define All The Type Of File Extentions That Supports In This Program With Their Catorgaries
file_types = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", "otd", ".md", ".tex"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp", ".key"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".fly", ".webm"],
    "Audios": [".mp3", ".wav", ".acc", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Executables": [".exe", ".msi", ".bat", ".cmd", ".sh", ".appimage"],
    "Codes": [".py", ".java", ".c", ".cpp", ".js", ".ts", ".html", ".css", ".php", ".go", ".rs", ".ipynb", ".json", ".xml", ".yaml", ".yml"],
    "Databases": [".db", ".sqlite", ".sqlite3", ".mdb", ".accdb"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Designs": [".psd", ".ai", ".xd", ".fig", ".dwg", ".dxf", ".sketch"],
    "Disk Images": [".iso", ".img", ".dmg", ".vhd", ".vmdk"],
    "Torents": [".torrent"],
    "Logs": [".log"],
    "Backups": [".bak", ".tmp", ".old"]
}

# Declear Lists
file_names = []
exts = []

# Define File Path
path = r"FILE PATH"  # Please Edit The Srings With Related File Path

# Get All The File And Folder Names
all_files = os.listdir(path)


for i in all_files:
    full_path = os.path.join(path, i)
    
    # Cheak Weather That The Element Is a File Or A Folder
    if os.path.isfile(full_path):
        file_name,ext = os.path.splitext(i) # Split the File Name And Its Extention
        exts.append(ext.lower()) # Append The Extentions To A List With Full Simple 
        file_names.append(file_name) # Append File Names
        
unique_exts = list(dict.fromkeys(exts)) # Remove Duplicates And Store The Extentions In A New List

def make_folders(folder_name):
    """This Function Is Used to Make Related Folders And Remove The Related File Extentions From That Unique List"""
    os.makedirs(os.path.join(path, folder_name), exist_ok = True)
    for y in unique_exts:
        if y in file_types[folder_name]:
            unique_exts.remove(y)
    return

# Call To The Fuction Above By Considering The File Extention           
for z in unique_exts:
    if z in file_types["Documents"]:
        make_folders("Documents")
        
    elif z in file_types["Spreadsheets"]:
        make_folders("Spreadsheets")
        
    elif z in file_types["Presentations"]:
        make_folders("Presentations")
        
    elif z in file_types["Images"]:
        make_folders("Images")
        
    elif z in file_types["Videos"]:
        make_folders("Videos")
        
    elif z in file_types["Audios"]:
        make_folders("Audios")
        
    elif z in file_types["Archives"]:
        make_folders("Archives")
        
    elif z in file_types["Executables"]:
        make_folders("Executables")
        
    elif z in file_types["Codes"]:
        make_folders("Codes")
        
    elif z in file_types["Databases"]:
        make_folders("Databases")
        
    elif z in file_types["Fonts"]:
        make_folders("Fonts")
        
    elif z in file_types["Designs"]:
        make_folders("Designs")
        
    elif z in file_types["Disk Images"]:
        make_folders("Disk Images")
        
    elif z in file_types["Torents"]:
        make_folders("Torents")
        
    elif z in file_types["Logs"]:
        make_folders("Logs")
        
    elif z in file_types["Backups"]:
        make_folders("Backups")
        
    else:
        os.makedirs(os.path.join(path, "Others"), exist_ok = True)
        

def move_file(folder, file_name):
    """This Function Help To Move Files To Related Folders"""
    dest_folder = os.path.join(path, folder)
    src = os.path.join(path,file_name)
    dest = os.path.join(dest_folder, file_name)
    shutil.move(src, dest)
    return

# Call To The Fuction Above By Considering The File Extention 
for q in range(len(exts)):
    full_file_name = file_names[q] + exts[q]
       
    if exts[q] in file_types["Documents"]:
        move_file("Documents", full_file_name)
        
    elif exts[q] in file_types["Spreadsheets"]:
        move_file("Spreadsheets", full_file_name)
        
    elif exts[q] in file_types["Presentations"]:
        move_file("Presentations", full_file_name)
        
    elif exts[q] in file_types["Images"]:
        move_file("Images", full_file_name)
        
    elif exts[q] in file_types["Videos"]:
        move_file("Videos", full_file_name)
        
    elif exts[q] in file_types["Audios"]:
        move_file("Audios", full_file_name)
        
    elif exts[q] in file_types["Archives"]:
        move_file("Archives", full_file_name)
        
    elif exts[q] in file_types["Executables"]:
        move_file("Executables", full_file_name)
        
    elif exts[q] in file_types["Codes"]:
        move_file("Codes", full_file_name)
        
    elif exts[q] in file_types["Databases"]:
        move_file("Databases", full_file_name)
        
    elif exts[q] in file_types["Fonts"]:
        move_file("Fonts", full_file_name)
        
    elif exts[q] in file_types["Designs"]:
        move_file("Designs", full_file_name)
        
    elif exts[q] in file_types["Disk Images"]:
        move_file("Disk Images", full_file_name)
        
    elif exts[q] in file_types["Torents"]:
        move_file("Torents", full_file_name)
        
    elif exts[q] in file_types["Logs"]:
        move_file("Logs", full_file_name)
        
    elif exts[q] in file_types["Backups"]:
        move_file("Backups", full_file_name)
        
    else:
        move_file("Others", full_file_name)
        
# Output The Value Done If The Program Works         
print("Done!!!")

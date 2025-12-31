# 📂 Automatic File Organizer (Python)

A simple Python script that **automatically organizes files** in a folder into categorized subfolders based on their file extensions (Documents, Images, Videos, Codes, and more).

Created with ❤️ by **Ranuth Nanvidu**

---

## 🚀 Features

* Automatically scans a given directory
* Creates folders based on file type (if they don’t already exist)
* Moves files into appropriate folders
* Supports **20+ file categories**
* Works on **Windows, Linux, and macOS**
* No external libraries required

---

## 📁 Supported Categories

* Documents
* Spreadsheets
* Presentations
* Images
* Videos
* Audios
* Archives
* Executables
* Codes
* Databases
* Fonts
* Designs
* Disk Images
* Torrents
* Logs
* Backups
* Others (for unsupported extensions)

---

## 🛠 Requirements

* Python **3.7 or higher**
* Uses only standard Python libraries:

  * `os`
  * `shutil`

---

## 📌 How to Use

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Edit the folder path**

   Open `main.py` and change the path variable:

   ```python
   path = r"FILE PATH"
   ```

   Example:

   ```python
   path = r"C:\Users\YourName\Downloads"
   ```

3. **Run the script**

   ```bash
   python main.py
   ```

4. 🎉 Files will be organized automatically.

---

## 📂 Example

**Before:**

```
Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
├── script.py
```

**After:**

```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audios/
│   └── song.mp3
├── Codes/
│   └── script.py
```

---

## ⚠️ Important Notes

* Only files in the root directory are processed
* Subfolders are ignored
* Existing folders will not be overwritten
* Unknown file types are moved to the **Others** folder

---

## 📜 License

This project is open-source and free to use for learning and personal projects.

---

## 🤝 Contributing

Contributions are welcome!

* Add more file extensions
* Improve performance
* Refactor the code
* Open issues or pull requests

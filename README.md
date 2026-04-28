# File Type Identifier Tool

## 📌 Overview
The File Type Identifier Tool is a defensive cybersecurity utility written in Python that identifies the real type of a file by analyzing its binary header (magic numbers) instead of relying on its file extension.

This tool helps detect potentially malicious or suspicious files, such as executables disguised as harmless formats like .pdf, .jpg, or .png.

---

## 🎯 Project Goals
- Analyze file headers using magic numbers
- Identify the real file type based on binary signatures
- Compare the detected file type with the file extension
- Detect and flag mismatches that may indicate disguised files
- Provide a safe, read-only, defensive analysis tool for learning purposes

---

## 🧠 How It Works
1. The tool reads the first bytes of a file in binary mode  
2. The raw header is displayed in hexadecimal format  
3. The header is compared against a database of known magic numbers  
4. The detected file type is compared with the file extension  
5. The tool reports whether the file is compatible or suspicious  

---

## 📂 Project Structure
file-type-identifier-tool/  
│  
├── file_type_identifier.py     # Main file analysis tool  
├── create_test_files.py        # Script to generate test files  
├── test_files/                 # Legitimate and disguised test files  
└── README.md  

---

## 🧪 Supported File Types
The tool currently supports detection of the following formats:
- PDF (Portable Document Format)
- JPG / JPEG (Image format)
- PNG (Portable Network Graphics)
- ZIP (Compressed archive)
- EXE (Windows Executable)

New formats can be added by extending the magic number database.

---

## ▶️ Usage

### Requirements
- Python 3.x

### Run the tool
Execute the following command in the project directory:

    python file_type_identifier.py

You will be prompted to enter the **absolute path** of the file you want to analyze.

---

## 📊 Example Output

    === File Analysis ===
    Extension: .jpg
    Real type detected: EXE
    Header (hex): 4d5a900003000000
    Result: ⚠️ POSSIBLE MISMATCH: Real type is EXE but extension is jpg

---

## 🧪 Testing the Tool

### Generate Test Files
This project includes a script that generates both legitimate and disguised files for testing.

Run:

    python create_test_files.py

This will create a `test_files/` directory containing:
- Legitimate files (matching extension and magic number)
- Disguised files (magic number does NOT match the extension)

Example disguised scenarios:
- Executable disguised as PDF
- ZIP archive disguised as JPG
- PNG file disguised as ZIP

These files are safe and contain only minimal binary headers for testing.

---

## 🔐 Security & Ethics
- This is a **defensive security tool**
- Files are **never executed**
- Files are **not modified or moved**
- Analysis is **read-only**
- Intended strictly for **educational purposes**

---

## 🧠 What This Project Demonstrates
- Understanding of file headers and magic numbers
- Binary file handling in Python
- Basic malware detection techniques
- Why file extensions are unreliable for security
- Secure and ethical defensive programming practices

---

## 🚀 Possible Improvements
- Support for additional file formats
- Directory scanning
- Command-line arguments (CLI flags)
- Report generation (TXT or CSV)
- Logging and alert system

---

## 📄 Disclaimer
This project was created for educational purposes only.  
The author is not responsible for any misuse of this tool.

---

## 👤 Author
Guilherme Soato  
Cybersecurity student and Python learner

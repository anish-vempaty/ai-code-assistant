# AI Code Assistant (Gemini 2.5 Flash Version)

## 🧠 Goal
Build a desktop app that:
1. Asks for a project folder
2. Opens it in VS Code
3. Shows Gemini Flash suggestions in a GUI
4. Applies changes after approval

---

## 📦 Requirements
```bash
pip install google-generativeai python-dotenv PyQt6
```

Also:
- Install VS Code and make sure the `code` CLI works.
- Get your Gemini API key from https://aistudio.google.com/app/apikey

Create a `.env` file:
```env
GEMINI_API_KEY=your-api-key-here
```

---

## 📁 Project Structure
```
ai_code_assistant/
├── app.py
├── gemini_review.py
├── file_utils.py
├── vscode_launcher.py
├── .env
```

---

## 🧠 File: gemini_review.py
```python
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def review_code(content, filename):
    prompt = f"You are a senior software engineer. Review this code in {filename} and suggest improvements. Return the updated version or say 'NO CHANGES REQUIRED'.\n\n" + content

    response = model.generate_content(prompt)
    return response.text.strip()
```

---

## 📁 File: file_utils.py
```python
import os

def get_code_files(project_dir, exts=(".py", ".js", ".ts", ".java")):
    code_files = []
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(exts):
                code_files.append(os.path.join(root, file))
    return code_files
```

---

## 📁 File: vscode_launcher.py
```python
import subprocess

def open_in_vscode(path):
    subprocess.run(["code", path])
```

---

## 🖥️ File: app.py (GUI using PyQt6)
```python
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QListWidget, QTextEdit
)
from file_utils import get_code_files
from gemini_review import review_code
from vscode_launcher import open_in_vscode

class CodeReviewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gemini Code Reviewer")
        self.resize(800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Select your project folder")
        self.layout.addWidget(self.label)

        self.select_btn = QPushButton("Browse Folder")
        self.select_btn.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_btn)

        self.file_list = QListWidget()
        self.layout.addWidget(self.file_list)

        self.review_output = QTextEdit()
        self.review_output.setReadOnly(True)
        self.layout.addWidget(self.review_output)

        self.apply_btn = QPushButton("Apply Suggestion")
        self.apply_btn.clicked.connect(self.apply_suggestion)
        self.layout.addWidget(self.apply_btn)

        self.selected_file = None
        self.project_dir = None

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.project_dir = folder
            open_in_vscode(folder)
            self.file_list.clear()
            files = get_code_files(folder)
            for f in files:
                self.file_list.addItem(f)
            self.file_list.itemClicked.connect(self.review_selected_file)

    def review_selected_file(self, item):
        self.selected_file = item.text()
        with open(self.selected_file, 'r', encoding='utf-8') as f:
            content = f.read()
        suggestion = review_code(content, self.selected_file)
        self.review_output.setPlainText(suggestion)

    def apply_suggestion(self):
        if self.selected_file and self.review_output.toPlainText() != "NO CHANGES REQUIRED":
            with open(self.selected_file, 'w', encoding='utf-8') as f:
                f.write(self.review_output.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CodeReviewer()
    window.show()
    sys.exit(app.exec())
```

---

## ✅ To Run
```bash
python app.py
```
Then select a folder, view file suggestions, and apply edits with a click.


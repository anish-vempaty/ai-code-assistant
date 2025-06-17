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
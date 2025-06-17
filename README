
# 🧠 AI Code Assistant (Gemini Flash Edition)

A desktop-based AI-powered coding assistant that reviews your source code files using **Gemini 2.5 Flash API** and suggests improvements — all through a clean GUI, no CLI required.

---

## 🚀 Features

- ✅ **Cross-platform GUI** using PyQt6
- 🔍 **Reads your entire project directory**
- 🤖 **Analyzes each file** with Gemini Flash (free tier compatible!)
- ✏️ **Suggests refactors, improvements, and bug fixes**
- ✅ **Apply edits with one click**
- 🧑‍💻 **Automatically opens project in VS Code**
- 🔐 Secure API key management with `.env`

---

##  `requirements.txt`

Create a `requirements.txt` file with this:

```txt
google-generativeai==0.3.2
python-dotenv==1.0.1
PyQt6==6.6.1
```

> Run this to generate it automatically:

```bash
pip freeze > requirements.txt
```

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/anish-vempaty/ai-code-assistant.git
cd ai-code-assistant
````

### 2. Set up environment

```bash
python -m venv venv
venv\\Scripts\\activate         # Windows
# or
source venv/bin/activate        # Linux/macOS

pip install -r requirements.txt
```

### 3. Add your Gemini API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

> Get your key from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## 🖥️ Usage

```bash
python app.py
```

* Choose your project folder.
* The app opens it in VS Code.
* Click on files to get AI suggestions.
* Click **Apply Suggestion** to update the file.

---

## 📦 Build Executable

### Windows `.exe`:

```bash
pyinstaller --noconsole --onefile app.py
```

### Linux:

```bash
pyinstaller --onefile app.py
```

> Find the executable in the `dist/` folder.

---

## 💡 Tech Stack

* `PyQt6` – for GUI
* `google-generativeai` – Gemini Flash API
* `dotenv` – for managing secrets
* `VS Code CLI` – to auto-open projects

---

## 🙌 Credits

Built by [Anish Vempaty](https://github.com/anish-vempaty)
Powered by [Gemini Flash API](https://ai.google.dev)

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---



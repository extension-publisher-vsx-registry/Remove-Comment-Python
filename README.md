# Usage Documentation: Python Remove Comment

<img src="https://raw.githubusercontent.com/DwiDevelopes/pos-file-view/main/main.gif" alt="Python Remove Comment Demo" width="100%" />

The **Python Remove Comment** extension (`python-remove-comment`) is designed to help you remove `#` comments from Python code quickly, easily, and precisely right inside Visual Studio Code.

<a href="https://gitanimals.org"><img src="https://render.gitanimals.org/farms/dwidevelopes" alt="GitAnimals Farm" width="600" height="300" /></a>

---

## 📌 Extension Information

* **Extension Name:** Python Remove Comment (`python-remove-comment`)
* **Publisher:** `dwidevelopes`
* **Version:** `1.0.0`
* **Minimum VS Code Version:** `^1.90.0`

---

## ✨ Key Features

* **`#` Comment Removal:** Cleanly removes comment lines or code blocks starting with `#`.
* **Right-Click Context Menu Integration:** Easily invoked via right-click when selecting code snippets.
* **Quick Access Editor Title Bar:** Provides a 1-click execution button at the top-right corner of the editor tab.
* **Command Palette Integration:** Fully supports standard VS Code command execution (`Ctrl+Shift+P` / `Cmd+Shift+P`).

---

## 🚀 How to Use

The comment removal feature is specifically activated for **Python** files (`.py`). You can execute it in 3 ways:

### 1. Via Right-Click (Editor Context Menu)

1. Open a Python file (`.py`).
2. **Select / Highlight** the code block containing the `#` comments you want to remove.
3. Right-click on the selected text area.
4. Choose **`Python: Remove Python Comment (#)`**.

### 2. Via Editor Title Bar (Top-Right Corner of Tab)

1. Open a Python file (`.py`) in the editor.
2. Look at the group of action buttons in the top-right corner of the editor tab.
3. Click the **Python: Remove Python Comment (#)** icon.

### 3. Via Command Palette

1. Open a Python file (`.py`).
2. Press `Ctrl + Shift + P` (Windows/Linux) or `Cmd + Shift + P` (macOS).
3. Type and select **`Python: Remove Python Comment (#)`**.

---

## ⚙️ Command Details & Activation Conditions (*When Clause*)

| Command | UI Location | Activation Requirement (*When Clause*) |
| --- | --- | --- |
| `extension.removePythonComments` | **Editor Context Menu** (`editor/context`) | Text is selected & file is Python (`editorHasSelection && editorLangId == 'python'`) |
| `extension.removePythonComments` | **Tab Title Context Menu** (`editor/title/context`) | File is Python (`resourceLangId == 'python'`) |
| `extension.removePythonComments` | **Editor Title Bar** (`editor/title`) | File is Python (`resourceLangId == 'python'`) |
# 🌐 Language Translator Application

A simple and user-friendly *Tkinter and Python based  GUI application* that translates text into multiple languages using *Googletrans*.

This project demonstrates GUI development with Tkinter, asynchronous translation handling with asyncio, and integration with the googletrans API.

---

## 🚀 Features

* Translate text into *100+ languages*
* Simple and clean GUI built with *Tkinter*
* Dropdown menu to select the output language
* Uses *googletrans* for fast translation
* Asynchronous translation for smoother performance

---

## 🛠️ Technologies Used

* *Python*
* *Tkinter* (GUI)
* *Googletrans*
* *Asyncio*

---

## 📦 Installation

### 1. Clone the repository

bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


### 2. Install required packages

Make sure you have Python installed, then run:

bash
pip install googletrans==4.0.0-rc1


(This is the stable version for most systems)

---

## ▶️ How to Run the Application

Run the Python file:

bash
python yourfilename.py


The GUI window will open.

---

## 🖥️ How It Works

### ✔️ Input Section

* Type text you want to translate in the *input text box*.

### ✔️ Language Selection

* Select the *destination language* from the dropdown.

### ✔️ Output Section

* Click the *Translate* button.
* The translated text will appear in the output box.

---


## 🧠 Code Overview

### Key Components:

* Tk() — creates the main GUI window
* Entry — input text field
* Text — output text area
* Combobox — language selection
* googletrans.Translator() — performs translation
* asyncio.run() — handles asynchronous translation

---



## ⭐ Future Improvements

* Add text-to-speech
* Add input language auto-detection
* Improve UI styling
* Add dark mode


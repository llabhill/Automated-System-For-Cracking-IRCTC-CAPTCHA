# IRCTC Captcha Solver Script (Selenium + EasyOCR)

This project demonstrates how to extract and solve the IRCTC captcha using Python, Selenium, and EasyOCR. A sample GIF is included to show how the script works.

---

## 🚀 Features

* Extracts captcha image from base64
* Decodes captcha using **EasyOCR**
* Inputs captcha automatically into the IRCTC form
* Can be integrated with login flows (optional)
* Shows a GIF demo of the script solving the captcha

---

## 📌 Demo (How the Script Works)

Below is the GIF showcasing the script's working:

![IRCTC Selenium Script Demo](https://github.com/user-attachments/assets/6ff136e7-741d-4d99-a18b-0880fca7f129)

---

## 🛠️ Requirements

Install required Python packages:

```bash
pip install selenium easyocr opencv-python matplotlib
```

Download a compatible **ChromeDriver** and place it in your project folder.

---

## 📄 Script Overview

The script performs the following tasks:

1. Sets up Selenium Chrome WebDriver
2. Opens IRCTC login popup (optional)
3. Extracts captcha from HTML (base64 image)
4. Uses EasyOCR to decode captcha
5. Inputs captcha into the field

> Note: Full login automation is **not** the main purpose of this script. The core goal is captcha extraction + solving.

---

## 🧩 How Captcha Extraction Works

IRCTC shows captcha as a **base64 encoded inline image**. This script:

* Reads the `src` attribute
* Converts base64 to an image file
* Runs OCR on it
* Types detected text

---

## ▶️ Running the Script

Run the Python script:

```bash
python irctc_login.py
```

Make sure your Chrome version matches your ChromeDriver version.

---

## ⚠️ Disclaimer

This script is for **educational purposes only**.
Automating IRCTC login may violate IRCTC terms of service. Use responsibly.

---

## 📬 Contact

If you want enhancements (better captcha accuracy, rotation fixes, UI improvements), feel free to ask!

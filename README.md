# 📝 Handwritten Text Recognition Using OCR

A Python-based Optical Character Recognition (OCR) application that extracts text from images using **OpenCV**, **Pytesseract**, and **Object-Oriented Programming (OOP)**.

This project processes multiple images from a folder, enhances them using image preprocessing techniques, and extracts text using the Tesseract OCR engine.

---

## 📌 Features

- Extracts text from multiple images automatically
- Uses Object-Oriented Programming (OOP)
- Image preprocessing for improved OCR accuracy
- Supports multiple image formats
- Saves extracted text into separate `.txt` files
- Simple and easy-to-understand implementation

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- Pytesseract
- Tesseract OCR
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```
Handwritten-Text-Recognition/
│
├── images/
│   ├── Note1.jpg
│   ├── Assignment.png
│   ├── Quote.png
│   └── Report.png
│
├── Hand written text recognition.py
├── README.md
└── requirements.txt
```

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install opencv-python pytesseract
```

---

## Install Tesseract OCR

Download and install **Tesseract OCR** for Windows.

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the Tesseract path in the Python file if necessary.

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/handwritten-text-recognition.git
```

2. Navigate to the project folder.

```bash
cd handwritten-text-recognition
```

3. Place your images inside the **images** folder.

4. Run the program.

```bash
python "Hand written text recognition.py"
```

---

## 🖼 Supported Image Formats

- JPG (.jpg)
- JPEG (.jpeg)
- PNG (.png)
- JFIF (.jfif)

---

## 🔄 Workflow

The application performs the following steps:

1. Reads all supported images from the **images** folder.
2. Converts each image to grayscale.
3. Removes noise using Gaussian Blur.
4. Applies Adaptive Thresholding.
5. Extracts text using the Tesseract OCR engine.
6. Displays the extracted text in the terminal.
7. Saves the extracted text as a `.txt` file.

---

## 📸 Sample Output

```
============================================================
File: Note1.jpg
============================================================

Python Programming

Python is an easy-to-learn programming language.
It is widely used in Artificial Intelligence,
Machine Learning, Web Development, and Automation.

============================================================
OCR completed successfully!
Extracted text files have been saved.
============================================================
```

---

## 📁 Output Files

For every processed image, the program automatically generates a text file.

Example:

```
Note1.txt
Assignment.txt
Quote.txt
Report.txt
```

---

## 💡 Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Image Processing
- Computer Vision
- Optical Character Recognition (OCR)
- File Handling
- Python Automation

---

## 🚀 Future Improvements

- GUI using Tkinter
- Drag-and-drop image upload
- PDF document support
- OCR confidence score
- Export results to CSV
- Real-time webcam OCR
- Support for AI-based OCR models such as EasyOCR or TrOCR

---

## 👩‍💻 Author

**Hafsa Anwar**

BS Robotics & Intelligent Systems

---

## 📄 License

This project is developed for educational and learning purposes.

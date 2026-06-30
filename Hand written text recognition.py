import os
import cv2
import pytesseract

# -------------------------------
# Configure Tesseract OCR Path
# -------------------------------
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

class HandwrittenOCR:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def preprocess_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        return binary

    def extract_text(self):
        if not os.path.exists(self.folder_path):
            print("Folder not found!")
            return

        image_extensions = (".jpg", ".jpeg", ".png")

        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(image_extensions):
                image_path = os.path.join(self.folder_path, filename)

                image = cv2.imread(image_path)

                if image is None:
                    print(f"Could not read: {filename}")
                    continue

                processed_image = self.preprocess_image(image)
                extracted_text = pytesseract.image_to_string(processed_image)

                print("=" * 50)
                print(f"File: {filename}")
                print("-" * 50)
                print(extracted_text.strip())
                print()


if __name__ == "__main__":
    folder_path = "images"      # Change this to your image folder
    ocr = HandwrittenOCR(folder_path)
    ocr.extract_text()
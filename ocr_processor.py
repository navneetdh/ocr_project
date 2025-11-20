import pytesseract, os
from PIL import Image
from logger import logger

pytesseract.pytesseract.tesseract_cmd = r"c:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def process_task(file_path, output_dir):
    """Processes an image file and saves the extracted text to the output directory."""
    try:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save the extracted text
        text_filename = os.path.join(output_dir, os.path.splitext(os.path.basename(file_path))[0] + ".txt")
        with open(text_filename, "w", encoding="utf-8") as text_file:
            text_file.write(text)
        
        print(f"Processed: {file_path} -> {text_filename}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
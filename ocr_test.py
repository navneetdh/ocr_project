import os
# c:\Program Files\Tesseract-OCR\tesseract.exe
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"c:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def image_to_text(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        # Check if it's an image file
        if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif')):
            try:
                # Open image and extract text
                img = Image.open(file_path)
                text = pytesseract.image_to_string(img)
                
                # Define output text file path
                text_filename = os.path.splitext(filename)[0] + ".txt"
                output_path = os.path.join(output_dir, text_filename)
                
                # Save extracted text to file
                with open(output_path, "w", encoding="utf-8") as text_file:
                    text_file.write(text)
                
                print(f"Processed: {filename} -> {text_filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = "D:\Shared Folder\Courses\PROJECTS\OCR_PROJECT\word\\1\\"  # Change to your input directory containing images
    output_directory = "D:\Shared Folder\Courses\PROJECTS\OCR_PROJECT\Output\\"  # Change to your output directory for text files
    image_to_text(input_directory, output_directory)

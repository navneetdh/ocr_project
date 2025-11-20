import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from ocr_processor import process_task

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Application")

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.text_area.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.tiff;*.bmp;*.gif")]
        )
        if file_path:
            extracted_text = process_task(file_path)
            if extracted_text:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, extracted_text)
            else:
                messagebox.showerror("Error", "Failed to extract text from the image.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
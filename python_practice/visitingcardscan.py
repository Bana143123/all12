import cv2
import pytesseract
from tkinter import Tk, Label, Button, filedialog, Text
from PIL import Image, ImageTk

# Ensure tesseract is set to the correct path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Span63\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class VisitingCardScanner:
    def __init__(self, master):
        self.master = master
        master.title("Visiting Card Scanner")

        self.label = Label(master, text="Upload a visiting card image")
        self.label.pack()

        self.upload_button = Button(master, text="Upload", command=self.upload_image)
        self.upload_button.pack()

        self.image_label = Label(master)
        self.image_label.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

        self.extract_button = Button(master, text="Extract Text", command=self.extract_text, state='disabled')
        self.extract_button.pack()

        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()

    def upload_image(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.filepath:
            image = Image.open(self.filepath)
            image.thumbnail((300, 300))
            self.image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.image)
            self.extract_button.config(state='normal')

    def extract_text(self):
        if self.filepath:
            img = cv2.imread(self.filepath)
            text = pytesseract.image_to_string(img)
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", text)

root = Tk()
scanner = VisitingCardScanner(root)
root.mainloop()

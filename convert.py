import tkinter as tk
from tkinter.filedialog import askopenfile
import PyPDF2
from PIL import Image, ImageTk
# import fitz
# import glob, os

# window object to hold all elements of our interface
root = tk.Tk()

# increase the window's dimensions
canvas = tk.Canvas(root, width=300, height=300)
# initialize the canvas
canvas.grid(columnspan=3)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instructions
instructions = tk.Label(
    root, text="Select a PDF file on your computer to change to a Text file", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# function to open browser for pdf files


def open_file():
    browse_text.set("loading..")
    file = askopenfile(parent=root, mode='rb', title="Choose a pdf file", filetypes=[
                       ("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        num_pages = read_pdf.numPages
        page = read_pdf.getPage(num_pages-2)
        page_content = page.extractText()

    text_box = tk.Text(root, height=200, width=250, padx=15, pady=15)
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center", justify="center")
    text_box.grid(column=1, row=3)
    browse_text.set('Browse')


# Button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(
), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


canvas = tk.Canvas(root, width=600, height=250)
# initialize the canvas
canvas.grid(columnspan=3)

root.mainloop()

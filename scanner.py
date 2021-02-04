import cv2
import os
import shutil
import pytesseract
from tkinter import *
from tkinter import filedialog as fd

root = Tk()

root.title('Scanner')
Label(root, text=os.getcwd()).pack() # Local direcotory

def scan_img():
    # Scan and add to clipboard
    root.clipboard_clear()
    label_final.delete('1.0',END)
    img = fd.askopenfilename()
    folder = img
    full_img = cv2.imread(img)
    custom_oem_psm_config = r'--oem 1 --psm 4'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' # Local PATH of tesseract to scan image on Windows
    text = pytesseract.image_to_string(img,config=custom_oem_psm_config, lang="rus")
    label_filename.config(text=folder)
    label_final.insert(END,text)
    root.clipboard_append(text)
    resized_but.config(command=lambda: cv2.imshow('Image', full_img))


def save_from_text():
    root.clipboard_clear()
    label_final_get = label_final.get('1.0',END)
    root.clipboard_append(label_final_get)
    root.update()

Button(root,text='Scan',command=scan_img, padx=15, pady=15).pack()
label_filename = Label(root, text='Your folder')
label_filename.pack()
label_final = Text(root, height=30,width=100)
label_final.pack()
Button(root, text='Copy', command=save_from_text,padx=15,pady=15).pack()
resized_but = Button(root, text='Open Full Image', padx=15)
resized_but.pack()
root.mainloop()

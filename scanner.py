import cv2
import os
import shutil
import pytesseract
from tkinter import *
from tkinter import filedialog as fd

'''Options for page segmentation modes(psm):

0: Orientation and script detection (OSD) only.
1: Automatic page segmentation with OSD.
2: Automatic page segmentation, but no OSD, or OCR.
3: Fully automatic page segmentation, but no OSD. (Default)
4: Assume a single column of text of variable sizes.
5: Assume a single uniform block of vertically aligned text.
6: Assume a single uniform block of text.
7: Treat the image as a single text line.
8: Treat the image as a single word.
9: Treat the image as a single word in a circle.
10: Treat the image as a single character.
11: Sparse text. Find as much text as possible in no particular order.
12: Sparse text with OSD.
13: Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

OCR Engine Mode(oem)

Tesseract has different engine modes for speed and performance

0: Legacy engine only.
1: Neural nets LSTM engine only.
2: Legacy + LSTM engines.
3: Default, based on what is available. '''

root = Tk()

root.title('Scanner')
Label(root, text=os.getcwd()).pack() # Текущая директория

def scan_img():
    # Отсканировать и добавить в буфер обмена
    root.clipboard_clear()
    label_final.delete('1.0',END)
    img = fd.askopenfilename()
    folder = img
    full_img = cv2.imread(img)
    custom_oem_psm_config = r'--oem 1 --psm 4'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
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

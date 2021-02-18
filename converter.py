from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import ImageTk, Image
root = Tk()
root.geometry("400x400")
root.title("Image_Conversion_App")


def dwg_to_jpg():
    filename = fd.askopenfilename()
    if filename.endswith(".dwg"):
        Image.open(filename).save("edited.jpg")
        Label_1 = Label(root, text="Done", width=20, fg="green", font=("bold", 15))
        Label_1.place(x=80, y=280)
    else:
        Label_2 = Label(root, text="Error!", width=20, fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)


Label_3 = Label(root, text="Choose File", width=20, font=("bold", 15))
Label_3.place(x=80, y=80)

Button(root, text="DWG_to_JPG", width=20, height=2, bg="brown", fg="white", command=dwg_to_jpg).place(x=120, y=120)

root.mainloop()

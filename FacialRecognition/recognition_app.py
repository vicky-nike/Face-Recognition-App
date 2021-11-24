from tkinter import *
from tkinter import messagebox
import tkinter.font as tkfont
import cv2
import os
import face_recongnition
import pandas as pd

root = Tk()
root.title('Recognition app')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='face-id.png'))

def detect():
    found = face_recongnition.testDetect()
    #found = testDetect()
    messagebox.showinfo("Information","Recogonised as {}".format(found))

# Button defination
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
root.geometry("200x250")
label = Label(root, text = 'Face Enrollment', fg= "red", font=bold_font, justify ="left")
button1 = Button(root, text="Detect", bg = "#006aff",font=bold_font, fg = "white", justify ="center", height=1, width=10, command=detect)

# Put buttons on screen
label.place(x=36, y=20)
button1.place(x=45, y=160)

root.mainloop()
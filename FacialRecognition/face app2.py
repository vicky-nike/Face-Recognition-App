from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import matplotlib.pyplot as plt
import tkinter.font as tkfont
import cv2
import random
import os

root = Tk()
root.title('Face detection app')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='FacialRecognition/face-id.png'))
#root.geometry("700x400")
root.attributes("-fullscreen", True)
root.bind('<Escape>', lambda event: root.state('normal'))

#functions
def home():
    #Button color change
    global homeButton, enrollNewButton, editDatabaseButton, settingsButton
    homeButton.configure(bg="#2626ff", fg='white')
    enrollNewButton.configure(bg="white", fg='#4d3ce6')
    editDatabaseButton.configure(bg="white", fg='#4d3ce6')
    settingsButton.configure(bg="white", fg='#4d3ce6')

    #font details
    bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    # labels
    bgTopLabel = Label(root, text="", bg='#dae8fc', font=bold_font, height=3, width=44, borderwidth=1, relief="solid")
    topLabelText = Label(root, text="Face Home", bg='#dae8fc', fg = "black", font=bold_font,justify=LEFT, height=2, width=10)
    boxLabel = Label(root, text="", bg='#dae8fc',font=bold_font, height=15, width=30)
    NameLabel = Label(root, text="", font=bold_font,justify=CENTER, height=1, width=10)
    NameEntry = Label(root, text="", font=bold_font,justify=CENTER, height=2, width=15)
    StartButton = Button(root, text='Start', bg='white', fg='black', font=bold_font, height=1, width=10)

    #place labels
    bgTopLabel.place(anchor=W, relheight=0.15, relwidth=0.686, relx=0.295, rely=0.1)
    topLabelText.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.31, rely=0.1)
    boxLabel.place(anchor=W, relheight=0.75, relwidth=0.46, relx=0.295, rely=0.6)
    NameLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.77, rely=0.26)
    NameEntry.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.77, rely=0.37)
    StartButton.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.92)

def enrollNew():
    #Button color change
    global homeButton, enrollNewButton, editDatabaseButton, settingsButton
    homeButton.configure(bg="white", fg='#4d3ce6')
    enrollNewButton.configure(bg="#2626ff", fg='white')
    editDatabaseButton.configure(bg="white", fg='#4d3ce6')
    settingsButton.configure(bg="white", fg='#4d3ce6')
    
    #font details
    bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    # labels
    bgTopLabel = Label(root, text="", bg='#dae8fc', font=bold_font, height=3, width=44, borderwidth=1, relief="solid")
    topLabelText = Label(root, text="Enroll New", bg='#dae8fc', fg = "black", font=bold_font,justify=LEFT, height=2, width=10)
    boxLabel = Label(root, text="", bg='#dae8fc',font=bold_font, height=15, width=30)
    NameLabel = Label(root, text="Name", font=bold_font,justify=CENTER, height=1, width=10)
    NameEntry = Entry(root, borderwidth=1, bg = "#dae8fc", fg= "black", font=bold_font, width=17)
    StartButton = Button(root, text='Start', bg='white', fg='black', font=bold_font, height=1, width=10)

    #place labels
    bgTopLabel.place(anchor=W, relheight=0.15, relwidth=0.686, relx=0.295, rely=0.1)
    topLabelText.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.31, rely=0.1)
    boxLabel.place(anchor=W, relheight=0.75, relwidth=0.46, relx=0.295, rely=0.6)
    NameLabel.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.26)
    NameEntry.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.37)
    StartButton.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.92)

def editDatabase():
    #Button color change
    global homeButton, enrollNewButton, editDatabaseButton, settingsButton
    homeButton.configure(bg="white", fg='#4d3ce6')
    enrollNewButton.configure(bg="white", fg='#4d3ce6')
    editDatabaseButton.configure(bg="#2626ff", fg='white')
    settingsButton.configure(bg="white", fg='#4d3ce6')
    
    #font details    
    bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    # labels
    bgTopLabel = Label(root, text="", bg='#dae8fc', font=bold_font, height=3, width=44, borderwidth=1, relief="solid")
    topLabelText = Label(root, text="Edit Database", bg='#dae8fc', fg = "black", font=bold_font,justify=LEFT, height=2, width=10)
    boxLabel = Label(root, text="", bg='#dae8fc',font=bold_font, height=15, width=30)
    NameLabel = Label(root, text="Name", font=bold_font,justify=CENTER, height=1, width=10)
    NameEntry = Entry(root, borderwidth=1, bg = "#dae8fc", fg= "black", font=bold_font, width=17)
    StartButton = Button(root, text='Start', bg='white', fg='black', font=bold_font, height=1, width=10)

    #place labels
    bgTopLabel.place(anchor=W, relheight=0.15, relwidth=0.686, relx=0.295, rely=0.1)
    topLabelText.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.31, rely=0.1)
    boxLabel.place(anchor=W, relheight=0.75, relwidth=0.46, relx=0.295, rely=0.6)
    NameLabel.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.26)
    NameEntry.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.37)
    StartButton.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.92)

def settings():
    #Button color change
    global homeButton, enrollNewButton, editDatabaseButton, settingsButton
    homeButton.configure(bg="white", fg='#4d3ce6')
    enrollNewButton.configure(bg="white", fg='#4d3ce6')
    editDatabaseButton.configure(bg="white", fg='#4d3ce6')
    settingsButton.configure(bg="#2626ff", fg='white')
    
    #font details

#BG labels
labelLeft = Label(root, text="", bg="#6963ff", height= 60, width=25)
image = Image.open('FacialRecognition/logo-main.png')
my_img = ImageTk.PhotoImage(image)
my_label = Label(image= my_img, bg='white', height=100, width=100)
my_label.place(anchor=CENTER, relx=0.14, rely=0.2)

# Button defination
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
global homeButton
homeButton = Button(root, text = "Home", bg = "white",font=bold_font, fg = "#4d3ce6",	
activebackground='#2626ff', activeforeground='white', justify ="center", height=1, width=16, command=home)
global enrollNewButton
enrollNewButton = Button(root, text="Enroll New", bg = "white",font=bold_font, fg = "#4d3ce6", activebackground='#2626ff', 	
activeforeground='white', justify ="center", height=1, width=16, command=enrollNew)
global editDatabaseButton
editDatabaseButton = Button(root, text = "Edit Database", bg = "white",font=bold_font, fg = "#4d3ce6", activebackground='#2626ff', activeforeground='white', justify ="center", height=1, width=16, command=editDatabase)
global settingsButton
settingsButton = Button(root, text = "Settings", bg = "white",font=bold_font, fg = "#4d3ce6", activebackground='#2626ff', activeforeground='white', justify ="center", height=1, width=16, command=settings)

# Put buttons on screen
labelLeft.place(anchor=W, relheight=1, relwidth=0.28, relx=0, rely=0.5)
homeButton.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.04, rely=0.45)
enrollNewButton.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.04, rely=0.58)
editDatabaseButton.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.04, rely=0.71)
settingsButton.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.04, rely=0.84)

root.mainloop()
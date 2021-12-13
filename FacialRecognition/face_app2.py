from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import matplotlib.pyplot as plt
import tkinter.font as tkfont
import cv2
from time import sleep
import random
import os
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import imutils
from threading import Thread
import csv_add_details
import face_training

root = Tk()
root.title('Face detection app')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='face-id.png'))
root.attributes("-fullscreen", True)
root.bind('<Escape>', lambda event: root.state('normal'))

#tab functions
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
    NameEntry.place(anchor=W, relheight=0.1, relwidth=0.25, relx=0.77, rely=0.37)
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
    normal_font = tkfont.Font(family="Helvetica", size=12, slant='italic')
    # labels
    bgTopLabel = Label(root, text="", bg='#dae8fc', font=bold_font, height=3, width=44, borderwidth=1, relief="solid")
    topLabelText = Label(root, text="Enroll New", bg='#dae8fc', fg = "black", font=bold_font,justify=LEFT, height=2, width=10)
    global boxLabel
    boxLabel = Label(root, text="", bg='#dae8fc',font=bold_font, height=15, width=30)
    NameLabel = Label(root, text="Name", font=bold_font,justify=CENTER, height=1, width=10)
    global NameEntry
    NameEntry = Entry(root, borderwidth=1, bg = "#dae8fc", fg= "black", font=bold_font, width=17)
    msgTitleLabel = Label(root, text="Message box",anchor=CENTER, font=bold_font, height=1, width=8)
    global msgLabel
    msgLabel = Label(root, text=' Enter name and click start', font=normal_font, anchor=NW, height=1, width=8, borderwidth=1, relief=SUNKEN)
    global StartButton
    StartButton = Button(root, text='Start', bg='white', fg='black', font=bold_font, height=1, width=10, command=getName)

    #place labels
    bgTopLabel.place(anchor=W, relheight=0.15, relwidth=0.686, relx=0.295, rely=0.1)
    topLabelText.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.31, rely=0.1)
    boxLabel.place(anchor=W, relheight=0.75, relwidth=0.46, relx=0.295, rely=0.6)
    NameLabel.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.26)
    NameEntry.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.37)
    msgTitleLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx= 0.77, rely=0.5)
    msgLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.77, rely=0.6)
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

#functions
def getName():
    global NameEntry
    global msgLabel
    global StartButton
    name = str(NameEntry.get())
    enrollNewStart(name)

def enrollNewStart(name):
    print(name)
    global id, homeButton, enrollNewButton, editDatabaseButton, settingsButton
    id = int(csv_add_details.create(name))
    msgLabel['text'] = "    Name got registered "
    StartButton['state'] = DISABLED
    homeButton['state'] = DISABLED
    enrollNewButton['state'] = DISABLED
    editDatabaseButton['state'] = DISABLED
    settingsButton['state'] = DISABLED
    sleep(1)
    makeDataset()

def makeDataset():
    print("preparing dataset")
    messagebox.showinfo("Attention", "Initializing face capture. Look at the camera and wait ...")
    msgLabel['text'] = "    Preparing dataset"
    global id
    dataset(id, 1, 0)
    messagebox.showinfo("Attention","Now turn your head 30 degrees left")
    dataset(id, 2, 10)
    messagebox.showinfo("Attention","Now turn your head 30 degrees right")
    dataset(id, 3, 20)
    face_training.trainStart()
    msgLabel['text'] = "Your face details got saved\nand trained "
    StartButton['state'] = NORMAL
    homeButton['state'] = NORMAL
    enrollNewButton['state'] = NORMAL
    editDatabaseButton['state'] = NORMAL
    settingsButton['state'] = NORMAL

def dataset(face_id, part, count):
    global boxLabel
    vs = WebcamVideoStream(src=0).start()
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while(True):

        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        frame1 = imutils.resize(frame, width = 700)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Get the latest frame and convert into Image
        cv2image= cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        dis_img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = dis_img)
        boxLabel.imgtk = imgtk
        boxLabel.configure(image=imgtk)

        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces: 

            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)     
            # Save the captured image into the datasets folder
            count += 1
            print(count)
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        if count == 10 and part == 1: # Take 10 face sample and stop video
            break
        elif count == 20 and part == 2:
            break
        elif count >= 30:
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cv2.destroyAllWindows()
    vs.stop()

#BG labels
labelLeft = Label(root, text="", bg="#6963ff", height= 60, width=25)
image = Image.open('logo-main.png')
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
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

def newFace():
    newWindow = Toplevel(root)
    newWindow.title("New Face")
    newWindow.geometry("200x250")
    bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    slim_font = tkfont.Font(family="Helvetica", size=13)

    label = Label(newWindow, text="New Face", fg= "red", font=bold_font, justify ="center")
    nameLabel = Label(newWindow, text="Name" ,font=slim_font, fg="red")
    global name1
    name1 = Entry(newWindow, bg="#C2C2CF", width=10, borderwidth=2)
    startButton = Button(newWindow, text='Start', font=bold_font, fg="white", bg="#006aff",justify='center', height=1, width=10, command=getName)
    global trainButton
    trainButton = Button(newWindow, text='Train', font=bold_font, fg="white", bg="#006aff",justify='center', height=1, width=10,state=DISABLED, command=lambda: [makeDataset(), newWindow.destroy()])

    label.place(x=60, y=20)
    nameLabel.place(x=20, y=80)
    name1.place(x=90, y=80, height=28, width=85)
    startButton.place(x=45, y=160)
    trainButton.place(x=45, y = 200)

def getName():
    global name1
    name = str(name1.get())
    newStart(name)
    global trainButton
    trainButton['state'] = NORMAL
    messagebox.showinfo("Information","Name got registered, now click train")

def newStart(name):
    print(name)
    global id
    id = int(csv_add_details.create(name))

def makeDataset():
    print("preparing dataset")
    messagebox.showinfo("Attention", "Initializing face capture. Look at the camera and wait ...")
    global id
    dataset(id, 1, 0)
    messagebox.showinfo("Attention","Now turn your head 30 degrees left")
    dataset(id, 2, 10)
    messagebox.showinfo("Attention","Now turn your head 30 degrees right")
    dataset(id, 3, 20)
    face_training.trainStart()

def dataset(face_id, part, count):
    vs = WebcamVideoStream(src=0).start()
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while(True):

        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces: 

            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)     
            # Save the captured image into the datasets folder
            count += 1
            print(count)
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('camera', frame)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count == 10 and part == 1: # Take 10 face sample and stop video
            break
        elif count == 20 and part == 2:
            break
        elif count >= 30:
            break

def update():
    newWindow = Toplevel(root)
    newWindow.title("Update")
    newWindow.geometry("200x250")
    bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
    slim_font = tkfont.Font(family="Helvetica", size=13)

    label = Label(newWindow, text="Update", fg= "red", font=bold_font, justify ="center")
    idLabel = Label(newWindow, text="ID",font=slim_font, fg="red")
    idE = Entry(newWindow, bg="#C2C2CF", width=10, borderwidth=2)
    idButton = Button(newWindow, text='Update', font=bold_font, fg="white", bg="#006aff",justify='center', height=1, width=10, command=newWindow.destroy)

    label.place(x=70, y=20)
    idLabel.place(x=35, y=80)
    idE.place(x=90, y=80, height=28, width=80)
    idButton.place(x=45, y=160)

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cv2.destroyAllWindows()
    vs.stop()

# Button defination
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
root.geometry("200x250")
label = Label(root, text = 'Face Enrollment', fg= "red", font=bold_font, justify ="left")
button1 = Button(root, text = "Enroll New", bg = "#006aff",font=bold_font, fg = "white", justify ="center", height=1, width=10, command=newFace)
button2 = Button(root, text="Update", bg = "#006aff",font=bold_font, fg = "white", justify ="center", height=1, width=10, command=update)

# Put buttons on screen
label.place(x=36, y=20)
button1.place(x=45, y=100)
button2.place(x=45, y=160)

root.mainloop()

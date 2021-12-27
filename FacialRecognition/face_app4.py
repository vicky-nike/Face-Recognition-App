from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter.font as tkfont
import cv2
from time import sleep
import os
from imutils.video import WebcamVideoStream
import imutils
import pandas as pd
import csv_add_details
import face_training
import dbus

sess_bus = dbus.SessionBus()
root = Tk()
root.title('Face detection app')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='face-id.png'))

root.attributes("-fullscreen", True)
#root.attributes("-zoomed", True)
#root.geometry("700x400")
#root.bind('<Escape>', lambda event: root.state('normal'))

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
    normal_font = tkfont.Font(family="Helvetica", size=12, slant='italic')
    # labels
    bgTopLabel = Label(root, text="", bg='#dae8fc', font=bold_font, height=3, width=44, borderwidth=1, relief="solid")
    topLabelText = Label(root, text="Face Home", bg='#dae8fc', fg = "black", font=bold_font,justify=LEFT, height=2, width=10)
    global boxLabelHome
    boxLabelHome = Label(root, text="", bg='#dae8fc',font=bold_font, height=15, width=30)
    NameLabel = Label(root, text="", font=bold_font,justify=CENTER, height=1, width=10)
    NameEntry = Label(root, text="", font=bold_font,justify=CENTER, height=2, width=15)
    EnterButton = Label(root, text='', font=bold_font,justify=CENTER, height=2, width=15)
    msgTitleLabel = Label(root, text="Message box",anchor=CENTER, font=bold_font, height=1, width=8)
    global msgLabelHome
    msgLabelHome = Label(root, text=' Click start to begin\nrecognition', font=normal_font, anchor=NW, height=1, width=8, borderwidth=1, relief=SUNKEN)
    StartButton = Button(root, text='Start', bg='white', fg='black', font=bold_font, height=1, width=10, command=recognition)
    
    #place labels
    bgTopLabel.place(anchor=W, relheight=0.15, relwidth=0.686, relx=0.295, rely=0.1)
    topLabelText.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.31, rely=0.1)
    boxLabelHome.place(anchor=W, relheight=0.75, relwidth=0.46, relx=0.295, rely=0.6)
    NameLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.77, rely=0.26)
    NameEntry.place(anchor=W, relheight=0.1, relwidth=0.25, relx=0.77, rely=0.37)
    EnterButton.place(anchor = W, relheight=0.06, relwidth=0.215, relx=0.77, rely=0.45)
    StartButton.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.92)
    msgTitleLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx= 0.77, rely=0.6)
    msgLabelHome.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.77, rely=0.7)

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
    NameEntry.bind('<FocusIn>', keyboardShow)
    EnterButton = Button(root, text='Enter', bg='white', fg='black', font=bold_font, height=1, width=10, command=lambda: [rootFocus(), keyboardHide()])
    msgTitleLabel = Label(root, text="Message box",anchor=CENTER, font=bold_font, height=1, width=8)
    global msgLabelNew
    msgLabelNew = Label(root, text=' Enter name and click start', font=normal_font, anchor=NW, height=1, width=8, borderwidth=1, relief=SUNKEN)
    global StartButton
    StartButton = Button(root, text='Start', bg='white', fg='black', font=bold_font, height=1, width=10, command=getName)

    #place labels
    bgTopLabel.place(anchor=W, relheight=0.15, relwidth=0.686, relx=0.295, rely=0.1)
    topLabelText.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.31, rely=0.1)
    boxLabel.place(anchor=W, relheight=0.75, relwidth=0.46, relx=0.295, rely=0.6)
    NameLabel.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.26)
    NameEntry.place(anchor=W, relheight=0.06, relwidth=0.215, relx=0.77, rely=0.37)
    EnterButton.place(anchor = W, relheight=0.06, relwidth=0.215, relx=0.77, rely=0.45)
    msgTitleLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx= 0.77, rely=0.6)
    msgLabelNew.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.77, rely=0.7)
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
    NameEntry.bind('<FocusIn>', keyboardShow)
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
    global id, homeButton, enrollNewButton, editDatabaseButton, settingsButton, msgLabelNew
    id = int(csv_add_details.create(name))
    msgLabelNew['text'] = "    Name got registered "
    StartButton['state'] = DISABLED
    homeButton['state'] = DISABLED
    enrollNewButton['state'] = DISABLED
    editDatabaseButton['state'] = DISABLED
    settingsButton['state'] = DISABLED
    sleep(1)
    makeDataset()

def makeDataset():
    global msgLabelNew
    print("preparing dataset")
    messagebox.showinfo("Attention", "Initializing face capture. Look at the camera and wait ...")
    msgLabelNew['text'] = "  Preparing dataset"
    global id
    vs = WebcamVideoStream(src=0).start()
    #cam = cv2.VideoCapture(0)
    #cam.set(3, 640) # set video widht
    #cam.set(4, 480) # set video height
    #face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    count = 0

    def dataset(face_id, count):
        global boxLabel
        global msgLabelNew

        #frame= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
        frame= cv2.cvtColor(vs.read(),cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, -1)
        img1 = Image.fromarray(frame)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img1)
        boxLabel.imgtk = imgtk
        boxLabel.configure(image=imgtk)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        #sleep(0.5)

        for (x,y,w,h) in faces: 

            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)     
            # Save the captured image into the datasets folder
            msgLabelNew['text'] = count+1
            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        
        if count == 10: # Take 10 face sample and stop video
            messagebox.showinfo("Attention","Now turn your head 30 degrees left")
            count += 1
            boxLabel.after(20, lambda: dataset(face_id, count))
        elif count == 20:
            messagebox.showinfo("Attention","Now turn your head 30 degrees right")
            count += 1
            boxLabel.after(20, lambda: dataset(face_id, count))
        elif count >= 30:
            #msgLabelNew['text'] = "Preparing dataset completed"
            face_training.trainStart()
            msgLabelNew['text'] = "Your face details got saved\nand trained "
            StartButton['state'] = NORMAL
            homeButton['state'] = NORMAL
            enrollNewButton['state'] = NORMAL
            editDatabaseButton['state'] = NORMAL
            settingsButton['state'] = NORMAL
            return
        else:
            boxLabel.after(20, lambda: dataset(face_id, count))
    
    dataset(id, count)

def recognition():
    global msgLabelHome
    global boxLabelHome
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX
    #iniciate id counter
    count=1
    # names related to ids: example ==> Marcelo: id=1,  etc
    data = pd.read_csv("records.csv")
    names = data['Name'].tolist()

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    img= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
    img = cv2.flip(img, -1)
    img1 = Image.fromarray(img)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img1)
    boxLabelHome.imgtk = imgtk
    boxLabelHome.configure(image=imgtk)
    #img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )
    conf = 0
    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        conf = round(100 - confidence)
        print("id", id, " conf", conf)
        found = str(names[id])
        if(conf>20):
            msgLabelHome['text'] = "Recognised as " + found
            break

    
    #cv2.imshow('camera',img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if(conf>20):
        return
    if(count==1):
        boxLabelHome.after(20, recognition)

def keyboardShow(event):
    kbd.Show()

def keyboardHide():
    kbd.Hide()

def rootFocus():
    root.focus()

#Start ONboard
kbd = sess_bus.get_object('org.onboard.Onboard', '/org/onboard/Onboard/Keyboard')
#root.attributes("-fullscreen", True)
#root.bind_class("Entry", "<1>", lambda ev: ev.widget.focus_force())

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
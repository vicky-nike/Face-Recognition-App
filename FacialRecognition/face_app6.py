from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter.font as tkfont
import cv2
from time import sleep
import os
import pandas as pd
import csv_add_details
import face_training
import recognised_record
from tkinter import ttk

root = Tk()
root.title('Face detection app')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='face-id.png'))
root.attributes("-fullscreen", True)
root.attributes('-topmost', False)
#root.attributes("-zoomed", True)
key = None

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
    global boxLabel, NameEntry, msgLabel, StartButton
    bgTopLabel = Label(root, text="", bg='#dae8fc', font=bold_font, height=3, width=44, borderwidth=1, relief="solid")
    topLabelText = Label(root, text="Enroll New", bg='#dae8fc', fg = "black", font=bold_font,justify=LEFT, height=2, width=10)
    boxLabel = Label(root, text="", bg='#dae8fc',font=bold_font, height=15, width=30)
    NameLabel = Label(root, text="Name", font=bold_font,justify=CENTER, height=1, width=10)
    NameEntry = Entry(root, borderwidth=1, bg = "#dae8fc", fg= "black", font=bold_font, width=17)
    NameEntry.bind('<Button-1>', check_keyboard)
    EnterButton = Button(root, text='Enter', bg='white', fg='black', font=bold_font, height=1, width=10, command=lambda: [rootFocus(), key.destroy()])
    msgTitleLabel = Label(root, text="Message box",anchor=CENTER, font=bold_font, height=1, width=8)
    msgLabel = Label(root, text=' Enter name and click start', font=normal_font, anchor=NW, height=1, width=8, borderwidth=1, relief=SUNKEN)
    StartButton = Button(root, text='Start', bg='white', fg='black', font=bold_font, height=1, width=10, command=getName)

    #place labels
    bgTopLabel.place(anchor=W, relheight=0.15, relwidth=0.686, relx=0.295, rely=0.1)
    topLabelText.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.31, rely=0.1)
    boxLabel.place(anchor=W, relheight=0.75, relwidth=0.46, relx=0.295, rely=0.6)
    NameLabel.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.26)
    NameEntry.place(anchor=W, relheight=0.06, relwidth=0.215, relx=0.77, rely=0.37)
    EnterButton.place(anchor = W, relheight=0.06, relwidth=0.215, relx=0.77, rely=0.45)
    msgTitleLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx= 0.77, rely=0.6)
    msgLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.77, rely=0.7)
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
    normal_font = tkfont.Font(family="Helvetica", size=12, slant='italic')
    # labels
    global boxLabel, NameEntry, msgLabel, StartButton
    bgTopLabel = Label(root, text="", bg='#dae8fc', font=bold_font, height=3, width=44, borderwidth=1, relief="solid")
    topLabelText = Label(root, text="Enroll New", bg='#dae8fc', fg = "black", font=bold_font,justify=LEFT, height=2, width=10)
    boxLabel = Label(root, text="", bg='#dae8fc',font=bold_font, height=15, width=30)
    NameLabel = Label(root, text="Name", font=bold_font,justify=CENTER, height=1, width=10)
    NameEntry = Entry(root, borderwidth=1, bg = "#dae8fc", fg= "black", font=bold_font, width=17)
    NameEntry.bind('<Button-1>', check_keyboard)
    EnterButton = Button(root, text='Enter', bg='white', fg='black', font=bold_font, height=1, width=10, command=lambda: [rootFocus(), key.destroy()])
    msgTitleLabel = Label(root, text="Message box",anchor=CENTER, font=bold_font, height=1, width=8)
    msgLabel = Label(root, text=' Enter name and click start', font=normal_font, anchor=NW, height=1, width=8, borderwidth=1, relief=SUNKEN)
    StartButton = Button(root, text='Start', bg='white', fg='black', font=bold_font, height=1, width=10, command=edit_getName)

    #place labels
    bgTopLabel.place(anchor=W, relheight=0.15, relwidth=0.686, relx=0.295, rely=0.1)
    topLabelText.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.31, rely=0.1)
    boxLabel.place(anchor=W, relheight=0.75, relwidth=0.46, relx=0.295, rely=0.6)
    NameLabel.place(anchor=W, relheight=0.1, relwidth=0.215, relx=0.77, rely=0.26)
    NameEntry.place(anchor=W, relheight=0.06, relwidth=0.215, relx=0.77, rely=0.37)
    EnterButton.place(anchor = W, relheight=0.06, relwidth=0.215, relx=0.77, rely=0.45)
    msgTitleLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx= 0.77, rely=0.6)
    msgLabel.place(anchor=W, relheight=0.1, relwidth=0.2, relx=0.77, rely=0.7)
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
    global NameEntry, msgLabel, StartButton
    name = str(NameEntry.get())
    data = pd.read_csv('records.csv', header=0)
    col_name = list(data.Name)
    for i in range(0, len(col_name)):
        if name == col_name[i]:
            found = 1
            break
        else:
            found = 0
    
    if found == 1:
        messagebox.showinfo("Attention", "Name already exist, give another user name")
    else:
        enrollNewStart(name)

def edit_getName():
    global NameEntry, msgLabel, StartButton, editId, boxLabel
    name = str(NameEntry.get())
    data = pd.read_csv('records.csv', header=0)
    col_name = list(data.Name)
    found = 0
    for i in range(0, len(col_name)):
        if name == col_name[i]:
            found = 1
            editId = i
            break
        else:
            found = 0
    if found == 1:
        boxLabel['text'] = " "
        messagebox.showinfo("Attention", "User name " + str(col_name[editId]) + " found, the id number is " + str(editId))
        makeDataset(1)
    else:
        msgLabel['text'] = ' Enter name and click start'
        messagebox.showinfo("Attention", "User name " + str(name) + " not found, try again or enroll new.")

def enrollNewStart(name):
    name = name.lower()
    global newId, homeButton, enrollNewButton, editDatabaseButton, settingsButton, msgLabel
    newId = int(csv_add_details.create(name))
    msgLabel['text'] = "    Name got registered "
    StartButton['state'] = DISABLED
    homeButton['state'] = DISABLED
    enrollNewButton['state'] = DISABLED
    editDatabaseButton['state'] = DISABLED
    settingsButton['state'] = DISABLED
    sleep(1)
    makeDataset(0)

def makeDataset(type):
    global msgLabel, boxLabel
    if(type==0):
        print("preparing dataset")
        messagebox.showinfo("Attention", "Initializing face capture. Look at the camera and wait ...")
        msgLabel['text'] = "  Preparing dataset"
        global newId
        id = newId
    else:
        print("updating dataset")
        messagebox.showinfo("Attention", "Initializing face capture. Look at the camera and wait ...")
        msgLabel['text'] = "  Updating dataset"
        global editId
        id = editId

    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    count = 0

    def makeDataset_display(face_id, count):
        global msgLabel
        
        if not os.path.exists('dataset'):
            os.makedirs('dataset')

        frame= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
        #frame = cv2.flip(frame, -1)
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
            msgLabel['text'] = count+1
            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        
        if count == 10: # Take 10 face sample and stop video
            messagebox.showinfo("Attention","Now turn your head 30 degrees left")
            count += 1
            boxLabel.after(20, lambda: makeDataset_display(face_id, count))
        elif count == 20:
            messagebox.showinfo("Attention","Now turn your head 30 degrees right")
            count += 1
            boxLabel.after(20, lambda: makeDataset_display(face_id, count))
        elif count >= 30:
            cam.release()
            cv2.destroyAllWindows()
            msgLabel['text'] = "Preparing dataset completed"
            face_training.trainStart()
            msgLabel['text'] = "Your face details got saved\nand trained "
            StartButton['state'] = NORMAL
            homeButton['state'] = NORMAL
            enrollNewButton['state'] = NORMAL
            editDatabaseButton['state'] = NORMAL
            settingsButton['state'] = NORMAL
            return
        else:
            boxLabel.after(20, lambda: makeDataset_display(face_id, count))
    
    makeDataset_display(id, count)

def recognition():
    global msgLabelHome
    global boxLabelHome
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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

    def recognition_display():
        msgLabelHome['text'] = " Recognition started "
        img= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
        #img = cv2.flip(img, -1)
        img1 = Image.fromarray(img)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img1)
        boxLabelHome.imgtk = imgtk
        boxLabelHome.configure(image=imgtk)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (64, 48),
        )
        conf = 0
        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            print("confidence: ", confidence)
            conf = round(100 - confidence)
            print("id", id, " conf", conf)
            found = str(names[id])
            if(conf>20):
                msgLabelHome['text'] = "Recognised as " + found
                recognised_record.got(found)
                break
        
        #cv2.imshow('camera',img)
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if(conf>20):
            cam.release()
            cv2.destroyAllWindows()
            return
        if(count==1):
            boxLabelHome.after(20, recognition_display)

    if(len(names) <= 1):
        messagebox.showinfo("Attention", "Please add entry to start recognition.")
    else:
        recognition_display()

def check_keyboard(event):
    if key is None:
        display_keyboard()
    try:
        key.destroy()
        display_keyboard()
    except TclError:
        display_keyboard()

def display_keyboard():
    global key
    key = Toplevel(root)
    key.title('On Screen Keyboard')
     # get screen height and width
    positionRight = int(root.winfo_screenwidth()/2 - 600/2)
    positionDown = int(root.winfo_screenheight()/2 - 200/2)
    
    key.geometry("{}x{}+{}+{}".format(600, 200, positionRight, (positionDown+150)))
    style = ttk.Style()
    key.configure(bg='gray27')
    style.configure('TButton', background='gray21')
    style.configure('TButton', foreground='white')
    style.map('TButton', foreground=[('active', 'black')])

    global theme
    theme = "light"
    global is_shift
    is_shift = False

    def press(num):
        global NameEntry
        current = NameEntry.get()
        NameEntry.delete(0, END)
        NameEntry.insert(0, str(current) + str(num))

    def Backspace():
        global NameEntry
        current = NameEntry.get()
        NameEntry.delete(len(current)-1)

    def Shift():
        global is_shift
        is_shift = not is_shift
        keyboard_display()

    def Clear():
        global NameEntry
        NameEntry.delete(0, END)

    def Theme():
        global theme
        if theme == "dark":
            key.configure(bg='gray27')
            style.configure('TButton', background='gray21')
            style.configure('TButton', foreground='white')
            style.map('TButton', foreground=[('active', 'black')])
            theme = "light"
        elif theme == "light":
            key.configure(bg='gray99')
            style.configure('TButton', background='azure')
            style.configure('TButton', foreground='black', cursor='man')
            style.map('TButton', foreground=[('active', 'white')], background=[('active', 'grey')])
            theme = "dark"
    
    def keyboard_display():
        if (is_shift):
            # Adding keys line wise
            # First Line Button
            tilda = ttk.Button(key, text='~', command=lambda: press('~'))
            tilda.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.005, rely=0.11)

            num1 = ttk.Button(key, text='!', command=lambda: press('!'))
            num1.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.07, rely=0.11)
            
            num2 = ttk.Button(key, text='@', command=lambda: press('@'))
            num2.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.135, rely=0.11)

            num3 = ttk.Button(key, text='#', command=lambda: press('#'))
            num3.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.2, rely=0.11)

            num4 = ttk.Button(key, text='$', command=lambda: press('$'))
            num4.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.265, rely=0.11)

            num5 = ttk.Button(key, text='%', command=lambda: press('%'))
            num5.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.33, rely=0.11)

            num6 = ttk.Button(key, text='^', command=lambda: press('^'))
            num6.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.395, rely=0.11)

            num7 = ttk.Button(key, text='&', command=lambda: press('&'))
            num7.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.46, rely=0.11)

            num8 = ttk.Button(key, text='*', command=lambda: press('*'))
            num8.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.525, rely=0.11)

            num9 = ttk.Button(key, text='(', command=lambda: press('('))
            num9.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.59, rely=0.11)

            num0 = ttk.Button(key, text=')', command=lambda: press(')'))
            num0.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.655, rely=0.11)

            under = ttk.Button(key, text='_', command=lambda: press('_'))
            under.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.72, rely=0.11)

            equal = ttk.Button(key, text='=', command=lambda: press('='))
            equal.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.785, rely=0.11)

            backspace = ttk.Button(key, text='Backspace', command=Backspace)
            backspace.place(anchor='w', relheight=0.175, relwidth=0.141, relx=0.85, rely=0.11)

            # Second Line Buttons #########################################################

            tab_button = ttk.Button(key, text='Tab', command=lambda: press('\t'))
            tab_button.place(anchor='w', relheight=0.175, relwidth=0.09, relx=0.005, rely=0.305)

            Q = ttk.Button(key, text='Q', command=lambda: press('Q'))
            Q.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.1, rely=0.305)

            W = ttk.Button(key, text='W', command=lambda: press('W'))
            W.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.165, rely=0.305)

            E = ttk.Button(key, text='E', command=lambda: press('E'))
            E.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.23, rely=0.305)

            R = ttk.Button(key, text='R', command=lambda: press('R'))
            R.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.295, rely=0.305)

            T = ttk.Button(key, text='T', command=lambda: press('T'))
            T.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.36, rely=0.305)

            Y = ttk.Button(key, text='Y', command=lambda: press('Y'))
            Y.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.425, rely=0.305)

            U = ttk.Button(key, text='U', command=lambda: press('U'))
            U.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.49, rely=0.305)

            I = ttk.Button(key, text='I', command=lambda: press('I'))
            I.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.555, rely=0.305)

            O = ttk.Button(key, text='O', command=lambda: press('O'))
            O.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.62, rely=0.305)

            P = ttk.Button(key, text='P', command=lambda: press('P'))
            P.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.685, rely=0.305)

            curly_l = ttk.Button(key, text='{', command=lambda: press('{'))
            curly_l.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.75, rely=0.305)

            curly_r = ttk.Button(key, text='}', command=lambda: press('}'))
            curly_r.place(anchor='w', relheight=0.175, relwidth=0.11, relx=0.88, rely=0.305)

            # Third Line Buttons ##########################################################

            caps = ttk.Button(key, text='Caps', command=Shift)
            caps.place(anchor='w', relheight=0.175, relwidth=0.12, relx=0.005, rely=0.50)
            
            A = ttk.Button(key, text='A', command=lambda: press('A'))
            A.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.13, rely=0.50)

            S = ttk.Button(key, text='S', command=lambda: press('S'))
            S.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.195, rely=0.50)

            D = ttk.Button(key, text='D', command=lambda: press('D'))
            D.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.26, rely=0.50)

            F = ttk.Button(key, text='F', command=lambda: press('F'))
            F.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.325, rely=0.50)

            G = ttk.Button(key, text='G', command=lambda: press('G'))
            G.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.39, rely=0.50)

            H = ttk.Button(key, text='H', command=lambda: press('H'))
            H.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.455, rely=0.50)

            J = ttk.Button(key, text='J', command=lambda: press('J'))
            J.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.52, rely=0.50)

            K = ttk.Button(key, text='K', command=lambda: press('K'))
            K.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.585, rely=0.50)

            L = ttk.Button(key, text='L', command=lambda: press('L'))
            L.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.65, rely=0.50)

            colon = ttk.Button(key, text=':', command=lambda: press(':'))
            colon.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.715, rely=0.50)

            quotation = ttk.Button(key, text='"', command=lambda: press('"'))
            quotation.place(anchor='w', relheight=0.175, relwidth=0.095, relx=0.78, rely=0.50)

            enter = ttk.Button(key, text='Enter', command=lambda: key.destroy())
            enter.place(anchor='w', relheight=0.558, relwidth=0.112, relx=0.88, rely=0.695)

            # Fourth line Buttons #########################################################

            shift = ttk.Button(key, text='Shift', command=Shift)
            shift.place(anchor='w', relheight=0.175, relwidth=0.15, relx=0.005, rely=0.695)

            Z = ttk.Button(key, text='Z', command=lambda: press('Z'))
            Z.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.16, rely=0.695)

            X = ttk.Button(key, text='X', command=lambda: press('X'))
            X.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.225, rely=0.695)

            C = ttk.Button(key, text='C', command=lambda: press('C'))
            C.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.29, rely=0.695)

            V = ttk.Button(key, text='V', command=lambda: press('V'))
            V.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.355, rely=0.695)

            B = ttk.Button(key, text='B', command=lambda: press('B'))
            B.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.42, rely=0.695)

            N = ttk.Button(key, text='N', command=lambda: press('N'))
            N.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.485, rely=0.695)

            M = ttk.Button(key, text='M', command=lambda: press('M'))
            M.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.55, rely=0.695)

            ang_l = ttk.Button(key, text='<', command=lambda: press('<'))
            ang_l.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.615, rely=0.695)

            ang_r = ttk.Button(key, text='>', command=lambda: press('>'))
            ang_r.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.68, rely=0.695)

            question = ttk.Button(key, text='?', command=lambda: press('?'))
            question.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.745, rely=0.695)

            plus = ttk.Button(key, text='+', command=lambda: press('+'))
            plus.place(anchor='w', relheight=0.175, relwidth=0.065, relx=0.81, rely=0.695)

            # Fifth Line Buttons ##########################################################

            close = ttk.Button(key, text='Close', command= key.destroy)
            close.place(anchor='w', relheight=0.175, relwidth=0.09, relx=0.005, rely=0.89)
            
            theme = ttk.Button(key, text='Theme', command=Theme)
            theme.place(anchor='w', relheight=0.175, relwidth=0.1, relx=0.1, rely=0.89)
            
            space = ttk.Button(key, text='Space', command=lambda: press(' '))
            space.place(anchor='w', relheight=0.175, relwidth=0.515, relx=0.205, rely=0.89)

            clear = ttk.Button(key, text='Clear', command=Clear)
            clear.place(anchor='w', relheight=0.175, relwidth=0.15, relx=0.725, rely=0.89)
            
        else:
            # Adding keys line wise
            # First Line Button
            tick = ttk.Button(key, text='`', command=lambda: press('`'))
            tick.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.005, rely=0.11)

            num1 = ttk.Button(key, text='1', command=lambda: press('1'))
            num1.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.07, rely=0.11)

            num2 = ttk.Button(key, text='2', command=lambda: press('2'))
            num2.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.135, rely=0.11)

            num3 = ttk.Button(key, text='3', command=lambda: press('3'))
            num3.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.2, rely=0.11)
            
            num4 = ttk.Button(key, text='4', command=lambda: press('4'))
            num4.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.265, rely=0.11)

            num5 = ttk.Button(key, text='5', command=lambda: press('5'))
            num5.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.33, rely=0.11)

            num6 = ttk.Button(key, text='6', command=lambda: press('6'))
            num6.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.395, rely=0.11)

            num7 = ttk.Button(key, text='7', command=lambda: press('7'))
            num7.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.46, rely=0.11)

            num8 = ttk.Button(key, text='8', command=lambda: press('8'))
            num8.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.525, rely=0.11)

            num9 = ttk.Button(key, text='9', command=lambda: press('9'))
            num9.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.59, rely=0.11)

            num0 = ttk.Button(key, text='0', command=lambda: press('0'))
            num0.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.655, rely=0.11)
            
            minus = ttk.Button(key, text='-', command=lambda: press('-'))
            minus.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.72, rely=0.11)

            equal = ttk.Button(key, text='=', command=lambda: press('='))
            equal.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.785, rely=0.11)

            backspace = ttk.Button(key, text='Backspace', command=Backspace)
            backspace.place(anchor='w', relheight=0.175, relwidth=0.141, relx=0.85, rely=0.11)
            
            # Second Line Buttons ##########################################################

            tab_button = ttk.Button(key, text='Tab', command=lambda: press('\t'))
            tab_button.place(anchor='w', relheight=0.175, relwidth=0.09, relx=0.005, rely=0.305)

            Q = ttk.Button(key, text='q', command=lambda: press('q'))
            Q.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.1, rely=0.305)
            
            W = ttk.Button(key, text='w', command=lambda: press('w'))
            W.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.165, rely=0.305)

            E = ttk.Button(key, text='e', command=lambda: press('e'))
            E.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.23, rely=0.305)

            R = ttk.Button(key, text='r', command=lambda: press('r'))
            R.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.295, rely=0.305)

            T = ttk.Button(key, text='t', command=lambda: press('t'))
            T.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.36, rely=0.305)

            Y = ttk.Button(key, text='y', command=lambda: press('y'))
            Y.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.425, rely=0.305)

            U = ttk.Button(key, text='u', command=lambda: press('u'))
            U.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.49, rely=0.305)

            I = ttk.Button(key, text='i', command=lambda: press('i'))
            I.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.555, rely=0.305)

            O = ttk.Button(key, text='o', command=lambda: press('o'))
            O.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.62, rely=0.305)

            P = ttk.Button(key, text='p', command=lambda: press('p'))
            P.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.685, rely=0.305)
            
            sq_l = ttk.Button(key, text='[', command=lambda: press('['))
            sq_l.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.75, rely=0.305)

            sq_r = ttk.Button(key, text=']', command=lambda: press(']'))
            sq_r.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.815, rely=0.305)

            back_slash = ttk.Button(key, text='\\', command=lambda: press('\\'))
            back_slash.place(anchor='w', relheight=0.175, relwidth=0.11, relx=0.88, rely=0.305)
            
            # Third Line Buttons ###########################################################
            
            caps = ttk.Button(key, text='Caps', command=Shift)
            caps.place(anchor='w', relheight=0.175, relwidth=0.12, relx=0.005, rely=0.50)
            
            A = ttk.Button(key, text='a', command=lambda: press('a'))
            A.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.13, rely=0.50)
            
            S = ttk.Button(key, text='s', command=lambda: press('s'))
            S.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.195, rely=0.50)

            D = ttk.Button(key, text='d', command=lambda: press('d'))
            D.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.26, rely=0.50)

            F = ttk.Button(key, text='f', command=lambda: press('f'))
            F.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.325, rely=0.50)

            G = ttk.Button(key, text='g', command=lambda: press('g'))
            G.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.39, rely=0.50)

            H = ttk.Button(key, text='h', command=lambda: press('h'))
            H.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.455, rely=0.50)

            J = ttk.Button(key, text='j', command=lambda: press('j'))
            J.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.52, rely=0.50)

            K = ttk.Button(key, text='k', command=lambda: press('k'))
            K.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.585, rely=0.50)

            L = ttk.Button(key, text='l', command=lambda: press('l'))
            L.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.65, rely=0.50)
            
            semi_co = ttk.Button(key, text=';', command=lambda: press(';'))
            semi_co.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.715, rely=0.50)

            quotation = ttk.Button(key, text="'", command=lambda: press('"'))
            quotation.place(anchor='w', relheight=0.175, relwidth=0.095, relx=0.78, rely=0.50)

            enter = ttk.Button(key, text='Enter', command=lambda: key.destroy())
            enter.place(anchor='w', relheight=0.558, relwidth=0.112, relx=0.88, rely=0.695)
            
            # Fourth line Buttons ######################################################

            shift = ttk.Button(key, text='Shift', width=6, command=Shift)
            shift.place(anchor='w', relheight=0.175, relwidth=0.15, relx=0.005, rely=0.695)
            
            Z = ttk.Button(key, text='z', command=lambda: press('z'))
            Z.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.16, rely=0.695)
            
            X = ttk.Button(key, text='x', command=lambda: press('x'))
            X.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.225, rely=0.695)

            C = ttk.Button(key, text='c', command=lambda: press('c'))
            C.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.29, rely=0.695)

            V = ttk.Button(key, text='v', command=lambda: press('v'))
            V.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.355, rely=0.695)

            B = ttk.Button(key, text='b', command=lambda: press('b'))
            B.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.42, rely=0.695)

            N = ttk.Button(key, text='n', command=lambda: press('n'))
            N.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.485, rely=0.695)

            M = ttk.Button(key, text='m', command=lambda: press('m'))
            M.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.55, rely=0.695)

            comma = ttk.Button(key, text=',', command=lambda: press(','))
            comma.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.615, rely=0.695)

            dot = ttk.Button(key, text='.', command=lambda: press('.'))
            dot.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.68, rely=0.695)

            slash = ttk.Button(key, text='/', command=lambda: press('/'))
            slash.place(anchor='w', relheight=0.175, relwidth=0.06, relx=0.745, rely=0.695)

            plus = ttk.Button(key, text='+', command=lambda: press('+'))
            plus.place(anchor='w', relheight=0.175, relwidth=0.065, relx=0.81, rely=0.695)


            # Fifth Line Buttons ###########################################################

            close = ttk.Button(key, text='Close', command=key.destroy)
            close.place(anchor='w', relheight=0.17, relwidth=0.09, relx=0.005, rely=0.89)
            
            theme = ttk.Button(key, text='Theme', command=Theme)
            theme.place(anchor='w', relheight=0.17, relwidth=0.1, relx=0.1, rely=0.89)
            
            space = ttk.Button(key, text='Space', command=lambda: press(' '))
            space.place(anchor='w', relheight=0.17, relwidth=0.515, relx=0.205, rely=0.89)

            clear = ttk.Button(key, text='Clear', command=Clear)
            clear.place(anchor='w', relheight=0.17, relwidth=0.15, relx=0.725, rely=0.89)
    
    keyboard_display()

def rootFocus():
    root.focus()

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
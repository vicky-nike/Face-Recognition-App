import cv2
import os

def edit_database():
        global msgLabelNew
        print("preparing dataset")
        messagebox.showinfo("Attention", "Initializing face capture. Look at the camera and wait ...")
        msgLabelNew['text'] = "  Preparing dataset"
        global id

        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height
        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        count = 0

        def edit_database_display (face_id, count):
            global boxLabel
            global msgLabelNew
            
            if not os.path.exists('dataset'):
                os.makedirs('dataset')

            frame= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
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
                cam.release()
                cv2.destroyAllWindows()
                msgLabelNew['text'] = "Preparing dataset completed"
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
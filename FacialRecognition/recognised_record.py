from datetime import datetime, date
import csv
import os
from csv import writer

def got(name):
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    #print("current time", time)
    #print("\ndate", today)

    if os.path.isfile('history.csv'):
        data = [today,time,name]
        with open('history.csv', 'a+', newline='\n') as f:
            writer_obj = writer(f, lineterminator="\n")
            writer_obj.writerow(data)
            f.close()
        print("added the data in file")
        return
    
    else:
        fields = ['Date', 'Time', 'Name']
        filename = 'history.csv'

        with open(filename, 'w') as csvfile:
            csvwriter = writer(csvfile)
            csvwriter.writerow(fields)
        data = [today, time, name]
        with open('history.csv', 'a+', newline='') as f:
            writer_obj = writer(f)
            writer_obj.writerow(data)
            f.close()
        print('made file and added the data')
        return

#got('nikhil')
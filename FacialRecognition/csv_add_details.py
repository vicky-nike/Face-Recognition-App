import pandas as pd
import csv
import os.path
from csv import writer

#name = input("Enter your name  : ")

def create(name):
    if os.path.isfile('records.csv'):
        results = pd.read_csv('records.csv')
        last = len(results)
        list_data=[last,name]
        with open('records.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list_data)  
            f_object.close()
        print("Entrollment successfull with ID %d ",last)
        return last
    
    else:
        # field names
        fields = ['ID','Name']
                
        # data rows of csv file
        rows = [ ['0','None']]
        filename = "records.csv"
        ID = 1
        # writing to csv file
        with open(filename, 'w') as csvfile:
                # creating a csv writer object
                csvwriter = csv.writer(csvfile)
                        
                # writing the fields
                csvwriter.writerow(fields)
                        
                # writing the data rows
                csvwriter.writerows(rows)
        list_data=[ID,name]
        with open('records.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list_data)  
            f_object.close()
        print("Entrollment successfull with ID %d ",ID)
        return ID

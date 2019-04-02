import csv
import os

filename = 'results.csv'

def save(results):
    try:
        csv_file = open(filename,'w+')
        csvWriter = csv.writer(csv_file,delimiter=',')
        
        csvWriter.writerow(results)
        
        print('records saved to ' + filename)
    except Exception as e:
        print(e)


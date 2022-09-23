
import csv


try:
    #parse the csv file bristol air quality data.csv
    with open('bristol-air-quality-data.csv', 'r') as f, open('crop.csv','w') as g:
        g.write('f.readlines()')
        #create a for loop to filter the date that is
        for x in f.readlines():
            if x[0:4].isnumeric() and int(x[0:4]) > 2009:
                g.write(x)
except BaseException as err:
    print(f"An error ocurred: {err}")
            
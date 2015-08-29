import csv

frame = 0

def openFile(file_name):
    fileReader = csv.reader(open(file_name, 'rb'), delimiter=',')

def read():
    movementsList = []
    row = fileReader[frame + 2]
    for x in range(1,25):
        movementsList.append(row[x + 18])

    return movementsList
    

    

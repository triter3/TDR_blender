import csv

frame = 0
tableReader = []
fileReader = []

def openTable(table_name):
    with open(table_name) as csvfile:
        file1 = csv.reader(csvfile, delimiter=';')
        global tableReader
        for row in file1:
            tableReader.append(row)

def openFile(file_name):
    with open(file_name) as csvfile:
        file1 = csv.reader(csvfile, delimiter=';')
        global fileReader
        for row in file1:
            fileReader.append(row)

def rotate(armature):
    global frame
    for x in range(0,25):  
        armature.bone_rotation(tableReader[0][x], tableReader[1][x], fileReader[frame + 2][x + 19])

    if frame >= 388:
        frame = 0
        print(reset)
    frame += 1
    

    

    

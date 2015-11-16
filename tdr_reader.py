import csv
import tdr_calcul
import bge

frame = 0
fileReader = []
table = []
scene = 0

def openTable(table_name):
    with open(table_name) as csvfile:
        file1 = csv.reader(csvfile, delimiter=';')
        global table
        for row in file1:
            table.append(row)
        for x in range(len(table) -1):
            print(x)
            for i in range(25):
                val = table[x + 1][i + 1]
                val = val.replace(",",".")
                val = float(val)
                table[x + 1][i + 1] = val

def openFile(file_name):
    with open(file_name) as csvfile:
        file1 = csv.reader(csvfile, delimiter=';')
        global fileReader
        for row in file1:
            fileReader.append(row)
        for x in range(len(fileReader) - 2):
            for i in range(18):
                val = fileReader[x + 2][i + 1]
                val = val.replace(",",".")
                val = float(val)
                fileReader[x + 2][i + 1] = val

def rotate(inc):
    global frame
    global scene

    frame = frame + inc
    if frame > len(fileReader)-6:
        frame = len(fileReader)-6
        print("reset")
    if frame < 0:
        frame=0
    print (fileReader[frame+2][0])
    tdr_calcul.calculations(table[2], table[3], table[4], fileReader[frame + 2], table[1], scene)

def oneframePlus(cont):
    global frame
    sens = cont.sensors["Keyboard.001"]
    if sens.positive:
        rotate(1)

def oneframeLess(cont):
    global frame
    sens = cont.sensors["Keyboard.002"]
    if sens.positive:
        rotate(-1)

def reset(cont):
    global frame
    frame = 0
    rotate()

def getScene(sc):
    global scene
    scene = sc



    # ant figura de condi(len(fileReader)-6
    

    

    

import csv #llibreries que permeten llegir fitxers .csv
import tdr_calcul #s'imporen les funcións del fitxer calculations.py
import bge #llibreria de blender

frame = 0 #variable global que conta per a quin fotograma va el programa
fileReader = [] #variable array que contindrà tots els valors del sensor que cal aplicar
table = [] #variable array que contindrà tots els valors de al configuració del gúa
scene = 0 #variable global

def openTable(table_name): #funció que s'ocupa de agafar la configurció del del fixer i passar-la a una array
    with open(table_name) as csvfile: #fucnió que obr el fixer
        file1 = csv.reader(csvfile, delimiter=';') #funció que passa el fitxer .csv a una array
        global table #s'indica que dintre aquesta funcó s'utilitzara la funcó global table
        for row in file1: #bucle que actuarà tantes vegades com lies hi ha el fitxer
            table.append(row) #aplica cada linia a la variable global table
        for x in range(len(table) -1): #bucle que actuarà tantes vegades com files menys una hi hagin
            for i in range(25): #bucle que es fara 25 vegades
                val = table[x + 1][i + 1] #es fica el valor de la rai en una determinada posicio a una variable
                val = val.replace(",",".") #si el valor es decimal tindra una coma, i aquesta funcó o trandformara a punt
                val = float(val) #aquesta funcó transorma un string a una variable float, per tant transforma un conjunt de caracters en un valor
                table[x + 1][i + 1] = val #torna ficar el valor de la variable val dintre la mateixa posició 

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
        print("finich")
    if frame < 0:
        frame=0
    print(fileReader[frame + 2][0])
    tdr_calcul.calculations(table[2], table[3], table[4], fileReader[frame + 2], table[1], scene)

def reset():
    global frame
    frame = 0
    rotate(0)

def getScene(sc):
    global scene
    scene = sc



    # ant figura de condi(len(fileReader)-6
    

    

    

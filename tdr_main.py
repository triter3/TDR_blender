import time #libreria de python
import bge #llibreria de Blender
import tdr_reader #s'imporen les funcións del fitxer reader.py
import math #llibreria de python


afterTime = 0 #varable global
own = 0 #variable global
FPS = 20 #variable global que conté el valor de fotorgames per segon que te d'anar el programa

def runningUp(cont): #funció que es crida desde un modul del del "Game Logic"
    global afterTime #s'indica que dintre aquesta funcó s'utilitzara la variable global afterTime
    global FPS #s'indica que dintre aquesta funcó s'utilitzara la variable global FPS
    nowTime = time.time() #Agafa els segons exactes que porta l'ordinador engegat
    delta = (nowTime - afterTime) * FPS #Es resten els segons que porta l'ordinador engegat per els segosn que portava l'ordinador engegat l'última vegada que s'ha fet un bucle, per així saber cuanta estona porta el programa sense fer un bule. I segudament es multiplica per els FPS, i ens dona un valor anomenat delta.
    if delta >= 1: #quan el valor delta es més gran o igual que 1, vol dir que ja toca fer un nou bucle i s'executa el codia que hi ha dinre aquest condicional
        tdr_reader.rotate(1) #es crida la funció rotate del fitxer reader.py i se li passa el valor 1 perque els fotogrames s'incrementin un més
        afterTime = nowTime #es fica el valor de la variable nowTime a la variable de la funcó afterTime


def runningDown(cont): #funció que fa el mateix que la anteror, l'unica diferencia es que quan crida la funció rotate li passa un menys 1 perque es redueixi un futugrama. Basicament es el mateix pero marxa en rere
    global afterTime
    global FPS
    nowTime = time.time()
    delta = (nowTime - afterTime) * FPS
    if delta >= 1:
        tdr_reader.rotate(-1)
        afterTime = nowTime

            

def init(cont): #funció que es criada el principi del programma
    global own #s'indica que dintre aquesta funcó s'utilitzara la funcó global own
    scene = bge.logic.getCurrentScene() #s'agafa l'escena que està en aquest moment al Blender.
    tdr_reader.openFile("prova_11_13.csv") #es crida la funció openFile del fitxer reader.py i se li passa el nom del fitxer que es desea obrir. Aquest fixter es el que conté els valors dels sensors de l'animació.
    tdr_reader.openTable("calibration.csv") #aquest funcio es molt semblant a l'anterior, l'única diferencia és que en aquesta es passa el nom del fitxer de configuracío del gua
    tdr_reader.getScene(scene) #aquesta funció bàsicament passa el valor scene a el fitxer reader.py
    #initAngles(scene)
    cont.owner["stat"] = "Animation_run" #es modifica la propietat del "GameLogic" anomenada stat
    print("init") #escriu a la consola de Blender init, per indicar que tot s'ha inicialitzat bé
    tdr_reader.rotate(0) #es crida la funció rotate del fitxer reader.py i se li passa el valor 0 perque sense sumarse cap fotograma es situi be la mà a la posició zero del fitxer .csv

def reset(cont): #es una funcó que es cridada desde el "Game Logic" i que bàsicament reinicia el contador de fotogrames a zero
   tdr_reader.reset() #crida la funcó reset de el fitxer reader.py

def oneframePlus(cont): #es la funció que permet sumar un sol fotograma més clicant la "i". Aquesta funcó es cridada desde el "Game Logic"
    sens = cont.sensors["Keyboard.001"] #es fica les propietats d'un sensor especific dintre d'una variable
    if sens.positive: #basicament serveix perque només es cridi la funció una vegada quan s'ha clicat el boto corresponent
        tdr_reader.rotate(1) ##es crida la funció rotate del fitxer reader.py i se li passa el valor 1 perque els fotogrames s'incrementin un més

def oneframeLess(cont): #funció que fa el mateix que l'anteriorm l'únic que crida la funció rotate passant el valor menys 1, perque així es redueixi un fotograma
    sens = cont.sensors["Keyboard.002"]
    if sens.positive:
        tdr_rotate.rotate(-1)

#def initAngles(scene):
    #scene.objects.get("Mio_home").channels["Thumb1_R"].rotation_mode = bge.logic.ROT_MODE_XYZ
    #scene.objects.get("Mio_home").channels["Thumb1_R"].rotation_euler = (0, 0, (-14.5 * (math.pi/180)))

    #scene.objects.get("Mio_home").channels["Index1_R"].rotation_mode = bge.logic.ROT_MODE_XYZ
    #scene.objects.get("Mio_home").channels["Index1_R"].rotation_euler = (0, 0, (5.0 * (math.pi/180)))

    #scene.objects.get("Mio_home").channels["Ring1_R"].rotation_mode = bge.logic.ROT_MODE_XYZ
    #scene.objects.get("Mio_home").channels["Ring1_R"].rotation_euler = (0, 0, (6.0 * (math.pi/180)))

    #scene.objects.get("Mio_home").channels["Pinky1_R"].rotation_mode = bge.logic.ROT_MODE_XYZ
    #scene.objects.get("Mio_home").channels["Pinky1_R"].rotation_euler = (0, 0, (10.0 * (math.pi/180)))

    #scene.objects.get("Mio_home").update()

    #scene.objects.get("Mio_home").channels["Thumb4_R"].rotation_mode = bge.logic.ROT_MODE_XYZ
    #scene.objects.get("Mio_home").channels["Thumb4_R"].rotation_euler = ((12 * (math.pi/180)), 0, 0)

    #scene.objects.get("Mio_home").update()


    





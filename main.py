import time
import bge
import armature
import reader

home = 0
afterTime = 0

def running(cont):
    FPS = 20
    nowTime = time.time()
    global afterTime
    delta = (nowTime - afterTime) * FPS
    if delta >= 1:
        update()
        global afterTime
        afterTime = nowTime
            

def init(cont):
    scene = bge.logic.getCurrentScene()
    reader.openFile("/home/edu/Documents/GitHub/TDR_Blender/hola.csv")
    reader.openTable("/home/edu/Documents/GitHub/TDR_Blender/table.csv")
    global home
    home = armature.Armature("Mio_home", scene)
    print("init")
    cont1 = bge.logic.getCurrentController()
    own = cont1.owner
    own["val"] = 1

def update():
        print("hola")
        reader.rotate(home)





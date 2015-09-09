import time
import bge
import armature
import reader

home = 0
def main(cont):
    print("start")
    init()
    running()

def running():
    run = True
    FPS = 1
    afterTime= time.time()
    while(run):
        nowTime = time.time()
        delta = (nowTime - afterTime) / FPS
        while(delta >= 1):
            update()
            delta -= 1
            afterTime = time.time()

def init():
    scene = bge.logic.getCurrentScene()
    reader.openFile("GCRANELLA.csv")
    global home
    home = armature.Armature("Mio_home", scene)
    

def update():
        print("hola")
        reader.rotate(home)





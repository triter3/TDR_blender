import time
import bge
import armature
import reader
import rotations

def main(cont):
    print("start")
    init()
    running()

def running():
    run = False
    FPS = 0.5
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
    reader.openFile("")
    home = armature.Armature("Mio_home", scene)
    

def update():
    print("hola")
    movementsList = reader.read()





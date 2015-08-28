import time
import bge
import armature
import reader

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
    P5_R = armature.Bones("Pinky5_R", "Mio_home", scene)
    P4_R = armature.Bones("Pinky4_R", "Mio_home", scene)
    I2_R = armature.Bones("Index2_R", "Mio_home", scene)
    

def update():
    print("hola")
    reader.read()
    



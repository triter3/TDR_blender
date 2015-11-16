import time
import bge
import tdr_reader
import math


afterTime = 0
own = 0

def running(cont):
    global own
    global afterTime
    if own["stat"] == "Animation_run":
        FPS = 20
        nowTime = time.time()
        delta = (nowTime - afterTime) * FPS
        if delta >= 1:
            update()
            afterTime = nowTime
            

def init(cont):
    global own
    scene = bge.logic.getCurrentScene()
    tdr_reader.openFile("prova_11_13.csv")
    tdr_reader.openTable("correccio.csv")
    tdr_reader.getScene(scene)
    #initAngles(scene)
    cont1 = bge.logic.getCurrentController()
    own = cont1.owner
    own["stat"] = "Animation_run"
    print("init")
    tdr_reader.rotate(0)

def update():
        tdr_reader.rotate(1)

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


    





import time

def main():
    print "start"
    running()

def running():
    run = True
    FPS = 1
    afterTime= time.time()
    while(run):
        nowTime = time.time()
        delta = (nowTime - afterTime) * FPS
        while(delta >= 1):
            update()
            delta -= 1
            afterTime = time.time()

def update():
    print "hola"

main()

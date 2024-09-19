import pgzrun, random
from time import time
TITLE="Satellites"
WIDTH=800
HEIGHT=600
satellites=[]
lines=[]
numberofsatellites=8
countsatellites=0
starttime=0
totaltime=0

def create_satellites():
    global starttime
    for i in range(0,numberofsatellites):
        satellite=Actor("satellites")
        satellite.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        satellites.append(satellite)
    starttime=time()



def draw():
    screen.blit("background",(0,0))
    number=1
    for satellite in satellites:
        number+=1
        satellite.draw()
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))


def update():
    pass
create_satellites()
pgzrun.go()
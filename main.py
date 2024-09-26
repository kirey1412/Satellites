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
    global totaltime,starttime
    screen.blit("background",(0,0))
    number=1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        number+=1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if countsatellites<numberofsatellites:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(totaltime)), (10,10), fontsize=30)


def on_mouse_down(pos):
    global countsatellites,numberofsatellites,satellites,lines
    if countsatellites <numberofsatellites:
        if satellites[countsatellites].collidepoint(pos):
            if countsatellites:
                lines.append((satellites[countsatellites-1].pos,satellites[countsatellites].pos))
            countsatellites+=1
        else:
            lines=[]
            countsatellites=0


def update():
    pass
create_satellites()
pgzrun.go()

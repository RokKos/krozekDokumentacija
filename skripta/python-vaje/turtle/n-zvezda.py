from turtle import *

FILEPATH = '../images/n-zvezda.png'
WIDTH = 400
HEIGHT = 250

setup(WIDTH, HEIGHT)
pu()
goto(-100, -HEIGHT/2 + 50)
pd()

## actual solution
n = 10
dolzina_stranice = 100
kot = 360 / n

import math

if n % 2 == 1:
    for i in range(n):
        fd(dolzina_stranice)
        lt(180-kot/2)
else:
    for i in range(int(n/2)):
        fd(dolzina_stranice)
        lt(2*kot)
    pu()
    lt(90 - kot)
    fd(dolzina_stranice / 2 / math.sin(math.radians(kot)))
    rt(180 - kot)
    fd(dolzina_stranice / 2 / math.sin(math.radians(kot)))
    lt(90 + kot)
    pd()
    for i in range(int(n/2)):
        fd(dolzina_stranice)
        lt(2*kot)



import subprocess
getcanvas().postscript(file="tmp.ps", colormode='color')
process = subprocess.Popen(["convert", "tmp.ps", FILEPATH])
#  import time
#  time.sleep(1)
#  process2 = subprocess.Popen(["display", FILEPATH])

#  done()

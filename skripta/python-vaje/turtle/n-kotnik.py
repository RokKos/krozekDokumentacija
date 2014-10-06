from turtle import *

FILEPATH = '../images/n-kotnik.png'
WIDTH = 400
HEIGHT = 280

setup(WIDTH, HEIGHT)
pu()
goto(-100, -HEIGHT/2 + 30)
pd()

## actual solution
n = 7
dolzina_stranice = 100
kot = 360 / n

for i in range(n):
    fd(dolzina_stranice)
    lt(kot)

import subprocess
getcanvas().postscript(file="tmp.ps", colormode='color')
process = subprocess.Popen(["convert", "tmp.ps", FILEPATH])
import time
time.sleep(1)
process2 = subprocess.Popen(["display", FILEPATH])

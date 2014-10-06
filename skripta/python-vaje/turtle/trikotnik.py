from turtle import *

FILEPATH = '../images/trikotnik.png'
WIDTH = 300
HEIGHT = 150

setup(WIDTH, HEIGHT)
pu()
goto(-WIDTH/2 + 30, -HEIGHT/2 + 30)
pd()

## actual solution
speed(1)
fd(100)
lt(120)
fd(100)
lt(120)
fd(100)

import subprocess
getcanvas().postscript(file="tmp.ps", colormode='color')
process = subprocess.Popen(["convert", "tmp.ps", FILEPATH])
#  process = subprocess.Popen(["display", FILEPATH])

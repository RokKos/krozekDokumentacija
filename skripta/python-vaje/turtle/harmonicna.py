from turtle import *

FILEPATH = '../images/harmonicna.png'
WIDTH = 800
HEIGHT = 120

setup(WIDTH, HEIGHT)
pu()
goto(-WIDTH/2+50, HEIGHT/2 - 30)
pd()

## actual solution
enota = 100
primerjaj = 560
n = 200

speed(0)

fd(primerjaj)
pu()
bk(primerjaj)
rt(90)
fd(50)
lt(90)
pd()
for i in range(1, n):
    fd(enota*1/i)
    lt(90)
    fd(20)
    bk(20)
    rt(90)

import subprocess
getcanvas().postscript(file="tmp.ps", colormode='color')
process = subprocess.Popen(["convert", "tmp.ps", FILEPATH])
#  import time
#  time.sleep(1)
#  process2 = subprocess.Popen(["display", FILEPATH])

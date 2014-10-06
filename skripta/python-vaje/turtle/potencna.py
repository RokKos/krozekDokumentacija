from turtle import *

FILEPATH = '../images/potencna.png'
WIDTH = 800
HEIGHT = 120

setup(WIDTH, HEIGHT)
pu()
goto(-WIDTH/2+50, HEIGHT/2 - 30)
pd()

## actual solution
enota = 300
n = 40

fd(2*enota)
pu()
bk(2*enota)
rt(90)
fd(50)
lt(90)
pd()
for i in range(n):
    fd(enota*2**-i)
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

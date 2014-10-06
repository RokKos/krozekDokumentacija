from turtle import *

FILEPATH = '../images/smrecica.png'
WIDTH = 1000
HEIGHT = 1000

setup(WIDTH, HEIGHT)
pu()
goto(-100, -HEIGHT/2 + 200)
pd()

## actual solution

s = 300
n = 10


rt(90)
fd(s/2)
lt(90)
fd(s/4)
lt(90)
fd(s/2)
pu()
lt(90)
bk(3/8*s)
pd()
fd(s)
pu()
bk(s)
rt(60)
pd()

for i in range(n):
    w = (n-i)/n * s
    fd(w)
    rt(120)
    fd(w/3)
    lt(120)

done()

import subprocess
getcanvas().postscript(file="tmp.ps", colormode='color')
process = subprocess.Popen(["convert", "tmp.ps", FILEPATH])
import time
time.sleep(1)
process2 = subprocess.Popen(["display", FILEPATH])

from graphics import *
import math

import fake_test
import numpy as np
"""
Take in data and convert to good format.
Input: Array 'outputArray' from 'fake_test.py' (array of 4-bit combinations).
Output: Tuple of 4 Arrays the nth array
contains all nth position qubits of strings in the input array.
"""
def take_data(inputArray):
    fstArray = []; sndArray = []; thdArray = []; fthArray = []
    for str in inputArray:
        fstArray.append(int(str[0])) # store first qubit of each str as an int
        sndArray.append(int(str[1]))
        thdArray.append(int(str[2]))
        fthArray.append(int(str[3]))
    return fstArray, sndArray, thdArray, fthArray

# combine helpers together
def main():
    # https://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html
    win = GraphWin('Art', 200, 150) # give title and dimensions
    center = {'x': 100, 'y': 75}

    cbits, iobits, szbits, shbits = take_data(fake_test.outputArray) # assuming list of tuples
    theta = 0
    r = 10
    for i in range(len(cbits)):
        if i>360:
            continue
        (cbit, iobit, szbit, shbit) = cbits[i], iobits[i], szbits[i], shbits[i]
        theta += 30 # or whatever

        sz = size(szbit)
        io = inout(iobit)
        r = io
        # r = max(10, r + io)
        x1 = r * math.cos(math.radians(theta))
        y1 = r * math.sin(math.radians(theta))
        sh = shape(shbit)

        if sh=='triangle':
            pt1 = Point(center['x']+x1, center['y']+y1)
            x2 = (r*sz) * math.cos(math.radians(theta - 3))
            y2 = (r*sz) * math.sin(math.radians(theta - 3))
            pt2 = Point(center['x']+x2, center['y']+y2)
            x3 = (r*sz) * math.cos(math.radians(theta + 3))
            y3 = (r*sz) * math.sin(math.radians(theta + 3))
            pt3 = Point(center['x']+x3, center['y']+y3)
            dit = Polygon(pt1, pt2, pt3)

        elif sh=='line':
            x2 = 2 * r * math.cos(math.radians(theta))
            y2 = 2 * r * math.sin(math.radians(theta))
            dit = Line(Point(center['x']+x1, center['y']+y1), Point(center['x']+x2, center['y']+y2))
            dit.setWidth(sz)

        dit.setFill(color(cbit))
        dit.draw(win)

    win.getMouse()
    win.close()


# make helpers
def color(i):
    # take int, return color string
    if i == 0:
        return color_rgb(105, 34, 143)
    
    elif i == 1:
        return color_rgb(8, 67, 138)
    

def inout(i):
    # take int, return coordinates?
    if i == 0:
        return np.random.randint(1,5)

    elif i == 1:
        return np.random.randint(10,15)

def size(i):
    # return size
    if i == 0:
        return np.random.randint(1,5)

    elif i == 1:
        return np.random.randint(10,15)

def shape(i):
    if i == 0:
         return 'line'

    elif i == 1:
        return 'triangle'

main()

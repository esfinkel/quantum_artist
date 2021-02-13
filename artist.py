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
    win = GraphWin('Art', 400, 400) # give title and dimensions
    center = {'x': 200, 'y': 200}

    cbits, iobits, szbits, shbits = take_data(fake_test.outputArray) # assuming list of tuples
    theta = 0
    r = 10
    for i in range(len(cbits)):
        # if theta > 100:
        #     continue
        (cbit, iobit, szbit, shbit) = cbits[i], iobits[i], szbits[i], shbits[i]
        theta += 13 # or whatever

        sz = size(szbit)
        r = inout(iobit)
        x1 = r * math.cos(math.radians(theta))
        y1 = r * math.sin(math.radians(theta))
        sh = shape(shbit)

        if sh=='triangle':
            pt1 = Point(center['x']+x1, center['y']+y1)
            x2 = r * math.cos(math.radians(theta - sz))
            y2 = r * math.sin(math.radians(theta - sz))
            pt2 = Point(center['x']+x2, center['y']+y2)
            x3 = r * math.cos(math.radians(theta + sz))
            y3 = r * math.sin(math.radians(theta + sz))
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
        return color_rgb(105, 34, 143) # purple - more common
    
    elif i == 1:
        return color_rgb(8, 67, 138) # blue
    

def inout(i):
    # take int, return coordinates?
    if i == 0:
        return np.random.randint(1,5) # equally common

    elif i == 1:
        return np.random.randint(10,15)

def size(i):
    # return size
    if i == 0:
        return np.random.randint(1,5) # equally common

    elif i == 1:
        return np.random.randint(10,15)

def shape(i):
    if i == 0:
         return 'line' # equally common

    elif i == 1:
        return 'triangle'

main()

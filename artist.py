from graphics import *
import math

import fake_test

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

    data = take_data(fake_test.outputArray) # assuming list of tuples
    theta = 0
    r = 10
    for i in len(data['firstArray']):
        (cbit, iobit, szbit, shbit) = data['firstArray'][i], data['secondArray'][i], data['thirdArray'][i], data['fourthArray'][i]
        theta += 5 # or whatever

        sz = size(szbit)
        io = inout(iobit)
        r = max(10, r + io)
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

    # ...
    win.getMouse()
    win.close()


# make helpers
def color(i):
    # take int, return color string
    return 'red'

def inout(i):
    # take int, return coordinates?
    return 10

def size(i):
    # return size
    return 5

def shape(i):
    return 'line'
    
#extra helpers
# The following four take Dictionary input (specifically from 'take_data(..)'
# and return an array of the nth qubits from the RNG output.
def first(input):
    return take_data(input).get('firstArray')
def second(input):
    return take_data(input).get('secondArray')
def third(input):
    return take_data(input).get('thirdArray')
def fourth(input):
    return take_data(input).get('fourthArray')

#main()

#Tests for the different functions above. Un-comment and use.

#print(take_data(["0000", "0001", "1000", "1100"]))
#print(take_data(outputArray))
#print(first(["0000", "0001", "1000", "1100"]))
#print(first(outputArray))
    

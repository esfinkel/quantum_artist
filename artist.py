from graphics import *
from fake_test import *

"""
Take in data and convert to good format.
Input: Array 'outputArray' from 'fake_test.py' (array of 4-bit combinations).
Output: Dictionary 'outputDict' containing four arrays where the nth array
contains all nth position qubits of strings in the input array, in the form
{'firstArray': [1,0,..0],..., 'fourthArray': [1,0,...0]}.
"""
def take_data(inputArray):
    fstArray = []; sndArray = []; thdArray = []; fthArray = []
    for str in inputArray:
        fstArray.append(int(str[0])) # store first qubit of each str as an int
        sndArray.append(int(str[1]))
        thdArray.append(int(str[2]))
        fthArray.append(int(str[3]))
    outputDict = {'firstArray':fstArray, 'secondArray':sndArray,
                  'thirdArray':thdArray, 'fourthArray':fthArray} #dictionary to retun all the qubit arrays.
    return outputDict
# Note: I wrote some extra helpers first (outputArray), second (...), etc. that
# give each int array by itself. You can use them in main() or call this 
# function  as take_data(outputArray).

# combine helpers together
def main():
    # https://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html
    import math
    win = GraphWin('Art', 200, 150) # give title and dimensions
    center = {'x': 100, 'y': 75}

    data = take_data() # assuming list of tuples
    theta = 0
    r = 10
    for (cbit, iobit, szbit, shbit) in data:
        theta += 5 # or whatever

        # # if circle
        # r = max(10, r + size(szbit))
        # x = r * math.cos(math.radians(theta))
        # y = r * math.sin(math.radians(theta))
        # dit = shape(shbit)(Point(x, y), r)
        # dit.setFill(color(cbit))
        # dit.draw(win)

        # if triangle
        sz = size(szbit)
        r = max(10, r + sz)
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        pt1 = Point(center['x']+x, center['y']+y)
        x2 = (r*sz) * math.cos(math.radians(theta - 3))
        y2 = (r*sz) * math.sin(math.radians(theta - 3))
        pt2 = Point(center['x']+x2, center['y']+y2)
        x3 = (r*sz) * math.cos(math.radians(theta + 3))
        y3 = (r*sz) * math.sin(math.radians(theta + 3))
        pt3 = Point(center['x']+x3, center['y']+y3)
        dit = Polygon(pt1, pt2, pt3)
        dit.setFill(color(cbit))
        dit.draw(win)

        # if line
        sz = size(szbit)
        r = max(10, r + sz)
        x1 = r * math.cos(math.radians(theta))
        y1 = r * math.sin(math.radians(theta))
        x2 = 2 * r * math.cos(math.radians(theta))
        y2 = 2 * r * math.sin(math.radians(theta))
        dit = Line(Point(center['x']+x1, center['y']+y1), Point(center['x']+x2, center['y']+y2))
        dit.setWidth(sz)
        dit.setFill(color(cbit))
        dit.draw(win)

    # shape(i)(...)

    '''

    for i in range(points):
    r = (data1[i%5] + 1) * 10
    x = r * cos(radians(i*360/points)) + 50
    y = r * sin(radians(i*360/points)) + 50
    if data2[i%5]==1:
        fill(153)
    else:
        fill(204, 102, 0)
    size = (data3[i%5] + 1) * 2
    if data4[i%5]==1:
        triangle(x, y, x+size, y, x+(size/2), y+size)
    else:
        circle(x, y, size)


    '''

    # ...
    win.getMouse()
    win.close()


# make helpers
def color(i):
    # take int, return color string
    pass

def inout(i):
    # take int, return coordinates?
    pass

def size(i):
    # return size
    pass

def shape(i):
    return Circle # or something
    
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
    
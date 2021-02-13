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
    win = GraphWin('Art', 200, 150) # give title and dimensions

    # shape(i)(...)

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
    
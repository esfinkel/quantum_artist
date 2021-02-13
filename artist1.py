#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 09:09:57 2021

@author: kshama.m17
"""
import graphics as gr
import four_bit_quantum_rng as fbqrng
line_width = 50
test_array = []

"""
Take in data and convert to good format.
Input: Array 'outputArray' from 'four_bit_quantum_rng.py' (array of 4-bit combinations).
Output: Dictionary 'outputDict' containing four arrays where the nth array
contains all nth position qubits of strings in the input array, in the form
{'firstArray': [1,0,..0],..., 'fourthArray': [1,0,...0]}.
"""
def take_data(inputArray):
    fstArray = []; sndArray = []; thdArray = []; fthArray = []
    for str in inputArray:
#        print (str[0])
#        print (int(str[0]))
        fstArray.append(int(str[0])) # store first qubit of each str as an int
        sndArray.append(int(str[1]))
        thdArray.append(int(str[2]))
        fthArray.append(int(str[3]))
    outputDict = {'firstArray':fstArray, 'secondArray':sndArray,
                  'thirdArray':thdArray, 'fourthArray':fthArray} #dictionary to retun all the qubit arrays.
    return outputDict
# Note: I wrote some extra helpers 'first (outputArray)', 'second (...)', etc. that
# give each int array by itself. You can use them in adddition to the above
# in main() or call this function  as take_data(outputArray).

# combine helpers together
def main():
    win = gr.GraphWin("My Art", 1000, 700) #title and dimensions.
    win.setCoords(0, 0, 1000, 700) #set coordinate system (xll, yll, xur, yur)
   
#    firstArray = [0,0,1] #results of 'take_data(..)' and 'first(..)' from artist.py
#    secArray = [0,0,1]
#    thirdArray = [0.,1,0]
#    fourthArray = [1,1,0]
    data = fbqrng.generate_data(fbqrng.circuit4)
    firstArray = first(data) #results of 'take_data(..)' and 'first(..)' from artist.py
    secArray = second(data)
    thirdArray = third(data)
    fourthArray = fourth(data) 
    
    #The path we'll sweep:
    x = -9; y = -9 #initialize coords.
    for j in range(len(firstArray)): # 0-999
        
        x = x + 30; y = y + 30 #Moving in a diagonal. Will have to play around with this.
        
        slope = inout(secArray[j]) #calling all the helper functions.
        breadth = size(thirdArray[j]) 
        shape1 = shape(fourthArray[j]) 
        color1 = color(firstArray[j])
        if shape1 == gr.Line: #checking to define GraphicObjects to be drawn.
            shape1 = gr.Line(gr.Point(x, y), gr.Point(x + (slope * breadth), y + (slope * breadth)))
            shape1.setWidth(line_width)
            shape1.setFill(color1)
        else:
            shape1 = gr.Polygon(gr.Point(x, y), 
                         gr.Point(x + (slope * breadth), y + (slope * breadth)), 
                         gr.Point(x + 7, y))
            shape1.setFill(color1)
        shape1.draw(win) #draw GraphicObject
        #print(j) #just a check
        
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

#returns string
def color(i):
    colorStr = "red" if i == 0 else "yellow"
    return colorStr

#returns int (slope)
def inout(i):
    val = 1 if i == 0 else -1
    return val

#returns int
def size(i): #the distance between 2 points for a line
    #and triangle (kinda isoceles?).
    breadth = 10 if i == 0 else 30
    return breadth

#returns GraphicsObject
def shape(i): 
    shapeObj = gr.Line if i == 0 else gr.Polygon
    return shapeObj
    
#extra helpers
# The following four take Dictionary input 'outputDict' (specifically from 'take_data(..)'
# and return an array of the nth qubits from the RNG output.
def first(input):
    return take_data(input).get('firstArray')
def second(input):
    return take_data(input).get('secondArray')
def third(input):
    return take_data(input).get('thirdArray')
def fourth(input):
    return take_data(input).get('fourthArray')

main()
#Tests for the different functions above. Un-comment and use.

#print(take_data(["0000", "0001", "1000", "1100"]))
#print(take_data(outputArray))
#print(first(["0000", "0001", "1000", "1100"]))
#print(first(outputArray))
    

import random
from matplotlib.pylab import *
import matplotlib.pylab as plt
__doc__ = matplotlib.pylab.__doc__

import math

    
def qpoints(coeffs, x1, x2,  n):
    values = []
    l=len(coeffs)
    for i in range(0,n):
        x=random.uniform(x1, x2)
        y=0
        for c in range(0, l):
            y += coeffs[c]*x**(l-1-c)
        values.append( (x,y) )
    values.sort()
    return values


def evalY(coeffs, x1, x2, n):
    if n %1 != 0:
        print ("n must be an interger")
    else:
        y = []
        poly = []
        l = len(coeffs)
        difference = (x2 - x1) / n
        for Xvalue in range(0, int(n) + 1):
            x = x1
            for c in range(0, l):
                if x != x2:
                    poly.append(coeffs[c]*x**(l-1-c))
                    value = sum(poly)
                else:
                     poly.append(coeffs[c]*x2**(l-1-c))
                     value = sum(poly)
            x1 =  x1 + difference
            y.append(float(value))
            poly = []
        return y
    
    


def points2plot(lst):
    x=[]
    y=[]
    for t in lst:
        x.append(t[0])
        y.append(t[1])
    return [x,y]


def yValues(lst):
    y=[]
    for t in lst:
        y.append(t[1])
    return y


def graphxy(x,y):
    ## Create a blank window
    fig = plt.figure()
    ## Name the graph we are plotting "quad" and put it in the right place for a single graph
    quad = fig.add_subplot(111)
    ## Plot the values from our x and y.
    quad.plot(x,y)
    ## Matplotlib calls the lines in the graph spines.
    ## Put the y axis centered at zero.
    quad.spines['left'].set_position('zero')
    ## Put the x axis centered at zero.
    quad.spines['bottom'].set_position('zero')
    ## Turn off the edge of the box on the right side.
    quad.spines['right'].set_color('none')
    ## Turn off the edge of the box on the top side.
    quad.spines['top'].set_color('none')
    ## Show the graph
    plt.show()


def simpsons(coeffs, x1, x2, n):
        if n%2==0:  
            deltaX=float((x2-x1)/n)
        else:   
            print("n must be even for simpsons rule")
        values = evalY(coeffs, x1, x2, n)
        yvalue = []
        try:
            for numbers in values:
                decimal = float(numbers)
                yvalue.append(decimal)
            simpsons = []
            t = 1
            simpsons.append(yvalue[0])
            for value in yvalue:
                if t != n:
                    if value != yvalue[0] and yvalue[n]:
                        if t%2 == 1:
                            value = float(value) * float(4)
                            simpsons.append(float(value))
                            t += 1
                        else:
                            value = float(value) * float(2)
                            simpsons.append(float(value))
                            t += 1
            simpsons.append(yvalue[n])
            answer = float(0)
            for values in simpsons:
                answer = float(answer) + float(values)
            answer = float(answer) * float(deltaX/3)
            return answer
        except:
            print("")


def trapezoidal(coeffs, x1, x2, n):
    deltaX=float((x2-x1)/n)
    values = evalY(coeffs, x1, x2, n)
    yvalue = []
    try:
        for numbers in values:
            decimal = float(numbers)
            yvalue.append(decimal)
        trap = []
        t = 1
        trap.append(yvalue[0])
        for value in yvalue:
             if t != n:
                if value != yvalue[0] and yvalue[n]:
                    value = float(value) * float(2)
                    trap.append(float(value))
                    t += 1
        answer = 0
        for values in trap:
            answer = float(answer) + float(values)
        answer = float(answer) * float(deltaX/2)
        trap.append(yvalue[n])
        return answer
    except:
        print ("")


def midpoint(coeffs, x1, x2, n):
    deltaX=float((x2-x1)/n)
    values = evalY(coeffs, x1, x2, n)
    yvalue = []
    try:
        for numbers in values:
            decimal = float(numbers)
            yvalue.append(decimal)
        midpoint =[]
        t = 1
        midpoint.append(yvalue[0])
        for value in yvalue:
            if t != n:
                    if value != yvalue[0] and yvalue[n]:
                         value = float(.5) * (yvalue[t] + yvalue[t + 1])
                         midpoint.append(value)
                         t += 1 
        midpoint.append(yvalue[n])
        answer = 0
        for values in midpoint:
            answer = float(answer) + float(values)
        answer = float(answer) * float(deltaX)  
        return answer
    except:
        print ("")


def approximation(coeffs, x1, x2, n):
    try:
        if n < 0 and n%1 != 0:
            print ("n must be an integer and positive")
            return
        if n == 0:
            print ("n cannot equal zero")
            return 
        if n < 0:
            print ("n must be positive")
            return 
        if n %1 != 0:
            print ("n must be an integer")
            return
        trap = trapezoidal(coeffs, x1, x2, n)
        mid = midpoint(coeffs, x1, x2, n)
        simpson = simpsons(coeffs, x1, x2, n)
        print("trapizoidal rule: ", trap)
        print("midpoint rule: ", mid)
        print("simpsons rule: ", simpson)
        points = qpoints(coeffs, x1, x2, n+1000)
        plot = points2plot(points)
        graphxy(plot[0],plot[1])
    except:
        print("")
        
        
    
            
    


       
  
    
    
            
    
        
    


from math import cos, sin, sqrt

#a = 1.0
#b = 1.0
#c = 1.0
#d = 0.0
#e = 4.5
#f = 2.0

# y = a + b*sin(c*x + d)

def dest(x):
    return a + b * sin(c*x+d)

def fun(x):
    return  e - b*c*cos(c*x+d)*(a+b*sin(c*x+d)-f) - x

def funp(x):
    #-2cos(x) ** 2
    return b*c*c*sin(c*x+d)*(a+b*sin(c*x+d)-f)-b*b*c*c*(cos(c*x+d)**2)-1

def dist(x):
    return sqrt((x-e)**2.0 + (a+b*sin(c*x+d)-f)**2.0)

def newtons(guess, depth):
    if depth == 0:
        return guess 
    
    return newtons(guess - (fun(guess)/funp(guess)), depth - 1)

def dist_to_sine(px, py, a, b, c, d):
    """ 
    return distance from point (px, py) to sine
    y = a + b*sin(c*x + d)
    """
    x = px
    for i in range(4):
        si = sin(c*x + d)
        co = cos(c*x + d)
        first = px - b*c*co*(a+b*si-py) - x
        second = b*c*c*si*(a+b*si-py)-b*b*c*c*co*co-1
        x = x - (first / second)

    return sqrt((x-px)**2.0 + (a+b*sin(c*x+d)-py)**2.0)
#x = e 
#print ('init x: ', x)
#x = newtons(x,15)
#print (x, dest(x), dist(x))
#print(dist_to_sine(4.5, 2.0, 1.0, 1.0, 1.0, 0.0))

import math
x , y , z = map(int , input().split())
def theatreSquare(x , y , z):
    a = math.ceil(x / z)
    b = math.ceil (y / z)
    return a * b
print (theatreSquare(x , y , z))    

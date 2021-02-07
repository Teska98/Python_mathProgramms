import math
b= int(input())
c= int(input())
alfal=int(input())
alfa=math.radians(alfal)
a=(b**2)+(c**2)-(2*b*c*(math.cos(alfa)))
print (math.sqrt(a))

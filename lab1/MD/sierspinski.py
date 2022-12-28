from turtle import *
right(30)
pu()
ht()
shape("triangle")
speed(300)
def sierpinski(s,n):
       if n==0:
              stamp()
       else:
              for i in range(0,3):
                     forward(s)
                     sierpinski(s/2,n-1)
                     backward(s)
                     left(120)
a=5
sierpinski(25*pow(2,a-2),a)
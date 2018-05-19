#!/usr/bin/python

def a (m,n):
        return (m*m) - (n*n)

def b (m,n):
        return 2 * m * n

def c (m,n):
        return (m*m) + (n*n)

SIZE=100

for x in range(1, SIZE):
    for y in range(1, SIZE):
        if y<x:
            A=a(x,y)
            B=b(x,y)
            C=c(x,y)
#           D=(A + C) / B
            print C, A, B       #, D



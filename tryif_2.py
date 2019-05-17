import numpy as np
import sys

print("Welcome")

while(1):
    try:
        a1=int(input())
        break
    except ValueError:
        print("retry")
        continue
print(a1)

while(1):
    try:
        a2=int(input())
        break
    except ValueError:
        print("retry")
        continue
print(a2)

while(1):
    try:
        a3=int(input())
        break
    except ValueError:
        print("retry")
        continue
print(a3)

while(1):
    try:
        a4=int(input())
        break
    except ValueError:
        print("retry")
        continue
print(a4)

b=np.array([[a1,a2],[a3,a4]])
print(b)

while(1):
    try:
        a5=int(input())
        break
    except ValueError:
        print("retry")
        continue
print(a5)

while(1):
    try:
        a6=int(input())
        break
    except ValueError:
        print("retry")
        continue
print(a6)

while(1):
    try:
        a7=int(input())
        break
    except ValueError:
        print("retry")
        continue
print(a7)

while(1):
    try:
        a8=int(input())
        break
    except ValueError:
        print("retry")
        continue
print(a8)

c=np.array([[a5,a6],[a7,a8]])
print(c)

d=b*c
print(d)

import numpy as np

print("Welcome")

while(1):
    try:
        a1=int(input())
        a2=int(input())
        a3=int(input())
        a4=int(input())
        b=np.array([[a1,a2],[a3,a4]])
        print(b)
        a5=int(input())
        a6=int(input())
        a7=int(input())
        a8=int(input())
        c=np.array([[a5,a6],[a7,a8]])
        print(c)
        print("よければY、だめならNを入力してください")
        cancan=input()
        if cancan=="y":
            break
        elif cancan=="n":
            continue
        
        except ValueError:
            print("retry")
            continue
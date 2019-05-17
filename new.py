while True:
    b=int(input())
    if type(b) is int:
        break
    else:
        continue
print("b is int<type> %d"%b)

while True:
    a=int(input())
    if a>10:
        break
    elif a==0:
        print("foolish")
        continue
    else:
        continue
print("aは%d"%a)

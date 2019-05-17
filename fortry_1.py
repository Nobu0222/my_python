i=0
list=[]


while i<10:
    i+=1
    try:
        list[i]=int(input())
    except ValueError:
        continue
    
print(list)
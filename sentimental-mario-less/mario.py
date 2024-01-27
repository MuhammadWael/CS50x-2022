while True:
    try:
        n = int(input("Height : "))
    except ValueError:
        continue
    else :
        if n in range (1,9):
            break

for i in range(n):
    for j in range(1,n-i):
        print(" ",end = "")
    for k in range(i+1):
        print("#",end = "")
    print("")

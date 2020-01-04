for row in range(1,6):
        for col in range(row):
                print(" ",end="")
        for col2 in range(5,row-1,-1):
                        print("*",end="")
        print()
        
star=1
for row in range(6,0,-1):
        for col in range(row-1,0,-1):
                print(" ",end="")
        print("*"*star,end=" ")
        star+=2
        print()


for row in range(1,6):
        for col in range(0,row):
                print(end="* ")
        print()
print("------------------------------------------")
for row in range(5):
        for col in range(0,row+1):
                print(row,end=" ")
        print()
print("------------------------------------------")
for row in range(5):
        for col in range(0,row+1):
                print(col,end=" ")
        print()
print("------------------------------------------")
for row in range(5):
        for col in range(0,row+1):
                print(end="~ ")
        print()
print("@@@@@@@@@@@@@@@@@@")
for row in range(5,0,-1):
        for col in range(row,0,-1):
                print(end="* ")
        print()
print("@@@@@@@@@@@@@@@@@@")
for row in range(5,0,-1):
        for col in range(row,0,-1):
                print(col,end=" ")
        print()
print("@@@@@@@@@@@@@@@@@@")
for row in range(5,0,-1):
        for col in range(row,0,-1):
                print(row,end=" ")
        print()
print("@@@@@@@@@@@@@@@@@@")
for row in range(0,6):
        for col in range(5,0,-1):
                print("",end="@")
                if row == col:
                        print("*"*row,end="")
        print()
print("@@@@@@@@@@@@@@@@@@")
for row in range(1,6):
        for col in range(5,row-1,-1):
                print("",end="@")
                if row == col:
                        print("*"*row,end="")
        print()
print("@@@@@@@@@@@@@@@@@@")

num=int(input("Enter the num value:"))
for x in range(1,num+1):
        for y in range(num,0,-1):
                print(end="@")
        for y in range(1,num+1):
                if x==1 or x==num:
                        print("*",end="")
                elif y==1 or y==num:
                        print("*",end="")
                else:
                        print(" ",end="")
        print()

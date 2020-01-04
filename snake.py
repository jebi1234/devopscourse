star=1
n=5
for i in range(n,0,-1):
        for j in range(i,0,-1):
                print(end="8")
        
        print("*"*star,end="")
        star+=2
        print() 

star=9
n=5
for i in range(n,0,-1):
        for j in range(i):
                print("8",end="")
        if star >0:
                print("*"*star,end=" ")
        star-=2
                
        print()

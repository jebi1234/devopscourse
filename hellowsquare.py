n=5
m=n
for i in range(n):
        for k in range(i):
                print(end=" ")
        for j in range(n):
                if (j==0 or j==n) or( i==0 or i==n) or (i==n-1 and j>0 and j<n) or (j==n-1 and i<n-1) :
                        print(end="*")
                else:
                        print(" ",end="")
        print()

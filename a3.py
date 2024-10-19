r=int(input("Enter no.rows : "))
c=int(input("Enter no.columns : "))
for i in range(1,r):
    for k in range(1,c):
     if i==1 or k==1 or i==r-1 or k==c-1 or i==k:
        print(" * " , end="")
     else:
        print( "   ",end="")
    print()

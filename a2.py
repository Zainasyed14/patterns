h = int(input("Enter no. of rows : "))
number=1
for i in range(h):
    for j in range(i+1):
        print(number, end="")
        number=number+1
    print()
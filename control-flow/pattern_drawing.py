user = int(input("Enter the size of the pattern: "))
row = 1
height = 1
while row <= user:
    for height in range (1,user+1):
        print("*",end="")
        height+=1
    print()
    row+=1

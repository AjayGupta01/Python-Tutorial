for row in range(6):
    for col in range(4):
        if col==0 or row==5 and col!=0:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
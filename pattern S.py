for row in range(7):
    for col in range(4):
        if row==0 and col!=0 or row==6 and col!=3 or row==3 and 0<col<3 or col==0 and 0<row<3 or col==3 and 3<row<6:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
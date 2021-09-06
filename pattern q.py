for row in range(6):
    for col in range(5):
        if ((row==0 or row==4) and 0<col<4) or ((col==0 or col==4) and 0<row<4) or row==col+1 and col!=1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
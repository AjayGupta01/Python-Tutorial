for row in range(5):
    for col in range(5):
        if (col==0 or col==4) and row!=4 or (row==4 and 0<col<4):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
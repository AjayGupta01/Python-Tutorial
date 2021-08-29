for row in range(6):
    for col in range(5):
        if col==0 or col==4 or row==col and col>0 and col<3 or col==3 and row==1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
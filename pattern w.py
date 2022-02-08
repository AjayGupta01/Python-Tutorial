for row in range(6):
    for col in range(5):
        if col==0 or col==4 or row+col==5 and row>2 or row==4 and col==3 :
            print("*",end=" ")
        else:
            print(end="  ")
    print()
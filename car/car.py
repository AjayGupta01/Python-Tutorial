'''
here is your code for car pattern with the help of star.
SEE IMAGE FOR LABELLING AND FOR BETTER UNDERSTANDING.
      ******PLEASE LIKE, SHARE AND SUBSCRIBE MY CHANNEL*********
'''



for row in range(10):
    for col in range(23):
        if (row==0 and 7<col<19) or ((row+col==8 or col-row==18) and row<3) or (row==3) or ((col==0 or col==22) and 3<row<8) or (row==7 and (col<5 or 7<col<15 or col>17)) or ((row==5 or row==9) and (4<col<8 or 14<col<18)) or ((col==4 or col==8 or col==14 or col==18) and 5<row<9):
            print("*",end=" ")
        else:
            print(end="  ")
    print()

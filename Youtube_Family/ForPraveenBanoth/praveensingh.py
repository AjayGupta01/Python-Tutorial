'''
Please Like , Share and Subscribe 

MY Channel

@Code With Ajay

'''



a=["P","R","S","H","A","N","I","G","V","E","N","E"]           
x=0
for row in range(5):
    for col in range(8):
        if (col==0) or (row+col==4 and row!=0) or ((col-row==2 or row+col==8) and 0<row<4):
            print(a[x],end=" ")
            x=x+1
        else:
            print(end="  ")
    print()

    
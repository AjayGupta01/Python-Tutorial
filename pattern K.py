row_val=0
col_val=3
for row in range(7):
    for col in range(4):
        if col==0 or row==col+3:
            print('*',end=' ')
        elif row==row_val and col==col_val:
            print('*',end='  ')
            row_val=row_val+1
            col_val=col_val-1
        else:
            print(end='  ')
    print()
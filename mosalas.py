side_1 = int(input ('please enter the First side value :'))
side_2 = int(input ('please enter the second side value :'))
side_3 = int(input ('please enter the third side value :'))

if side_1 < (side_2 + side_3) and side_2 < (side_1 + side_3) and side_3 < (side_1 + side_2):
    print(' ok ') 

else :
    print(' no ')
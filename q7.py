import random 
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
while list[0]==list[1] or list[1]==list[2] or list[2]==list[0] is True:
     global y
     y=random.choices(list,k=3)
     if list[0]==list[1] or list[1]==list[2] or list[2]==list[0] is False:
        print(y)
    


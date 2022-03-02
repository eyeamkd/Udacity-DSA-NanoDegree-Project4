def min_operations(target_number:int):
    current_number = 0
    operations = 0
    while(target_number>0):
        if target_number%2!=0:
            target_number-=1
            operations+=1
        else:
            target_number/=2 
            operations+=1
    print(operations)
        

min_operations(18)
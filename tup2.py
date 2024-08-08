tuple=(5 , 8 , 2 , 4, 7)

def max():
    max_value=tuple[0]

    for i in tuple:
        if i>max_value:
           

           max_value=i
           print(f"the max number is {max_value}")

max()
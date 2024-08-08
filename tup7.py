dict={'x' : '1' , 'y' : '2' , 'z' :'4'}

tuple_sort= tuple(sorted(dict.items() , key=lambda item : item[1] , reverse=True))

print(tuple_sort)
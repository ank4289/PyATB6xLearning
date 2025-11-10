numb=[1,2,3,4,5]

def even_num(x):
    return x%2==0



even_filter=list(filter(even_num,numb))
print(even_filter)
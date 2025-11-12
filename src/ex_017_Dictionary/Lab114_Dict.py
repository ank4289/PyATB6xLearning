Dict1={"a":1,"b":2,"c":3,"D":1}

uniq_val=set()
result={}

for key,value in Dict1.items():
    if value not  in uniq_val:
        result[key]=value
        uniq_val.add(value)

print(result)
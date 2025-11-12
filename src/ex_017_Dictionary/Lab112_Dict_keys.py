Dict1={"a":1,"b":2,"c":3}
print(Dict1.keys())
print(Dict1.values())

dict2={"a":2,"b":2}

Missing_key=set(Dict1.keys()-dict2.keys())

print(Missing_key)
key=["name","role","experience"]
value=["Aman","SDET",3]

my_dict=dict(zip(key,value))
print(my_dict)

dict1={"a":1,"b":2}
dict2={"C":3,"D":4}

merge_dict=dict1 | dict2
print(merge_dict)
print(merge_dict.get("a"))
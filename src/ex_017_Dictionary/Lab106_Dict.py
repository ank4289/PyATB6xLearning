Mydict = {
    "name": "Ankit Sharma",
    "age": 35,
    "role": "Software Test Lead",
    "experience": 10
}

print(Mydict)
print(Mydict["name"])
print(Mydict["age"])
print(Mydict["role"])
print(Mydict["experience"])

Mydict["role"]="Manual Tester"
print(Mydict)

del Mydict["age"]
print(Mydict)

for x, y in Mydict.items():
    print(x,y)

print("age" in Mydict)
print("role" in Mydict)
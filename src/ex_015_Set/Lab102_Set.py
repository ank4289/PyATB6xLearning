#SET
#Collection to unique
#{} -parenthesis

list_of_unique_item={1,2,3,4,4,5,5}
print(list_of_unique_item)

list=[45.2,33,33,45,21]
set1=set(list)
print(set1)

t=("TheTestingAcademy","for","TesterAcademy")
print(t)
print(set(t))

mixed={1,"QA",True,3.5}
print(mixed)

empty=set()
print(type(empty))

for item in mixed:
    print(item)

mixed.add(10)
print(mixed)
mixed.remove(10)
print(mixed)
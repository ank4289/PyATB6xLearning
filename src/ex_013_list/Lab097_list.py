A_list=[1,2,3]

A_list[0]="Ankit"
A_list[1]="Sharma"
A_list[2]="Tester"

for item in A_list:
    print(item)

#Range() also return the list

for i in range(1,5):
    print(i)

A_list=[1,2,3]
print("zeroth index:",A_list[0])
print("First index",A_list[1])
print("Second index",A_list[2])

A_list.append(4)
print(A_list)

A_list.append(5)
print(A_list)
#extend()-Append a new list
A_list.extend([7,8,10,11])
print(A_list)

#insert()
A_list.insert(1,"Sharma")
print(A_list)
print(len(A_list))
A_list.insert(0,0)
print(A_list)

A_list[0]="Ankit"
print(A_list)

A_list.remove("Ankit")
print(A_list)

A_list_Copy=A_list.copy()
print(A_list)
print(A_list_Copy)

A_list_Copy.remove("Sharma")
print(A_list_Copy)
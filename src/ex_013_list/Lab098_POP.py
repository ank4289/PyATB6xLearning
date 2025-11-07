Square=[1,4,9,16,25]

print(Square)
sq_pop=Square.pop()
print(sq_pop)
print(Square)
Sq_pop_new=Square.pop(2)
print(Sq_pop_new)
print(Square)

Square.clear()
print(Square)

Number=[10,20,30,20,50]
index_return=Number.index(20)
print(index_return)

print(Number.count(20))

Number.sort()
print(Number)

Number.sort(reverse=True)
print(Number)

Number.reverse()
print(Number)

print(max(Number))
print(min(Number))
print(sum(Number))

#slicing
print(Number)
print(Number[2:4])
print(Number[-1])

print("apple" in Number)
print(20 in Number)
#range(1,5) -> list
l=list(range(1,5))
print(l)
#nested list
Matrix=[[1,2,3],[4,5,6],[7,8.9]]
print(Matrix[1][2])

#del statement
del Number[0]
print(Number)
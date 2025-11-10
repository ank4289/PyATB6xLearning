set1={1,2,3}

set2={3,4,5}

print(set1.union(set2))
print(set1|set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1-set2) #it will print element set1 that are not present in set2

print(set2-set1) #it will print element set2 that are not present in set1

print(set1^set2) #will print only the elements which are not common in both set


set1={1,2,3}
set2={4,5,6}

print(set1.union(set2))

set1={1,2,3,4,5,6}
set2={7,8,9,4,5,10}

print(set1.intersection(set2))

print(set1-set2)

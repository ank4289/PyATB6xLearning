cities=("London","Paris","Los Angles","Tokyo")
print(len(cities))
print("Paris" in cities)
print("New Delhi" in cities)


#t=(2,3,5)
#t.append(2)

#real example
live_url=(["test.com","Jira.com","Google.com"])
print(live_url)

colors=("Red","Green","White","Yellow")
for c in colors:
    print(c)

number=(1,2)*3
print(number)

num="Ankit"*3
print(num)

nums=(1,2,2,3,4)
print(nums)
print(nums.count(2))
print(nums.index(3))

my_list=[1,2,3]
my_tuple=tuple(my_list)
print(my_tuple)

back_to_list=list(my_tuple)
print(back_to_list)
print(max(back_to_list))

My_list=[1,2,3]

print(My_list[0:2])
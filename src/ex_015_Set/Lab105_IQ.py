#first non repeating character swiss answer=w

s=set()
def non_repeating_char(string):

    for i in string:
        if string.count(i) == 1:
            s.add(i)
            return i
    return None  # outside the for loop

print(non_repeating_char("swiss"))
print(s)








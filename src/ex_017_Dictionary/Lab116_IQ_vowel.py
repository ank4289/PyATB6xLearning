input_string="hello world"


vowel="aeiou"

vowel_count=0
result=list()

for char in input_string:
    if char in vowel:
        vowel_count=vowel_count+1
        result.append(char)

print(vowel_count)
print(result)

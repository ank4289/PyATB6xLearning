ListString=["Ankit","","QA","Tester",""]

#filter_string=list(filter(None,ListString))
#print(filter_string)

def non_empty(x):
    if x != "":
        return True
    return None

fil_str=list(filter(non_empty,ListString))
print(fil_str)
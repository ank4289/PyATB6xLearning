student_info1 = {
    "name": "Pramod",
    "age": 35,
    "address": {
        "home_address": "Delhi",
        "office_address": "Noida"
    }
}

student_info2 = {
    "name": "Amit",
    "age": 69,
    "address": {
        "home_address": "Goa",
        "office_address": "KA"
    }
}

list_stu=[student_info1,student_info2]
print(list_stu)
print(list_stu[0])
print(list_stu[0]["name"])
print(list_stu[0]["address"]["home_address"])
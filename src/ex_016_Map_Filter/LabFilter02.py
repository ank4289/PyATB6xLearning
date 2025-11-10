Res=["Pass","Fail","Skip","Pass","Fail"]

def Pass_num(x):
    return x=="Pass"

#filter_pass=list(filter(Pass_num,Res))
filter_pass=list(filter(lambda x:x=="Pass",Res))
print(filter_pass)

list_student=[50,51,100]

def student(x):
    if x >50:
        return True

filter_student=list(filter(student,list_student))
print(filter_student)
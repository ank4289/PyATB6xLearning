s1=int(input("Enter side side 1"))
s2=int(input("Enter side side 2"))
s3=int(input("Enter side side 3"))


def check_classification(side1,side2,side3):
    if side1>0 and side2>0 and side3>0:
        if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
            if side1 == side2 == side3:
                return "equilateral"
            elif side1 == side2 or side2== side3 or side1== side3:
                return "isocleses"

            else:
                return "scalene"
        else:
                print("Not a triangle")
    else:
        print("Not a valid length")





result= check_classification(s1,s2,s3)
print(result)
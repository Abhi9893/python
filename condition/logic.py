#age =20
age = int(input("Enter your age: "))

if(age>34 and age<65): #or not
    print("you can work with us")
else:
    print("you cannot work with us")

a =50
b =10
if a!=b:
    print("pninfosys")
else:
    print("no")


a =200
b =33
c =500
if a > b and c >a:
    print("Both conditions are true")

a =200
b =33
c =500
if a > b or a > c:
    print("At least one of the conditions is True")
else:
    print("no")
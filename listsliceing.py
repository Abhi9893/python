# list_slicing.py

# pn =["vikas","ram","rohan","divya",4,True,40.5,23]
# 0,1,2,3,4      -1,-2,-3
#print(pn[0][3])
#print(pn[-4 : -1])
#print(pn[1][4])
#print(pn[0][1])
#print(pn[1:4])

#print(pn[1:])
#pn[0]="raj"
# print(pn[-1])
#print(pn[1:])
#print(pn[:3])
#print(pn)

# a=['apple','banana','cherry']
# b=a[1]
# print(b)
# a[1]="cherry"
# print(a)
# a[2]=b
# print(a)

# a=['apple','banana','cherry']
# a[1],a[2]=a[2],a[1]
# print(a)

#output = apple,cherry,banana

["FA2",95]
marks =["FA1",80,"FA2",85,"FA3",95]
report =marks[-4:]
#"FA2",85,"FA3",95
print(report)
report=report[:1]+marks[:5]
report=marks[2:3]+marks[-2]
report=marks[-4:-2]
report=report[:2]
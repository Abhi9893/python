# n=5

# for i in range(5):
#     #print("*" * (i+1))
#     print("*" * (i))

# n=3
# for i in range(3):
#     print(" " * (n-i-1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1))

rows =6
for row in range(1, rows):
    num =1
    for j in range(rows, 0,-1):
        if j > row:
            print(" ", end=' ')
        
        else:
            print("*",end=' ')
            num += 1
    print("")


# n=1
# for i in range(5):
#     print((n-1) * " " +i*'*')

# n=4
# for i in range(5):
#     print((n-i) * " " +i*'*')


# n = 5
# for i in range(0, n):
#     for j in range(0, i+1):
#         print("*",end=" ")
#     print(" ")

# n= 5
# for j in range(1, n+1):
#     print("*" * j)

# n = 5
# for i in range(n+1,0,-1):
#     for j in range(0, i-1):
#         print("*",end="")
#     print(" ")

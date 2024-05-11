# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))

# # for i in range(row):
#     for j in range(col):
#         print("*", end=" ")  # Use end=" " to print stars horizontally

#     print()  # Move to the next line after completing a row

# for i in range(1,row+1):
#         for j in range(1,col+1):
#             print(j,end=" ")
#         print()   

# row = int(input("Enter the number of rows: "))

row = int(input("Enter the number of rows: "))

# for i in range(1, row + 1):
#     for j in range(65, i + 65):
#         print(chr(j), end=" ")
#     print()


for i in range(1,row+1):
    print(" "*(row-i),end=" ")
    for j in range(1,2*i):
        print(j,end=" ")
    print()



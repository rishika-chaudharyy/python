eng=int(input("Enter english marks"))
math=int(input("Enter math marks"))
if eng>=80 and math>=80:
    print("A")
elif eng>=80 or math>=80:
    print("B")
else:
    print("C")
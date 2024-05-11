num=int(input("Enter a number"))

if num%15==0:
    print("Divisible by 15")
else:
    print("Number is not divisible by 15")
    if num%3==0 or num%5==0:
        print("Divisible by 3 or 5")
    else:
        print("Not divisible by 3 or 5")
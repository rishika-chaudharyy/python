cp=float(input("Enter the cost price"))
sp=float(input("Enter the selling price"))

if cp>sp:
    print("Loss of ",cp-sp)
elif cp<sp:
    print("Profit of ",sp-cp)
else:
    print("No profit or loss")
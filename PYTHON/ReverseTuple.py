color=("red","green","yellow","black","white","blue")
list=[]
for x in reversed(color):
    list.append(x)

new=tuple(list)
print(new)
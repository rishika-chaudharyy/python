color=("Red","Yellow","Green")#Creating tuple

#Single tuple item
#another way
fruit=tuple("apple")
my=("Pink",)
print(color,type(color))#checking type of it

#finding length
print(len(my))


#accessing items in tuple

print(color[0])

print(color[-1])

print(color[0:1])
print(color[-1:-2])

#check if item present

if "green" in color:
    print("Yes")
else:
    print("No")
#Traverse
    for i in color:
        print(i)

#concatenate
more=("orange",)
colors=color+more
print(colors)


#unpacking a tuple
color1,color2,color3,color4=colors
print(color1,color2,color3,color4)
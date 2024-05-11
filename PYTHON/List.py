fruit=["apple","mango","banana","cherry","pineapple","dragonfruit"]#create list


print(fruit,type(fruit))#print list and type of it
    

print(len(fruit))#print length of list

    
if "banana" in fruit:
    print("Yes")
else:
    print("No")
#Checking if an item is present or not
if "kiwi" not in fruit:
    print("Not present")
else:
    print("Present")


#accessing items in list 
print(fruit[1])
print(fruit[-5])
print(fruit[0:len(fruit)])
print(fruit[-1:])


#adding items in list
fruit.append("kiwi")#add at last
print(fruit)

fruit.insert(0,"kiwi")#add at particular index
print(fruit)

morefruit=["orange","peach"]#add another list to it
fruit.extend(morefruit)
print(fruit)

#removing items
fruit.remove("kiwi")#that item will get remove
print(fruit)

fruit.pop(1)
print(fruit)


#changing item into a list
fruit[1]="kiwi"
print(fruit)

fruit[1:3]=["papaya"]
print(fruit)


#sorting

fruit.sort()
print(fruit)
fruit.sort(reverse=True)
print(fruit)
fruit.reverse()
print(fruit)


#list comprehension
new_fruit = [fruits for fruits in fruit if "a" in fruits]
print(new_fruit)

#copy a list
new=fruit.copy()
print(new)

neww=fruit+new_fruit
print(neww)



#nested list
list=[10,20,[40,50]]
print(list)
print(list[2][0])
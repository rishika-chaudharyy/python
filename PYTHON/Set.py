set={"name","rishi","hiti","riti"}
print(set)

#length and type
print(len(set),type(set))

#accessing
for i in set:
    print(i)

#checking if item present or not
    if "name" in set:
        print("yes")

#add
set.add("Risji")
print(set)

#add a sequence
name={"hhe","uhuh"}
set.update(name)
print(set)

#removing
name.remove("hhe")#if not present throws error
print(name)


name.discard("ohoh")#does not throw error
print(name)

s1={1,2,3,4}
s2={5,6,7,8}
s3=s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

s1.intersection_update(s2)#keep only duplicates while joining
print(s1)

s1.symmetric_difference_update(s2)#keep non duplicates
print(s1)
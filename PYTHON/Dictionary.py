phones={"john":7899,"ria":7869}

print(phones,type(phones))
print(len(phones))

print(phones["john"])
print(phones.get("ria"))

print(phones.keys())
phones["john"]=7890
print(phones)

phones['kia']=980
print(phones)

more_ph={"shelly":9804}
phones.update(more_ph)
print(phones)

phones.pop("john")
print(phones)

phones.popitem()
print(phones)

#phones.clear()
#print(phones)


for x in phones:
    print(x)

for x in phones:
    print(phones[x])

for x,y in phones.items():
    print(x,y)

ph={"area" :{'x':9,'y':10}}
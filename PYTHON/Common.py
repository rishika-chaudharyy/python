l1=[1,5,5]
l2=[3,4,5,5,10]
l3=[5,5,10,20]
s1=set(l1)
s2=set(l2)
s3=set(l3)

s1s2=s1.intersection(s2)
final=s1s2.intersection(s3)

finallist=list(final)
print(finallist)

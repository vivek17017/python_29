"""
#Q1
l1=["apple",4,5,2,"mule"]
t1=tuple(l1)
print(t1)


#Q2
t1=tuple([int(e) for e in input("enter a list separated by comma").split(',')])[::-1]
print(t1)



t1=tuple([int(e) for e in input("enter a list separated by comma").split(',')])
sum=0
for e in t1:
    if e%2!=0:
        sum=sum+e
print(sum)




l1=["engine","air","east","and","mule"]
l2=sorted(l1)
l3=l2.startswith('a')





#Q5
t1=tuple([int(e) for e in input("Enter numbers separated by comma").split(',')])
print(t1)
sum=0
for e in t1:
    if e%2!=0:
        sum=sum+e
print(sum)






l1=['abac','baxd','aabb','ccaa','bgs','ccss']
t1=()
i=0
l1.sort()
for u in range(97,123):
    if l1[i][0]==chr(u):
        i+=1


l1=["apple",4,5,2,"mule"]
t1=tuple(l1)
print(t1)



l1=["engine","air","east","aman","ear","english","sandip","ashish","satya"]
l2=[]
l3=[chr(e) for e in range(97,123)]
for e in l3:
    t1=[]
    for i in l1:
        if i.startswith(e):
            t1.append(i)
    if t1!=[]:
        l2.append(tuple(t1))
print(l2)


Q4
l1=input("Enter alphabet separated by comma").split(",")
l3=[]
for e in l1:
    l2=[]
    l2.append(e)
    l2.append(ord(e))
    l3.append(tuple(l2))

print(l3)

#Q3
l1=["engine","air","east","aman","ear","english","sandip","ashish","satya"]
l2=[]
l3=[chr(e) for e in range(97,123)]
for e in l3:
    t1=[]
    for i in l1:
        if i.startswith(e):
            t1.append(i)
    if t1!=[]:
        l2.append(tuple(t1))
print(l2)
"""
#Q4
l1=input("Enter alphabet separated by comma").split(",")
l3=[]
for e in l1:
    l2=[]
    l2.append(e)
    l2.append(ord(e))
    l3.append(tuple(l2))

print(l3)
print("List Operation")
l=["Maharashtra","Delhi","Bihar","Uttar Pradesh","Andhra Pradesh","Arunachal Pradesh"]
print(l)
l.append("Punjab")
print(l)
l.insert(1,"Kerala")
print(l)
l.extend(["Tamil Nadu","Karnataka"])
print(l)
l.pop()
print(l)
l.remove("Kerala")
print(l)
del l[0]
for i in l:
    print(i)


print("Stack Operation")
l=[]
print(l)
l.append("Punjab")
print(l)
l.append("Rajasthan")
print(l)
l.append("Manipur")
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
# l.pop()  -- It will throw Error


print("Queue Operation")
l=[]
print(l)
l.append(49)
print(l)
l.append(52)
print(l)
l.append(37)
print(l)
l.append(6)
print(l)
l.append(18)
print(l)
l.pop(0)
print(l)
l.pop(0)
print(l)
l.pop(0)
print(l)
l.pop(0)
print(l)
l.pop(0)
print(l)
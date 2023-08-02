
# Access list

mylist=[1,2,3,4,5,6]
print(mylist[2:5])
print(mylist[1:6:2])
print(mylist[:-1])


# change list
mylist2=[1,2,3,4,5,6]
mylist2[2]=66
print(mylist2)
mylist2[2:6]=424,5646,868868,582975,428946
print(mylist2)

# add list
mylist3=[1,2,3,4,5,6]
mylist3.append("appended")
mylist3.insert(1,"inserted")
secondlist=['a','b','c','d','e']
mylist3.extend(secondlist)
print(mylist3)

# remove list
mylist4=["Yusof","Bozorg",'Nazir','Danish']
mylist4.remove("Yusof")
mylist4.pop(-1)
print(mylist4)
mylist4.clear()
print(mylist4)
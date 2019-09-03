from array import *;

array1= array('i',[5,2,3,4,5,6,7,8,9,0])
array1.insert(2,60)
array1.remove(0)
for x in array1 :
    print(x)

print("60 is at index: ")
print(array1.index(60))

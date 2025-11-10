#1.Create a tuple
my_tuple = (1,2,3,4,5)
print("Tuple:",my_tuple)

#2.Find the size of a tuple
my_tuple = (10,20,30,40)
print("Size of tuple:",len(my_tuple))

#3.Sort tuples
my_tuple = (5,2,8,1,3)
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted tuple:",sorted_tuple)

#4.Create a tuple with different data types
mixed_tuple = (1,"Hello",3.14,True)
print("Mixed tuple:",mixed_tuple)

#5.Unpack a tuple in several variables
tup = (10,20,30)
a,b,c = tup
print(a,b,c)

#6.Convert a tuple to a string
tup = ('P','y','t','h','o','n')
str1 = ''.join(tup)
print("string:",str1)

#7.Get 4th element and 4th element from last
tup = (10,20,30,40,50,60)
print("4th element:",tup[3])
print("4th from last:", tup[-4])

#8.Find the repeated items of a tuple
tup = (1,2,3,2,4,2,5)
repeated = [item for item in set(tup) if tup.count(item)>1]
print("Repeated items:", repeated)

#9.Check whether an element exists within a tuple
tup = (10,20,30,40)
print(20 in tup)
print(100 in tup)

#10.Convert a list into tuple
my_list = [1,2,3,4]
my_tuple = tuple(my_list)
print(my_tuple)

#11.Remove an item from a tuple
tup = (1,2,3,4,5)
tup_list = list(tup)
tup_list.remove(3)
tup = tuple(tup_list)
print(tup)

#12.Slice a tuple
tup = (10,20,30,40,50,60)
print("Sliced tuple:",tup[1:4])

#13.Find the index of an item
tup = (10,20,30,40)
print("Index of 30:",tup.index(30))

#14.Find the length of a tuple
tup = (1,2,3,4,5)
print("Length:",len(tup))

#15.Reverse a tuple
tup = (10,20,30,40)
reversed_tuple = tup[::-1]
print("Reversed tuple:", reversed_tuple)

#16.Convert a given string list to a tuple
str_list = ['apple','banana','cherry']
tup = tuple(str_list)
print("Tuple:",tup)
















#1.Reverse a given list
l = [100,200,300,400,500]
l.reverse()
print(l)

#2.Concatenate two lists
list1 = ["Hello","Madam"]
list2 = ["Dear","Sir"]
result = list1 + list2
print(result)

#3.Remove empty strings
list1 = ["Pen", "", "Pencil", "Eraser", "", "Scale"]
result = [item for item in list1 if item != ""]
print(result)

#4.Convert string to list
s = "Hello World"
list1= list(s)
print(list1)

#5.Check if a list contains an element
lst = [1,2,3,'a','b','c']
print('a' in lst)

#6.Remove all elements in list
lst = [10,20,30]
print(lst.clear())
print(lst)

#7.Count occurences of a specified object
pets = ["dog","cat","fish","fish","cat"]
print(pets.count("cat"))

#8.Return the length of a list
lst = [10,20,30,40]
print(len(lst))

#9.Insert a value at a specific index
lst = [1,2,3,4]
lst.insert(2,100)
print(lst)

#10.Clone or copy list
lst = [1,2,3]
copy_lst = lst.copy()
print(copy_lst)

#11.Extend a list without append
list1 = [1,2,3]
list2 = [4,5]
list1.extend(list2)
print(list1)

#12.Remove duplicates from a list
li = [3,2,2,1,1,1]
li = list(set(li))
print(li)

#13.Find the index of the 1st matching element
lst = [10,20,30,20,40]
print(lst.index(20))





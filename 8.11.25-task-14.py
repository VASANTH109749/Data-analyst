#1.Create a list
lst = [1,2,3,4,5]
print(lst)

#2.Length of list
lst = [1,2,3,4,5]
print(len(lst))

#3.Access elements
lst = [1,2,3,4,5]
print(lst[-1:-2:-1])
print(lst[2:3])

#4.Update the third element

numbers = [10,20,30,40]
numbers[2]=100
print(numbers)

#5.Delete an element using del
numbers = [10,20,30,40]
del numbers[1]
print(numbers)

#6.Append
numbers = [10,20,30,40]
numbers.append(50)
print(numbers)

#7.Insert
numbers = [1,2,3,5]
numbers.insert(3,4)
print(numbers)

#8.Remove an element using remove()
numbers = [1,2,3,5]
numbers.remove(5)
print(numbers)

#9.Remove the last element using pop function
numbers = [1,2,3,5]
numbers.pop()
print(numbers)

#10.Clear all elements using clear function
numbers = [1,2,3,5]
numbers.clear()
print(numbers)





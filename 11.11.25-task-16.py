#1.Create a list
fruits = ["Apple","Banana","Mango","Orange","Grapes"]
print(fruits)

#2.Add a new fruit to a list
fruits.append("pineapple")
print(fruits)

#3.Remove one fruit from the list
fruits.remove("Banana")
print(fruits)

#4.Number of fruits in list
print("Number of fruits:",len(fruits))

#5.Print fruits one by one
print("Fruits list:")
for fruit in fruits:
    print(fruit)

#6.Reverse the list and print it
fruits.reverse()
print("reversed list:",fruits)

#7.Sort the list alphabetically
fruits.sort()
print(fruits)

#8.Check if particular fruit in list
if "Apple" in fruits:
    print("Apple in the list")
else:
    print("Apple is not in the list")

#Tuple
#1.Create a tuple of 5 favorite colors
colors = ("Red","Blue","Green","Yellow","Purple")
print(colors)

#2.Print the first and last color
print("First color:",colors[0])
print("Last color:",colors[-1])

#3.Find the length of the tuple
print("Length of tuple:",len(colors))

#4.Count how many times a color appears
print("Count of blue:",colors.count("Blue"))

#5.Print all colors one by one using for loop
print("Colors:")
for color in colors:
    print(color)

#6.Combine two tuples
more_colors = ("Black", "White")
combined = colors + more_colors
print("Combined tuple:",combined)

#7.Find the maximum and minimum from a tuple of numbers
numbers = (10,45,3,78,21)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

#8.Try to change a value in the tuple
try:
    colors[0] = "Pink"
except TypeError:
    print("Error: Tuples are immutable.You cannot change their values.")

#Student Marks Analysis

students = [("Alice",(85,90,78)),("Bob",(75,80,82)),("Charlie",(95,88,92))]
#1.Print each students mark using nested loops
for student in students:
            name,marks = student
            print(f"{name}:",end="")
            for i, mark in enumerate(marks,start=1):
                        print(f"Subject{i}:{marks}",end="," if i < len(marks) else "")
            print()


#2.Calculate and print each students average marks:
            print("\nAverage Marks:")
            for student in students:
                name, marks = student
                average = sum(marks)/len(marks)
                print(f"{name}:{average:.2f}")

#3.Find the highest mark scored by each student
print("\nHighest marks:")
for student in students:
    name, marks = student
    print(f"{name}:{max(marks)}")

#4.Add a new student and repeat steps
students.append(("David",(88,76,90)))
print("\nAfter adding new student:\n")
                
for student in students:
            name,marks = student
            print(f"{name}:",end="")
            for i, mark in enumerate(marks,start=1):
                        print(f"Subject{i}:{marks}",end="," if i < len(marks) else "")
            print()

print("\nAverage Marks:(updated")
for student in students:
                name, marks = student
                average = sum(marks)/len(marks)
                print(f"{name}:{average:.2f}")            
    
print("\nHighest marks:(updated)")
for student in students:
    name, marks = student
    print(f"{name}:{max(marks)}")
    
#New task: Grocery store inventory
inventory = [["Fruits",["Apple","Banana","Mango"]],["Vegetables",["Carrot","Tomato","Spinach"]],["Dairy",["Milk","Cheese","Yogurt"]]]

#1.Print all categories and their items using nested loops
for category in inventory:
             print(f"Category: {category[0]}")
             for item in category[1]:
                 print("-",item)
             print()

#2.Add a new item Orange to the Fruits category
for category in inventory:
             if category[0] == "Fruits":
                 category[1].append("Orange")

#3.Remove spinach from vegetables
for category in inventory:
    if category[0] == "Vegetables" and "Spinach" in category[1]:
        category[1].remove("Spinach")

#4.Count how many times in each category
print("Item Count in Each Category:")
for category in inventory:
    print(f"{category[0]}:{len(category[1])} items")

#5.Print updated inventory
print("\nUpdated Inventory:")
for category in inventory:
    print(f"Category: {category[0]}")
    for item in category[1]:
        print("-", item)
    print()    
    
        

        
    

    












    

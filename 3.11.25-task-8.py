#1.Print numbers from 1 to 20
for i in range(1,21):
    print(i)

#2.Print all even numbers from 2 to 50
for i in range(2,51,2):
    print(i)

#3.Print all odd numbers from 1 to 50
for i in range(1,50,2):
    print(i)
#4.Print the square of numbers from 1 to 15
for i in range(1,16):
    print(i**2)
#5.Print the cube of numbers from 1 to 10
for i in range(1,11):
    print(i**3)   
#6.Print numbers from 10 down to 1 in reverse order
for i in range(10,0,-1):
    print(i)
#7.Print a multiplication table of 5
for i in range(1,11):
    print(f"5 x {i}={5*i}")

#8.Print all characters of a string one by one
s = "Python"
for char in s:
    print(char)

#9.Print numbers divisible by 3 between 1 and 30
for i in range(1,31):
    if i%3==0:
        print(i)
    

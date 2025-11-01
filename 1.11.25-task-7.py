#1.Create five variables of different data types
a="Hello World"
b=3.14
c=10
d=["hello","welcome",20]
e=("Hai","Hello",30)
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))

#2.Print a sentence using variables
name="John"
age=15
print(f"My name is {name} and my age is {age}.")

#3.Sum, Difference, product, quotient
x = 10
y = 5

print("Addition",x+y)
print("Subtraction",x-y)
print("Multiplication",x*y)
print("Division",x/y)

#4.Combine string and integer using f-string
name="Alice"
age = 20
print(f"{name} is {age} years old.")

#5.Arithmetic operators
num1 = 4
num2 = 3
a, b, c = 5, 7, 9

print("Square:",num1**2)
print("Cube:",num2**3)
print("Average:",(a+b+c)/3)

#6.Relational operators
a= 10
b= 20

print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#7.logical operators
num = 8
print(num>0 and num%2==0)
print(num<0 or num==0)

#8.Swap two variables
a=5
b=10
a,b=b,a
print("After swapping: a=",a,",b=",b)

#9.Compare two numbers
x=25
y=30
if x>y:
    print("x is greater")
elif x==y:
    print("Both are equal")
else:
    print("y is greater")

#10.Even or odd
num = int(input("Enter a number:"))
if num%2==0:
    print("Even number")
else:
    print("odd number")

#11.Positive, negative or zero
num = int(input("Enter a number:"))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")

#12.Grading system
marks = int(input("Enter the marks:"))
if marks>90:
    print("A grade")
elif marks>75:
    print("B grade")
elif marks>50:
    print("C grade")
else:
    print("Fail")

#13.leap year check
year = int(input("Enter the year:"))
if(year%400==0)or(year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")

#14.Voting eligibilty
age = int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#15.Largest of three numbers
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a>=b and a>=c:
    print("Largest number:",a)
elif b>=c:
    print("Largest number:",b)
else:
    print("Largest number:",c)

#16. Nested if- Positive, Even/Odd
num = int(input("Enter a number:"))
if num>0:
    if num%2==0:
        print("Positive and Even")
    else:
        print("Positive and odd")
else:
    print("Negative or Zero")

#17.Nested if-Age category
age = int(input("Enter age:"))
if age<13:
    print("Child")
else:
    if age<=19:
        print("Teen")
    elif age<=59:
        print("Adult")
    else:
        print("Senior Citizen")

#18.Vowel or Consonant
ch = input("Enter a single alphabet:").lower()
if ch in ['a','e','i','o','u']:
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet!")

#19.Three subject marks-Pass/fail/outstanding
m1 = int(input("Enter mark 1:"))
m2 = int(input("Enter mark 2:"))
m3 = int(input("Enter mark 3:"))

avg = (m1+m2+m3)/3
if m1>=40 and m2>=40 and m3>=40:
    print("Pass")
    if avg>=90:
        print("Outstanding")
else:
    print("Fail")



    
        
        
    
    
    
    
    











    
    












      

#1. Add two numbers
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print("Sum =",a+b)

#2. Subtract two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Difference =",a-b)

#3. Multiply two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Product =",a*b)

#4. Divide two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Quotient =",a/b)

#5. Find the remainder
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Remainder =",a%b)

#6. Square of the number
num = float(input("Enter the number: "))
print("Square =",num**2)

#7. Cube of the number
num = float(input("Enter the number: "))
print("Cube =",num**3)

#8. Average of three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
average = (a+b+c)/3
print("Average =",average)

#9. Swap two variables
a = input("Enter the first value:")
b = input("Enter the second value:")
temp = a
a = b
b = temp
print("After swapping: a=",a,", b =", b)

#10. Check Datatype
value = input("Enter any value:")
print("Datatype is:", type(value))

#11.Add Integer and Float
x = 10
y = 5.5
z = x+y
print("Result =",z,"| Datatype =",type(z))

#12. Simple Comparision
a= float(input("Enter the first number:"))
b= float(input("Enter the second number:"))
if a>b:
    print(a,"is greater than", b)
else:
    print(b,"is greater than or equal to",a)

#13.Check equal or not
a= float(input("Enter the first number:"))
b= float(input("Enter the second number:"))
if a==b:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")

#14. Find the total and average marks
m1= float(input("Enter marks of the subject1:"))
m2= float(input("Enter marks of the subject2:"))
m3= float(input("Enter marks of the subject3:"))
m4= float(input("Enter marks of the subject4:"))
m5= float(input("Enter marks of the subject5:"))
total= m1+m2+m3+m4+m5
average= total/5
print("Total marks",total)
print("Average marks",average)

#15.Convert hours to minutes

Hours = float(input("Enter hours:"))
minutes = Hours*60
print(Hours,"hours=",minutes,"minutes=")

#16.Calculate simple interest

P= float(input("Enter Principal:"))
N= float(input("Enter time(in years):"))
R= float(input("Enter rate of interest:"))
SI =P*N*R/100
print("Simple interest is", SI)

#17.Find the area of the rectangle

length = float(input("Enter the length:"))
Breadth = float(input("Enter the breadth:"))
area = length*Breadth
print("Area of rectangle:",area)

#18.Check the number positive or negative

num = float(input("Enter the number:"))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")

#19.Calculate total cost
cost= float(input("Cost of one item:"))
qty= int(input("Enter the number of items:"))
total_cost= cost*qty
print("Total cost=",total_cost)

#20.Small calculator
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)


    











    








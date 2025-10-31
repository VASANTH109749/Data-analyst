#1.Check whether a number is positive, negative or zero
num = float(input("Enter a number:"))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")

#2.Check a number is even or odd
num = int(input("Enter a number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

#3.Check if the person is eligible to vote(age>=18)

age = int(input("Enter the age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
#4.Check if the student is passed or failed based on marks
marks=float(input("Enter the marks:"))
if marks>=40:
    print("passed")
else:
    print("Failed")
    
#5.Find the largest of two numbers
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
if a>b:
    print("The largest number:",a)
else:
    print("The largest number:",b)
    
#6.Display grade A,B,C,D based on marks    
marks=float(input("Enter the marks:"))
if marks>=90:
    print("A grade")
elif marks>=75:
    print("B grade")
elif marks>=60:
    print("C grade")
elif marks>=40:
    print("D grade")
else:
    print("Fail")
#7.Print the day name based on number(1-7)
day = int(input("Enter the day number(1-7):"))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday")
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==5:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")
else:
    print("Invalid day number")
#8.Check whether a character is alphabet,digit or special character
ch =input("Enter a character:")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

#9.Find the largest among three numbers
a= float(input("Enter the first number:"))
b= float(input("Enter the second number:"))
c= float(input("Enter the third number:"))

if a>=b and a>=c:
    print("Largest number:",a)
elif b>=a and b>=c:
    print("Largest number:",b)
else:
    print("Largest number:",c)

#10.Display a message based on temperature
temp = int(input("Enter the temperature:")
if temp>35:
           print("Hot")
elif temp>25:
    print("Warm")
elif temp>15:
    print("Cold")
else:
    print("Cool")

#11.Check whether a number is positive and even using nested if
num = int(input("Enter a number:"))
if num>0:
    if num%2==0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    print("The number is positive number")

#12.Simulate a login system using nested if
username = input("Enter username:")
password = input("Enter password:")
if username=="admin":
    if password=="12345":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")

#13.Check if a person is eligible for a job
age = int(input("Enter your age:")
experience = input("Do you have experience? (yes/no):").lower()
          
if age>18:
          if experience == "yes":
          print("Eligible for job:")
          else:
              print("Not eligible-experience required")
else:
    print("Not eligible-must be above 18")

#14.Check whether the year is leap year or not
year = int(input("Enter a year:"))
if(year%4==0 and year%100!=0)or(year%400==0):
    print("Leap yaer")
else:
    print("Not leap year")

#15.Check whether a student qualifies for a scholarship
marks = float(input("Enter the marks:"))
attendance = float(input("Enter attendance percentage:"))
if marks>=85:
    if attendance>=90:
        print("Eligible for scholarship")
    else:
        print("Not eligible- attendance below 90%")
else:
    print("Not eligible-marks  below 85")
        
        
        
              
    
    








    



    
          







    
        

    







    
    
    
           
           
           
           
             







             
             
             




    


    
    







    
    








    


    
    









    
    

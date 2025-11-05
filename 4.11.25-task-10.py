#1.Print numbers from 10 down to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

#2.Find the sum of even digits in a number
num = int(input("Enter a number:"))
sum_even = 0

while num >0:
    digit = num %10
    if digit % 2 == 0:
        sum_even += digit
    num //= 10
print("Sum of even digits:",sum_even)

#3.Count how many digits are in a number

num = int(input("Enter a number:"))
count = 0

while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)

#4.Check if a number is a palindrome

num = int(input("Enter a number:"))
temp = num
rev = 0

while num >0:
    digit = num %10
    rev = rev *10 + digit
    num //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#5. Find the reverse of a number
num = int(input("Enter a number:"))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev *10 + digit
    num //= 10
print("Reversed number:", rev)

#6.Print the fibonacci series up to 100
a, b = 0, 1
while a<= 100:
    print(a)
    a, b = b, a+b

#7.Compute the power of a number manually
base = int(input("Enter base:"))
exp = int(input("Enter exponent:"))
result = 1

while exp > 0:
    result *= base
    exp -=1
print("Power=", result)

#8.Keep dividing a number by 2 until  it becomes less than 1
num = int(input("Enter a number:"))
count = 0
while num >= 1:
    num /= 2
    count += 1
print("Number of divisions:", count)

#9.Print the digits of a number from last to first

num = int(input("Enter a number:"))
while num>0:
    digit = num%10
    print(digit)
    num //= 10

#10.Compute the sum of squares of digits
num = int(input("Enter a number:"))
sum_sq = 0
while num >0:
    digit = num%10
    sum_sq += digit**2
    num //= 10
print("Sum of squares of digits:", sum_sq)    
    
    

    
    
    

    

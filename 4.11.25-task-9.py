#1.Print all numbers between 1 and 100 that are divisible by 6 but not by 9
for i in range(1,101):
    if i%6==0:
        if i%9!=0:
            print(i)

#2.Find the sum of all odd numbers from 1 to 50
Sum=0
for i in range(1,50):
    if i%2!=0:
        print(i)
    Sum=Sum+i
print(Sum)    

#3.Count how many numbers between 1 and 200 are divisible by both 4 and 6

count = 0
for i in range(1,201):
    if i%4==0 and i%6==0:
        count += 1
    
print(count)    

#4.Print the multiplication table of given number n(1-10)
n=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n} x {i}={n*i}")

#5.Find the factorial of a number
n = int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
    fact *= i
print("factorial:",fact)

#6.Print all prime numbers between 1 and 50

for num in range(2,51):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

#7.Calculate the sum of digits of a number using arithmetic only:
num = int(input("Enter a number:"))
sum_digits = 0
for i in str(num):
    sum_digits += int(i)
print("Sum of digits:",sum_digits)    
        
#8.Count how many numbers between 1-500 are perfect cubes
count = 0
for i in range(1,501):
    if round(i**(1/3))**3 == i:
        count += 1
print("Perfect cubes count:", count)

#9.Print the reverse of a number using arithmetic only
num = int(input("Enter a number:"))
rev = 0
while num >0:
    digit = num%10
    rev = rev*10+digit
    num//= 10
print("Reversed number:", rev)

#10.Print numbers from 1 to 100 but skip numbers ending with 5
for i in range(1,101):
    if i % 10 == 5:
        continue
    print(i)

    


        
    

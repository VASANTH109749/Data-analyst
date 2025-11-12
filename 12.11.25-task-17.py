#1.Prime numbers between 1 and 100
count = -0
print("Prime numbers between 1 and 100 are:")
for num in range(2,101):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
print("\nTotal primes =", count)

#2.Pyramid pattern
rows = 5
for i in range(1,rows+1):
    for s in range(rows-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()

#3.Electricity bill calculator

units = int(input("Enter units consumed:"))

if units<= 100:
    bill = units*1.5
elif units <= 200:
    bill = (100*1.5)+(units-100)*2.5
elif units <= 300:
    bill = (100*1.5)+(100*2.5)+(units-200)*4.0
else:
    bill = (100*1.5)+(100*2.5)+(100*4.0)+(units-300)*5.0

if bill > 1000:
    bill += bill*0.1
print("Total Bill:", bill)


#4.Diamond Star pattern

rows = 5
for i in range(1,rows+1):
    print(" "*(rows-i)+"*"*(2*i-1))
for i in range(rows-1,0,-1):
    print(" "*(rows-i)+"*"*(2*i-1))

#5.Multiplication table grid
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()

#6.Pascals triangle
n = int(input("Enter number of rows:"))
for i in range(n):
    print(" "*(n-i), end="")
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num = num *(i-j)//(j+1)
    print()
        
    

    

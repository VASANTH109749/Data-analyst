#1.Right triangle
for i in range(5):
    for j in range(1,5-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()    

#2.Left triangle
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    

#3.Print square
for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()

#4.Print 8
for i in range(7):
    if i == 0 or i == 3 or i == 6:
        print("*****")
    else:
        print("*   *")

#5.Hollow square
for i in range(5):
    for j in range(5):
        if i ==0 or i == 4 or j == 0 or j == 4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#6.Hollow right triangle
for i in range(1,6):
    for j in range(1,i+1):
        if j == 1 or j == i or i == 5:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

#7.Inverse left triangle
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end = " ")
    print()

#8.Inverse right triangle
for i in range(4,0,-1):
    for k in range(0,4-i):
        print(" ", end = " ")
    for j in range(1,i+1):
        print("*", end = " ")
    print()

#9.
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = " ")
    print()    

#10.
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#11.
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
         if j == 1 or j ==i or i == n:
             print(j,end=" ")
         else:
             print(" ",end=" ")
    print()        
    



    
    

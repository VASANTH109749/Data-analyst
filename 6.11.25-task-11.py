#1.Concatenate a string
str1 = "basket"
str2 = "ball"
print(str1+str2)

#2.Write a program to test if a given string contains the specified sequence of char values.
str = "Python"
print("y" in str)

#3.Convert to lower case
str = "PYTHON"
print(str.lower())

#4.Trim any leading or trailing whitespace from a given string
str = " Vasanth "
print(str.strip())

#5. Reverse a string
str = "Python"
print(str[::-1])

#6.How do you replace all spaces with underscore
str = "Hello World"
print(str.replace(" ","_"))

#7.Middle three characters
str = "Python123"
Mid = len(str)//2
result = str[Mid-1:Mid+2]
print(result)

#8 Convert first and last letter to capital
str = "python"
s =str[0].upper()+str[1:5]+str[5].upper()
print(s)

#9. Get length of string
str = "Python"
print(len(str))

#10.Count occurence of given string
s = "I am new to office but not new to profession"
print(s.count("new"))

#11.Remove digits from a string
s = "Python123is4fun"
result = "".join([i for i in s if not i.isdigit()])
print(result)

#12.Count the number of words
s ="The quick brown fox jumps"
print(len(s.split()))

#13.Replace a specified character
s = "The quick brown fox jumps over lazy dog"
print(s.replace("o","x"))

#14.Count vowels in a string
s = "Education"
vowels = "aeiouAEIOU"
count = sum(1 for i in s if i in vowels)
print(count)

#15.Check if string contains only whitespace
s = " "
print(s.isspace())

#16.Remove all digits from string
s = "abc123xyz"
print("".join([i for i in s if not i.isdigit()]))

#17.Find the length of name
name = "Vasanth"
print(len(name))

#18.Convert to uppercase
name = "Vasanth"
print(name.upper())

#19.Convert to lowercase
name = "Python"
print(name.lower())

#20.Count letter a
name = "Banana"
print(name.count("a"))

#21.Check if starts with hello
name = "Hello world"
print(name.startswith("Hello"))

#22.Check if ends with .com
name ="example@gmail.com"
print(name.endswith(".com"))

#23.Find the position of python
s = "I am learning python programming"
print(s.find("python"))

#24.Replace java with python
s = "I love java"
print(s.replace("java","python"))

#25.Remove spaces from both sides
s = "  Hello World "
print(s.strip())

#26.Capitalize first letter
s = "Python is fun"
print(s.capitalize())

#27.Split sentence into words
s ="Python is fun"
print(s.split())

#28.Join a list of words
s = ["Python","is","fun"]
print(" ".join(s))

#29.Only alphabets
s = "Python"
print(s.isalpha())

#30.Only digits
s = "12345"
print(s.isdigit())

#31.Letters and numbers
s = "Python3"
print(s.isalnum())

#32.all lowercase
s ="python"
print(s.islower())

#33.all uppercase
s = "PYTHON"
print(s.isupper())

#34.swapcase
s = "PytHoN"
print(s.swapcase())

#35.Convert each word first letter to uppercase
s = "python programming language"
print(s.title())

#36.Only spaces
s = " "
print(s.isspace())

#37.Palindrome check
s = "madam"
print("Palindrome" if s==s[::-1] else "Not Palindrome")

#38.Remove all digits
s = "abc123xyz"
print("".join([i for i in s if not i.isdigit()]))

#39.Replace spaces with underscores
s = "Python is fun"
print(s.replace(" ","_"))

#40.Extract only numbers
s = "abc123xyz456"
print("".join([i for i in s if i.isdigit()]))

#41 Words starting with capital letters
s = "Python Is A Great Language"
for word in s.split():
    if word[0].isupper():
        print(word)

#42.Count each letter occurence
s = "banana"
for ch in set(s):
    print(ch, "=", s.count(ch))

#43.Remove punctuation
import string
s = "Hello, world!"
print("".join(ch for ch in s if ch not in string.punctuation))

#44.Check email endswith @gmail.com
email = "example@gmail.com"
print(email.endswith("@gmail.com"))

#45 Reverse string without slicing
s = "Python"
rev = ""
for ch in s:
    rev = ch +rev
print(rev)    

    
        
        















































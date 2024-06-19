
#1. Write a program that takes two numbers as input and prints their sum.
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
sum=x+y
print("Sum of the 2 numbers is: ", sum)

#2. Write a python program that checks whether a given number is even or odd.
x=int(input("Enter a number: "))
if x%2==0:
    print("The number is even")
else:
    print("The number is odd")

#3. Write a python program that calculates the factorial of a given number.
num=int(input("Entwe number:"))
factorial = 1
if num < 0:
   print("Factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#4. Write a program that asks the user for their name and then prints a greeting message.
x=input("Enter name: ")
print("Hello ", x, "!")

#5. Write a program that takes a string input from the user and writes it to a text file.
data=input("Enter your data:")
f=open('myfile.txt','w')
f.write(data)
f.close()

#6. Write a program that reads the content of a text file and prints it to the console.
f=open('myfile.txt','r')
f_content=f.read()
print("File Content:\n", f_content)
f.close()


#7. Write a python program that takes a string as input and returns its length.
x=input("Enter a string: ")
print(len(x))

#8. Write a python program that takes a string as input and returns its length.
x=input("String1: ")
y=input("String2: ")
print(x + y)

#9. Write a python program that checks if a substring is present in a given string.
x=input("Enter a string: ")
y=input("Enter substring: ")
if y in x:
    print("The substring is present: ")
else:
    print("The substring is not present")

#10. Write a python program that converts a given string to uppercase.
x=input("Enter:")
print(x.upper())

#11. Write a python program that generates the first n numbers in the Fibonacci sequence.
def fibonacci_while(n):
    num1, num2 = 0, 1
    for _ in range(n):
        print(num1, end=" ")
        num1, num2 = num2, num1 + num2

n = int(input("Enter a number:"))
fibonacci_while(n)

#12. Write a python program that calculates the sum of the digits of a given number.
def getSum(n): 
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
n = int(input("Enter a number:"))
print(getSum(n))

#13. Write a program that asks the user for their birth year and calculates their age.
from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
 
    return age
     
print(calculateAge(date(1997, 2, 3)), "years")

#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
 def read_and_print_lines():
    lines = []
    print("Enter multiple lines of input (enter an empty line to finish):")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    print("\nYou entered:")
    for line in lines:
        print(line)

read_and_print_lines()

#15.Write a program that reads data from a CSV file and prints it to the console.
 
import csv
with open('f.csv', mode ='r')as file:  
csvFile = csv.reader(file)
for lines in csvFile:
    print(lines) 
file.close()

#16. Write a program in python that counts the frequency of each character in a string.
x=input("Enter a string:")
freq = {}
for i in x:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of all characters in GeeksforGeeks is :\n " + str(freq))

#17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
x=input("Enter:")
print(x.title())

#18. Write a python program that checks if two strings are anagrams of each other.
str1 = input("Enter str1:")
str2 = input("Enter str2:")
if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
if(sorted_str1 == sorted_str2):
    print(str1 + " and " + str2 + " are anagram.")
else:
    print(str1 + " and " + str2 + " are not anagram.")

#19. Write a python program that removes all punctuation from a given string.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter:")
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)

#20. Write a python program that takes a list of numbers and returns their sum.
def calculate_sum(numbers):
    return sum(numbers)
my_list = [1, 2, 3, 4, 5]
result = calculate_sum(my_list)
print(f"The sum of the list is: {result}")

#21. Write a python program that counts the occurrences of a specific element in a list.
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))

#22. Write a python program that returns the minimum and maximum values in a list of numbers.
x=[1,2,3,4,5,6]
print("Minimum number in the list:", min(x))
print("Maximum number in the list:", max(x))

#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
celsius=int(input("Enter temperature in celcius:"))
fahrenheit = (celsius * 1.8) + 32
print("The temperature in fahrenheit is:", fahrenheit)

#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
op=input("Enter an operator (+, -, *, /):")
if op == '+':
    print("Addition:", x+y)
if op == '*':
    print("Multiplication:", x*y)
if op == '-':
    print("Subtraction:", x-y)
if op == '/':
    print("Division:", x/y)

#25. Write a program that copies the contents of one text file to another.
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)

#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix():
    string = input("Enter the string: ")
    prefix = input("Enter the prefix to check: ")
    suffix = input("Enter the suffix to check: ")
    if string.startswith(prefix):
        print(f"The string starts with the prefix '{prefix}'.")
    else:
        print(f"The string does not start with the prefix '{prefix}'.")
    if string.endswith(suffix):
        print(f"The string ends with the suffix '{suffix}'.")
    else:
        print(f"The string does not end with the suffix '{suffix}'.")
check_prefix_suffix()

#27. Write a program in python that converts a string into a list of its characters.
s = "Hello World"
x = list(s) 
print(x) 

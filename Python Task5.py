#Question 1: Write a program in Python to allow the error of syntax to be handled using exception handling.
x = int(input("Enter a number : "))
y = int(input("Enter another number : "))
try:
    print(x/y)
except Exception:
    print("Number is not divisible")

#Question 2: Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError):
    print("An I/O error or a ValueError occurred")
except:
    print("An unexpected error occurred")
	

#Question 3: Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”
num = (input("Enter a single to four digit number : "))
y = len(num)
if y == 4:
    try:
        print(num)
    except ValueError:
        print ("The length is too short/long !!! Please provide only four digits”")
else:
        print("Try again")

#Question 4: Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
count = 0
while True:
    username = input("Enter the username ")
    password = input("Enter the password ")
    count +=1
    if count ==3:
        break
    else:
        if username == "Rachana" and password == "Consultadd":
            print("Welcome to the program")
        else:
            print("Wrong username and password")
			
#Question 5: Go through the link provided below to understand finally and raise concept:
#Went through the link and the concept. 

#Question 6: Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:
file1 = open("myfile.txt", "r+")
print (file1.read())

#Question 1: Write a program to reverse a string.
a = str(input("Enter a word: "))
length = len(a)
x=a[length: :-1]
print (x)

#Question2: Write a function that accepts a string and prints the number of uppercase letters and lowercase letters
a = str(input("Enter a word: "))
lowercase = 0
uppercase = 0
for i in a:
    if(i>= 'a' and i<= 'z'):
        lowercase = lowercase + 1
    elif(i>= 'A' and i<= 'Z'):
        uppercase = uppercase + 1
print('Lower case: ', lowercase)
print('Upper case: ', uppercase)

#Question 3: Create a function that takes a list and returns a new list with unique elements of the first list.
list1 =[1,2,3,4,5,1,2,3,7,8,9]
list2 =[]
for x in list1:
    if x not in list2:
        list2.append(x)
print(list2)

#Question 4: Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
a = (input("Enter a hyphen-sequence seperated sentence: "))
output = a.split("-")
output.sort()
print('-'.join(map(str, output)))


#Question 5: Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
a = (input("Enter a sentence: "))
Output = a.upper()
print(Output)


#Question 6:Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
a = (input("Enter a number : "))
b = (input("Enter another number : "))
sum = int(a) + int(b)
print(sum)

#Question 7: Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length, then the function should print both the strings line by line.
a = (input("Enter a word: "))
b = (input("Enter another word : "))
len1 = len(a)
len2 =len(b)
if len1 > len2:
    print(a)
else:
    print(a)
    print(b)

# Question 8: Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
list = []
for i in range(1, 21):
    list.append(i**2)

print(tuple(list))

#Question 9: Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers
a = int(input("Enter a number : "))
for i in range(0,a+1):
    if i%2 == 0:
        print("Even numbers", i)
    else:
        print("Odd numbers", i)

#Question 10: Write a program which which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
list1 = list(range(1,21))
even = lambda x: x%2==0
list2 = list(filter(even, list1))
print(list2)

#Question 11: Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
list = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, list))
print(evenNumbers)

#Question 12: Write a function to compute 5/0 and use try/except to catch the exceptions
try:
    x = 5 / 0
except:
    print("Error dividing by zero")

#Question 13: Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
import operator
from functools import reduce
mainlist = [1,2,3,4,5,6,7]
newlist = reduce(lambda a,b:a*10+b, mainlist)
print(newlist)

#Question 14: Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.Make sure to use only higher order functions
a = int(input("Enter the starting number : "))
b = int(input("Enter the ending number : "))
list1 =[]
for x in range(a, b+1):
    if(x%7==0) and (x%3!=0):
        list1.append(str(x))
print(','.join(list1))

#Question 15: Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.
def multiplication(x):
    return x * x
a = (1,2,3,4)
result = map(multiplication, a)
print(list(result))

#Question 16: What is the output of the following codes:
#16 i:
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
Output is 2

#16 ii
 def a():
    try:
        f(x,4)
    finally:
        print('after f')
        print('after f?')
    a() 
No output since the function is not defined.


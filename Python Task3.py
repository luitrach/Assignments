#Question 1: Create a list of 10 elements of four different data types like int, string, complex and float.
list =[1,2,"Task3", "3+2a", 2.2, "Rachana", "1+5a", 6, 7, 5.8]

#Question 2: Create a list of size 5 and execute the slicing structure
list = [2, 4, 6, 8, 10, 12]
print(list[1 : 5])

#Question 3: Write a program to get the sum and multiply of all the items in a given list.
#For Sum:
list1 = [1, 2, 3]
list2 = [2, 4, 6]
list3 =[]
for x in range(0, len(list1)):
    list3.append(list1[x] + list2[x])
print(list3)

#For Multiplication
list1 = [1, 2, 3]
list2 = [2, 4, 6]
list3 =[]
for x in range(0, len(list1)):
    list3.append(list1[x] * list2[x])
print(list3)

#Question 4: Find the largest and smallest number from a given list.
list = [2, 4, 7, 9, 14, 27, 42]
print(min(list))
print(max(list))

#Question 5: Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in list:
    if (x%2 == 0):
        list.remove(x)
print(list)

#Question 6: Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and 30 (both included).
list = []
for i in range(1, 31):
    list.append(i**2)
a = (list[:5])
b = (list[-5:])
a.append(b)
print(a)

# Question 7: Write a program to replace the last element in a list with another list.
list1 = [1,3,5,7,9,10]
list2 = [2,4,6,8]
list1[-1:] = list2
print(list1)

#Question 8: Create a new dictionary by concatenating the following two dictionaries:
a = {1:10,2:20}  
b = {3:30,4:40}
a.update(b)
print(a)

#Question 9:Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
a = int(input("Enter a number : "))
output = {}
for x in range(1, a+1):
    output[x] = x*x
print(output)

 #Question 10: Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string
a =(input("Enter some comma sepearted numbers : "))
list = a.split(',')
tuple = tuple(list)
print('Input: ',list)
print('Output: ',tuple)

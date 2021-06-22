#Question 1: Write a program in Python to find out the character in a string which is uppercase using list comprehension.
a = input("Enter a word: ")
print("Original string:" , a)
uppercase = [char for char in a if char.isupper()]
print("Uppercase characters: " +str(uppercase))

#Question 2: Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with their respective subjects.
student = ["Smit", "Jaya", "Rayyan"]
subject = ["CSE", "Networking", "Operating System"]
print ("Name of Students: " +str(student))
print ("Name of Subjects: " +str(subject))
output = dict(zip(student, subject))
print("Output: "+ str(output))

#Question 4. Write a program in Python using generators to reverse the string.

a = "Consultadd Training"
def reverse(a):
    str = ""
    for i in a:
        str = i + str
    return str

print("Original: ", a)
print("Reverse: ", reverse(a))

#Question 5: Write an example on decorators
#Decorators allows to modify the behavior of function or a class. Here is an example:
def create_addition(x): 
    def adder(y): 
        return x+y 
  
    return adder 
  
add_15 = create_addition(15) 
  
print(add_15(10)) 

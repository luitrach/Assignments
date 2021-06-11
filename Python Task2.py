#Task2- Question 1
a = int(input("Enter a number : "))
if (a%3==0 and a%5==0):
    print("Consultadd - Python Training")
elif (a%3==0):
    print("Consultadd")
elif (a%5==0):
    print("Python Training")
else:
    print("Invalid Number")
#Question 2- Part I
a = int(input("Enter a number from 1 to 5: "))
num1= int(input("Enter a number : "))
num2= int(input("Enter a number : "))
if (a== 1):
    print(num1 + num2)
elif (a== 2):
    print(num1 - num2)
elif (a== 3):
    print(num1 / num2)
elif (a== 4):
    print(num1 * num2)
elif(a==5):
    first= int(input("Enter another number : "))
    second= int(input("Enter another number : "))
    print((num1 + num2 + first + second)/4)


#Question 2-Part II
a = int(input("Enter a number from 1 to 5: "))
num1= int(input("Enter a number : "))
num2= int(input("Enter a number : "))
outcome = 0
if (a== 1): 
    outcome = (num1 + num2)
    print(outcome)
elif (a==2):
    outcome = (num1 - num2)
    print(outcome)  
elif (a== 3):
    outcome = (num1 / num2)
    print(outcome)  
elif (a== 4):
    outcome = (num1 * num2)
    print(outcome)
elif (a==5):
    first= int(input("Enter another number : "))
    second= int(input("Enter another number : "))
    outcome = ((num1 + num2 + first + second)/4)
    print(outcome)
if outcome < 0:
    print ("Negative")

#Question 3
a = 10
b = 20
c = 30
avg = ((a + b + c)/3)
print("Avg =", avg)
if avg > a and avg > b and avg > c:
    print("Avg is higher than a, b, c")
elif avg > a and avg > b:
    print ("Avg is higher than a, b")
elif avg > a and avg > c:
    print ("Avg is higher than a, c")
elif avg > b and avg > c:
    print ("Avg is higher than b, c")
elif avg > a:
    print ("Avg is just higher than a")
elif avg > b:
    print ("Avg is just higher than b")
elif avg > c:
    print ("Avg is just higher than c")


#Question 4
counter = 0
while counter >= 0:
    counter += 0
    a = (input("Enter a number : "))
    if int(a)>0:
        print ("Good Going")
        break
    else:
        print ("Its Over")

#Question 5
outcome = []
for i in range (2000, 3201):
    if i % 7 == 0 and i % 5!= 0:
        outcome.append(i)
print (outcome)

#Question 6
No output is generated, gives an error that the objects is not iterable.

#Question 7:
for i in range (0, 7):
    if (i == 3 or i == 6):
        continue
    print(i, end=' ')
#Question 8:
a = (input("Enter a string : "))
letterCount = digitCount = 0
for i in a:
    if i.isdigit():
        digitCount += 1
    elif i.isalpha():
        letterCount += 1
print("Letters ", letterCount)
print("Digits ", digitCount)

#Question 9, Part 1
lucky = 5
a = int(input("Guess the lucky number : "))
if a == lucky:
    print("Correct answer")
else:
    print ("Try again")
a = int(input("Guess the lucky number : "))

#Question 9, Part 2
lucky = 5
a = int(input("Guess the lucky number : "))
if a == lucky:
    print("Correct answer")
else:
    print ("Try again")
answer = input("Do you want to try again?")
if answer == "No":
    print("Game over")
else:
    a = int(input("Guess the lucky number : "))

#Question 10
counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 5:
       print ("Try again")
   else:
       print ("Good guess")
   counter = counter +1
else:
   print ("Game over")
 
#Question 11
counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 5:
       print ("Try again")
   else:
       print ("Good guess")
       break
   counter = counter +1
else:
   print ("Sorry but that was not very successful")
 

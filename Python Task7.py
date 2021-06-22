#Question 1: Write a program that calculates and prints the value according to the given formula
import math

numbers = input("Enter the number D: ")
numbers = numbers.split(',')

list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    list.append(Q)

print(list)

#Question 2: Define a class named Shape and its subclass Square. The Square class has an init function which takes length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default
class shape(object):
    def _init_(self):
        pass
    def area (self):
        return 0

class square(shape):
  length = int(input("Enter the length"))
  def _init_(self, length):
    shape._init_(self)
    self.length = length
  def area(self):
    return self.length*self.length
SquareArea = square()
print (SquareArea.area())


#Question 3: Create a class to find three elements that sum to zero from a set of n real numbers
def Numbers(a, n):
 
    found = False
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (a[i] + a[j] + a[k] == 0):
                    print(a[i], a[j], a[k])
                    found = True
    if (found == False):
        print(" not exist ")
a = [-25,-10,-7,-3,2,4,8,10]
n = len(a)
Numbers(a, n)


#Question 4: Create a Time class and initialize it with hours and minutes.Create a method addTime which should take two Time objects and add them. Create another method displayTime which should print the time.Also create a method displayMinute which should display the total minutes in the Time
class Time():

  def __init__(self, hours, mins):
    self.hours = hours
    self.mins = mins

  def addTime(t1, t2):
    t3 = Time(0,0)
    if t1.mins+t2.mins > 60:
      t3.hours = (t1.mins+t2.mins)//60
    t3.hours = t3.hours+t1.hours+t2.hours
    t3.mins = (t1.mins + t2.mins) % 60
    return t3

  def displayTime(self):
    print ("Time is",self.hours,"hours and",self.mins,"minutes.")

  def displayMinute(self):
    print ((self.hours*60)+self.mins)

a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()

#Question 5: Write a Person class with an instance variable “age” and a constructor that takes an integer as a parameter. The constructor must assign the integer value to the age variable after confirming the argument passed is not negative; if a negative argument is passed then the constructor should set age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance methods:
class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
          self.age = 0
          print('Age is not valid')
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age<13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
      self.age+=1
age = int(input("Enter the age: "))         
b = Person(age)  
b.amIOld()
for j in range(0, 3):
    b.yearPasses()       
b.amIOld()
print("")

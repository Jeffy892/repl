## Run Python Programs

# 1. Make a Python program that prints your name.
def printName():
    print('Jefferson Santiago')

printName()

# 2. Make a program that displays the lyrics of a song.
def printLyrics():
    print("""
    
    I think it’s time to put em in they place
    Ima have to set em straight
    You don’t know me
    you don’t know where I’m from 
    or what i had to do to get this plate
    Ay
    Let me paint a picture
    Everybody dissing
    Acting like it wasn’t cool to listen
    Now look at me
    Now look at me
    - Back Then feat. William $
    """)

printLyrics()

#############################################################################
#############################################################################

## Variables

# 1. Make a program that displays several numbers.
def printNumbers():
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)

printNumbers()

def sum1():
    print(64 + 32)

sum1()

def add(x, y):
    total = x + y
    return total

print(add(1,2))

#############################################################################
#############################################################################

## Strings
# 1. Make a program that displays your favourite actor/actress.
favoriteArtist = 'Robert Downy Jr.'
print(favoriteArtist)

# 2. Try to print the word „lucky‟ inside s.
s = "My lucky number is %d, what is yours?"
print(s[3:8])

# 3. Try to print the day, month, year in the form “Today is 2/2/2016”.
date = "Today is %d/%d/%d" % (3,15,2021)
print(date)

#############################################################################
#############################################################################

## String replace
# 1. Try the replace program
s = "This string will be replaced by another string"
# string replace is case sensitive
s = s.replace("String", "troll")
print(s)

# 2. Can a string be replaced twice?
# string replace will  replace all the words that matched the given pattern
s = s.replace("string", "troll")
print(s)

# 3. Does replace only work with words or also phrases?
# String replace can also replace phrases
s = s.replace("replaced by another", "changed to something")
print(s)

#############################################################################
#############################################################################

## String find
# 1. Find out if string find is case sensitive
# string is case sensitive
s = "This is a string String string text"
print(s.find("is a string"))

# 2. What if a query string appears twice in the string?
# string find returns the index of the first word that it finds.
s = "This is a string String string text"
print(s.find("string"))

# 3. Write a program that asks console input and searches for a query.
s = "Choose what words or phrases you want to find in this string"
print(s)
print("Word or Phrase you want to find")
match = input()
s = s.find(match)
print(s)

#############################################################################
#############################################################################

## String join

# 1. Create a list of words and join them, like the example above.
a = "This is "
b = "a string"
c = "that is joined"

print(a + b)
print(a + b + c)


# 2. Try changing the separator string from a space to an underscore.
d = a + b + c
d = d.split(" ")
d = '_'.join(d)
print(d)

#############################################################################
#############################################################################

## String SPlit

# 1. Can a string be split on multiple characters?
test = "Test"
t = [char for char in test]
print(t)

# 2. Can you split a string this string?:
words = "World,Earth,America,Canada"
wordlist = words.split(",")
print(wordlist)

# 3. Given an article, can you split it based on phrases?
def phrases(article):
    return article.split(".")

#############################################################################
#############################################################################

## Random Numbers

# 1. Make a program that creates a random number and stores it into x.
import random
from collections import Counter
x = random.random()
print(x)

# 2. Make a program that prints 3 random numbers.
print(random.random())
print(random.random())
print(random.random())

# 3. Create a program that generates 100 random numbers and find the frequency of each
number.
def randomFreq(n = 100):
    numbers = []
    for x in range(n):
        numbers.append(random.randint(0, 9999))
    res = dict(Counter(numbers))

    return res

x = randomFreq()

print(x)

#############################################################################
#############################################################################

## Keyboard input

# 1. Make a program that asks a phone number.
print("What is your phone number?")
number = input()
print("Your number is %s" % number)

# 2. Make a program that asks the users preferred programming language.
print("What is your preffered programming language?")
lang = input()
print("Your preferred language is %s" % lang)


#############################################################################
#############################################################################

## If statments
# 1. Make a program that asks the number between 1 and 10. If the number is out of range the
program should display “invalid number”.
num = int(input("Please enter a number from 1 to 10: "))
if num > 0 and num < 10:
    print("your num %d" % num)
else:
    print("invalid number")

# 2. Make a program that asks a password.
password = "test1234"

inputPass = input("Pleas enter your password: ")
if inputPass == password:
    print("Password matched")
else:
    print("Password did not match")

#############################################################################
#############################################################################

## For loops 
# 1. Make a program that lists the countries in the set
clist = ['Canada', 'USA', 'Mexico', 'Australia']
for country in clist:
    print(country)

# 2. Create a loop that counts from 0 to 100
for x in range(101):
    print(x)

# 3. Make a multiplication table using a loop
for x in range(1,10):
    for y in range(1,10):
        print(x*y)

# 4. Output the numbers 1 to 10 backwards using a loop
for x in range(10, 1, -1):
    print(x)

# 5. Create a loop that counts all even numbers to 10
count = 0
for x in range(10):
    if x % 2 == 0:
        count += 1
print("Total number of even: %d" % count)

# 6. Create a loop that sums the numbers from 100 to 200
total = 0
for x in range(100, 200):
    total += x
print("Sum of numbers from 100 to 200 is: %d" % total)

#############################################################################
#############################################################################

## While loops
clist = ['Canada', 'USA', 'Mexico', 'Australia']
i = 0
while(i < len(clist)):
    print(clist[i])
    i += 1
# 2. What‟s the difference between a while loop and a for loop?
# While loop only runs when the loop condition is true when the loop starts
# it will not run if the loop is not true

# 3. Can you sum numbers in a while loop? Yes
x = range(10)
i = 0
total = 0
while(i < len(x)):
    total += x[i]
    i += 1

print(total)

# 4. Can a for loop be used inside a while loop? Yes, it is called a nested loop

while(i < len(x)):
    total += x[i]
    for y in range(3):
        print("forloop in while loop")

print(total)

#############################################################################
#############################################################################

## Functions
mylist = [1,2,3,4,5]


# 1. Make a function that sums the list mylist
def sumMyList(mylist):
    total = 0
    for x in mylist:
        total += x
    
    return total

print(sumMyList(mylist))

# 2. Can functions be called inside a function? Yes

def func2():
    print("This is function2")

def func3():
    print("This function3")


def func():
    func2()
    print("This is func")
    func3()

func()

# 3. Can a function call itself? Yes

mylist = [1, 3, 5, 9, 10, 17, 20, 30]

# recursive binary search
def binarySearch(myList, number, start, end):
    if(end >= start):
        mid = start + (end - start)
        if myList[mid] == number:
            return mid
        elif myList[mid] > number:
            binarySearch(myList, number, mid-1, end)
        else:
            binarySearch(myList, number, start, mid+1)
    else:
        return -1
    
res = binarySearch(mylist, 30, 0, len(mylist)-1)
print(res)


# 4. Can variables defined in a function be used in another function? (hint: scope). No variables that is defined 

def func5():
    testvar = 'lets test this'
    print(testvar)

#print(testvar)

#############################################################################
#############################################################################

## List
# 1. Make a program that displays the states in the U.S.
states = [
    "Alabama",
    "Maine",
    "Pennsylvania",
    "Alaska",
    "Maryland",
    "Rhode Island",
    "Arizona",
    "Massachusetts",
    "South Carolina",
    "Arkansas",
    "Michigan",
    "South Dakota",
    "California",
    "Minnesota",
    "Tennessee",
    "Colorado",
    "Mississippi",
    "Texas",
    "Connecticut",
    "Missouri",
    "Utah",
    "Delaware",
    "Montana",
    "Vermont",
    "District of Columbia",
    "Nebraska",
    "Virginia",
    "Florida",
    "Nevada",
    "Washington",
    "Georgia",
    "New Hampshire",
    "West Virginia",
    "Hawaii",
    "New Jersey",
    "Wisconsin",
    "Idaho",
    "New Mexico",
    "Wyoming",
    "Illinois",
    "New York",
    "American Samoa",
    "Indiana",
    "North Carolina",
    "Guam",
    "Iowa",
    "North Dakota",
    "Northern Mariana Islands",
    "Kansas",
    "Ohio",
    "Palau",
    "Kentucky",
    "Oklahoma",
    "Puerto Rico",
    "Louisiana",
    "Oregon",
    "Virgin Islands"
]

for state in states:
    print(state)

# 2. Display all states starting with the letter M
for state in states:
    if state[0] == 'M':
        print(state)

#############################################################################
#############################################################################

## List operations
y = [6, 4, 2]

# 1. Given the list y add the items 12, 8, and 4.
print(y)
y.append(12)
y.append(8)
y.append(4)
print(y)

# 2. Change the 2nd item of the list to 3.
print(y)
y.pop(1)
y.insert(1, 3)
print(y)

#############################################################################
#############################################################################

## Sorting list
def el(item):
    return item[1]
x = [(3,6),(4,7),(5,9),(8,4),(3,1)]
print(x)
x.sort(key=el)
print(x)

#############################################################################
#############################################################################

## Range function
# 1. Create a list of one thousand numbers
numbers = range(1000)

# 2. Get the largest and smallest number from that list
max = max(numbers)
min = min(numbers)

print("Max: %d\nMin: %d" % (max, min))

# 3. Create two lists, an even and odd one.
even = []
odd = []
for x in numbers:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)

#############################################################################
#############################################################################

## Dictionary
# 1. Make a mapping from countries to country short codes
usStates = {
    "CA" : "California",
    "VA" : "Virginia",
    "TX" : "Texas",
    "NY" : "New York"
}

# 2. Print each item (key and value)
print("US State Code\tState")
for key in usStates:
    print("%s\t\t%s" % (key, usStates[key]))


#############################################################################
#############################################################################

## Read File

# 1. Read a file and number every line
filename = "read.txt"

with open(filename) as f: 
    content = f.readlines()

line_num = 1
for line in content:
    line = line.replace("\n"," ")
    print("%d. %s" % (line_num, line))
    line_num += 1

# 2. Find out what the program does if the file doesn‟t exist.
filename = "read.txt"
with open(filename) as f: 
    content = f.readlines()


# It creates an error that file does not exists
# Error: No Such file or directory: [filename]

# 3. What happens if you create a file with another user and try to open it?
# If the file's permission doesnt allow any other users to use that file
# python will spit out an error that the file cannot be opened due to lack of permissions


#############################################################################
#############################################################################

## Write File
# 1. Write the text “Take it easy" to a file
filename = "writer.txt"

f = open(filename, "a")

f.write("Take it easy\n")
f.write("open(\"text.txt\")")

f.close()


## Nested Loops

# 1. Given a tic-tac-toe board of 3x3, print every position
for x in range(1, 4):
    for y in range(1, 4):
        print(str(x) + "," + str(y))

# 2. Create a program where every person meets the other
person = [ "John", "Marissa", "Pete", "Dayton" ]

for person1 in person:
    for person2 in person:
        if person1 != person2:
            print(person1 + " meets with " + person2)

# If a normal for loop finishes in n steps O(n), how many steps has a nested loop? it will be n^2 or n^m where m is how many loops inside another loop

#############################################################################
#############################################################################

## Slices

# 1. Take a slice of the list below:
pizzas = ["Hawai","Pepperoni","Fromaggi","Napolitana","Diavoli"]

print(pizzas[3])
print(pizzas[1:2])

text = "Hello World"

print(text.split(" ")[1])

## Multiple Return

def multRet(a,b):
    return a, b, (a+b)

print(multRet(1,2))

def func_five():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    number = input("Enter your number: ")
    address = input("Enter your address: ")

    return first_name, last_name, age, number, address

print(func_five())

#############################################################################
#############################################################################

## Scope

# 1. Add a function reduce amount that changes the variable balance
bal = 10
def reduceAmount(x):
    global bal
    bal = bal - x
    reduceAmount(1)

print(bal)

def amount(x):
    locVar = 1

#print(locVar) #crash

#############################################################################
#############################################################################

## Time and date
# 1. Print the date in format year-month-day
import time
timenow = time.localtime(time.time())

year,month,day,hour,minute = timenow[0:5]
print(str(year) + "/" + str(month) + "/" + str(day))

## Try except

# 1. Can try-except be used to catch invalid keyboard input? Yes
try:
    x = float(input("Enter a number to divide by 10"))
    y = x / 10
    print(y)
except Exception:
    print("Invalid number!")

# 2. Can try-except catch the error if a file can‟t be opened? Yes

try: 
    filename = "reads.txt"

    with open(filename) as f: 
        content = f.readlines()
except Exception:
    print("Something went wrong!")

# When would you not use try-except?
# When you want your application to crash and not 

#############################################################################
#############################################################################

### OOP Classes

## Class
# 1. Can you have more than one class in a file? Yes in python you can add more than one classes
# 2. Can multiple objects be created from the same class? Yes you can create multiple classes from the same class, this is called inheritance
# 3. Can objects create classes? No, classes creates objects, because classes are the blueprints of creating the classes
# 4. Using the code above, create another object.
class Person:

    age = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.address = "123 Persia"
        self.type = "Human"

    def info(self): 
        print(self.first_name)
        print(self.last_name)
        print(self.type)

    def location(self):
        print(self.address)

    def changeAge(self,age):
        self.age = age
    
    def getAge(self):
        return self.age



me = Person("JEff", "Samoerset")
me.info()
me.location()

#############################################################################
#############################################################################

## Getter and Setter

# 1. Add a variable age and create a getter and setter
print(me.getAge())
me.changeAge(1)
print(me.getAge())


# 2. Why would you use getter and setter methods?
# So that the class can control its own variables (state). Encapsulation
# This protects class variables to be changed accidentally by others

#############################################################################
#############################################################################

## Modules

# 1. Import the math module and call the sin function
import math
print(math.sin(60))

# 2. Create your own module with the function snake()
import mymodule
mymodule.snake()

#############################################################################
#############################################################################

## Inheritance

# 1. Create a new class that inherits from the class App
class App:
    def start(self):
        print("super class")

class SideApp(App):
    def version(self):
        print("This is the side app")

class SideSideApp: 
    def hello(self):
        print("Hello there from Side Side App")

class SideSideSide: 
    def hello2(self):
        print("Hello there from Side Side Side App")


app = SideApp()
app.start()
app.version()

class SmallApp(SideSideApp, SideSideSide):
    def check(self):
        print("This is a Small App")

mapp = SmallApp()
mapp.hello()
mapp.hello2()
mapp.check()


#############################################################################
#############################################################################

## Static Method

# 1. Can a method inside a class be called without creating an object?
# Static Methods can be called even without an object being created.
class PC:
    @staticmethod
    def checkCPU():
        print("CPU is an Ryzen 9 5950x")

    
PC.checkCPU()

# 2. Why does not everybody like static methods? because you can call a method without an object being created.


#############################################################################
#############################################################################

## Iterable

# 1. What is an iterable?
# An iteratable is a Python object that can be used as a sequence. You can go to the next item of the sequence using the next() method.

digits = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }

iter = digits.keys()
print(iter)

# 2. Which types of data can be used with an iterable?
# maps, list, sets, strings, and dictionaries


## Class Methods
# 1. What is a classmethod?
# A class method is a method that is shared on all objects

# 2. How does a classmethod differ from a staticmethod?
# A classmethod will not be called when anobject is not created

## Multiple Inheritance
# 1. Do all programming languages support multiple inheritance?
# No some programming languages does not support multiple inheritance. One example is Java

# 2. Why would you not use multiple inheritance?
# It can couse ambiguity when you inherit a class from multiple parent classes

# 3. Is there a limit to the number of classes you can inherit from?
# no limit.

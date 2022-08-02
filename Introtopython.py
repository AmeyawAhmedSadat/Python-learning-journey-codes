# Trailing comma
import matplotlib

print('red', 'car')

# Leaving space between two strings
'red ' 'car'

# Leaving space between two strings with plus sign
print('red ' + 'car')

# Printing elements after each other with trailing comma
print(5, 3)

# Printing without the print command and expecting outcome to be in parethensis
5, 6, 7, 'car'

# LIST (To create a list we use square brackets)
Courses = ['Maths', 'Science', 'English', 'CompScience']
print(Courses)

# Checking out the length of values in our list
len(Courses)

# Printing individual values from our list. python always starts from 0 so if we
# have 4 elements then it will be from 0-3
print(Courses[0])  # Prints the first value in our list which is maths

# We could always grab the last element in our list by using -1, we call this method
# indexing
print(Courses[-1])  # This prints out Compscience

# We could also index more than 1 value
print(Courses[0:2])
# In this case the first index is included but the second is
# not, so it starts from index 0 to 1 thats why it returns only two variables.

# Specifying beginning index but not ending and vice versa (Slicing)
print(Courses[2:])
print(Courses[:3])  # will print index 0, 1, 2 but not index three itself

# Adding a new item to our list (append command)
Courses.append("Social")  # Add a new variable called social to our list
print(Courses)

# Adding a new item to a specific place in our list (insert command(index, 'itemname)
Courses.insert(3, 'French')
print(Courses)

# Adding multiple values to our list with extend
# Assuming we had a list 2 and wanted to add that to Courses...
course2 = ["Books", "Data Science"]
Courses.extend(course2)
print(Courses)

# SUMMARY - APPEND ADDS 1 VALUE TO THE LIST, INSERT ADDS 1 VALUE WITH A SPECIFIC
# LOCATION TO BE INSERTED, EXTEND CAN ADD MULTIPLE VALUES TO OUR LIST OR ADD
# ANOTHER LIST AS EACH INDIVIDUAL ITEM.

# REMOVING VALUES FROM OUR LIST
Courses.remove("French")
print(Courses)

Courses.pop(5)  # by default this remove the last value of our list unless we
# specify an index and if you save this pop as a variable, it returns the variable
# you popped, If specify specific index too it returns what was removed.

# Sorting (1. By reversing the order)
Courses.reverse()  # This starts from the last value
print(Courses)

Courses.sort()
print(Courses)

# Sorting numbers (sort automatically sort numbers from ascending order to desc)
numbers1 = [1, 3, 5, 2, 10, 4]
numbers1.sort()
print(numbers1)

# SORTING IN DESCENDING ORDER
numbers1.sort(reverse=True)
print(numbers1)

# Sorting without altering the original list
sorted(numbers1, reverse=True)

# Finding the index of a certain value (In other words printing the number of
# place of a specific number

print(Courses)
Courses.index("Data Science")  # This will return the number of place of Data science

# Checking if our list contains a certain value or not (we use in function)
print("Arts" in Courses)  # This will return false since there is no art in courses

# Looping and returning each value in our list and their index
for i, c in enumerate(Courses, start=1):
    print(i, c)  # enumerate is used when you want to return a variable and its
    # count.

# Joining all values in our list (similar to concatenate in excel) as one string
course_strg = '/'.join(Courses)
print(course_strg)  # returns /Data Science/English/Maths/Science/Social

# Spliting our combined one string with sepeartors. (Similar to spliting a
# concatenated string into diff columns in excel

newlist = course_strg.split('/')
print(newlist)  # This will return a  list which is seperated

type(course_strg)  # strg
type(newlist)  # list

# ===================================================================================
# TUPLES : Tuples are like list but they are immutable which means we can't modify
# them.

tuple1 = ('boy', 'girl', 'man', 'dog')
print(tuple1)

tuple1.remove("boy")  # This will give us error since tuples are not mutatable

# ==================================================================================

# Sets (Sets don't care about order and don't accept duplicate)
cs_score = {'biggies', 'dre', 'fft', 'cat'}
print(cs_score)

5 / 3
import sys

print(sys.version)
sys.float_info

# Escape backslash and n -- newline escape or newline

print("Boy is coming\n soon")  # escapes soon and send it to the nextline

# Backslash t is tab or more space
print("This will leave more\tSpace")

# Placing a backslah in a sting use double backslash
print("This will put a backslash\\ in the text")

# Second way of placing backslash in a string (use r infront of the string)
print(r"This will put a backslash \ in the text")
# ==================================================================================
# String Methods
A = "The boy is good"
A.upper()  # Changes all letters to upper case

# Replacing a word in a string
A.replace("boy", "girl")  # replaces boy with a gril

# Finding substring and returns the first output of the sequence of index number of
# that substring
A.find("boy")
A * 2

# Stride
# We can also input a stride value as follows, with the '2' indicating that we are
# selecting every second variable:
A[::2]  # returns every letter using seq of 2
A[0:6:2]

# Concatenate Strings
A + " in his school"
str(1) + str(1)

# TUPLES
# Tuples are ordered sequence. Tuples are written as comma seperated elements
# within parentheses
Rating = (1, 3, 4, 5, 6, 7, 9)
# Tuple can contain different types of data eg string, float, int etc
Rating2 = ("boy", 1, 4.2)
print(Rating2)
for i in enumerate(Rating2):
    print(i)

print(Rating + Rating2)
Rating = Rating2
Rating

# LIST
# Converting list into strings
list_new = "Hello, my name is ahmed".split()
print(list_new)

# Converting a list into a string
strg_new = " ".join(list_new)
print(strg_new)

# Aliasing
B = [4, 6, 7, 8, "boy"]
A = B
B[4] = "man"
print(A)  # A automatically changes as we changed any element in B since A and B
# are referencing the same list

# Cloning
H = [1, 5, 6, 7, 8, "boot"]

G = H[:]  # cloning H to get the same thing in H. G won't change if H changes
print(G)
H[3] = "banana"
print(H)  # this changes the third element to banana  but G doesn't change because
# its just a clone
print(G)
help(print)
help(G)

# adding multiple elements to our list as one element hence a list inside a list
G.append(["man", "goat", "meat"])
print(G)

G.extend(["man", "goat", "meat"])
print(G)

# Deleting an element from a list
G.remove("meat")  # uses element name
print(G)
del (G[4])  # uses index in deleting an element in a list
print(G)
G[6][2]

# =========================== STRING =============================================
# USING COUNT AND FIND TO RETURN INDEX AND NUMBER OF ELEMENTS IN OUR STRINGS
print(G.count("boot"))  # will return number of times boot  appeared

K = "Hello world"
print(K.find("world"))  # returns the index of the first element we are trying to
# find

# Concatenation
greeting = "Hello"
name = "Martin"

greeting + ', ' + name  # This returns Hello, martin with a space in between them.

# Using format and placeholder to format our strings instead on +
message = '{}, {}. welcome!'.format(greeting, name)
message

# Using f string formatting to concatenate
message = f'{greeting}, {name}. welcome!'  # this is the same as using format strings
message

# To find out all the methods or functions we can use on a variable we can use dir
print(dir(greeting))
print(help(str))  # To find out what a specific method or function does
help(str.format)
# ===================================================================================
# string formatting
person = {'names': 'Bright', 'age': 23}
Sentence = 'My name is' + person['names'] + 'I am' + str(person['age']) + 'years ' \
                                                                          'old. '
print(Sentence)

# FORMATTING NUMBERS USING FORMAT IN STRINGS
for z in range(1, 11):
    sentence = 'The value is {:02}'.format(z)
    print(sentence)

#  FORMATTING DECIMAL PLACES IN STRING
pi = 3.4321543
sentence1 = 'Pi is approximately {:.2f}'.format(pi)
print(sentence1)

ll = 24.5654565765
amount = 'Amount of the money is approximately {:.0f}'.format(ll)
print(amount)  # This will round the figures

# Adding comma to large numbers so that they are readable
ds = '1M is equal to {:,.2f}'.format(1000 ** 2)
print(ds)

# formatting dates
import datetime

mydatetime = datetime.datetime(2017, 9, 24, 12, 40, 35)
print(mydatetime)

datetoday = '{0: %b, %A, %Y}'.format(mydatetime)
print(datetoday)
type(datetoday)

dAY = '{0:%B, %d}, fell on {0:%A} and it was {0:%j} day of the year'.format(
    mydatetime)
print(dAY)
# ==================================================================================
# Integers and Floats
num = 3
print(type(num))

# Arithmetic operations
# Exponent: 2 ** 2 (2 exponent 2)
# Floor division: 2 // 3 (returns integer even if the results is a float)
# Module: 5 % 2 (5 MOD 2)

# FUNCTIONS
# round (for rounding numbers)
# abs (for making numbers absolute values

# Comparison functions
# equal to:               ==
# not equal to:           !=
# Greater than:           3>2
# Less than:              2<3
# Greater than or equal to: 3>=2
# less than or equal to: 3<= 2

num_1 = 3
num2 = 2
print(num2 == num_1)  # returns false since num2 is not equal to numb1

# Parsing strings to integers
num_1 = '100'
num_2 = '200'

mum1 = int(num_1)
num2 = int(num_2)
print(num2 + mum1)

# =================================================================================

# ====================== DICTIONARIES =============================================
# A dictionary consists of keys and values. It is helpful to compare a dictionary to
# a list.
# Instead of being indexed numerically like a list, dictionaries have keys.
# These keys are the keys that are used to access values within a dictionary.
# Dictionary helps to work with key value pairs
# dictionary contain a key and a value for a example in a dictionary, a key could
# be name and the value would be the exact name. The key is matched to the value
# by a colon
student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'Science']}
print(student['name'])  # This returns the value of the key name

# we can also  access the values of our dictionary with get method which doesn't
# return error even if the key doesn't exist
print(student.get('name'))  # This returns john

print(student.get('class'))  # This returns none since there is no key such as class

print(student.get('class', 'not found'))  # This returns not found since there is no
# key  such as class but returns not found as we specified

# Adding a new key to our dictionary
student['phone'] = '+233545932461'
print(student.get('phone', 'not found'))

# updating the whole dictionary
student.update({'name': 'Jame', 'age': 26, 'class': 'JHS 1'})
print(student)

# deleting a specific key in our dictionary
del (student['class'])
student.pop('age')

# Looping through our dictionary
print(len(student))  # checking the length of our dictionary
print(student.keys())  # print all keys in our dictionary
print(student.values())  # print all values in our dictionary
print(student.items())  # prints both keys and values pairs

# When looping through dictionary, we can use items function to return both key
# and values else it will return only keys

for key, value in student.items():
    print(key, value)

lk = ['bo', 'gj0', 'ggh']
lk.remove('ggh')

for i, index in enumerate(lk, start=1):
    print(i, index)

# Verifying if a key is found in a dictionary
'name' in student
'jame' in student  # returns false because jame is not a key in the dic

# Adding a new element to sets
#  set.add(element)

# Intersection of sets
# set1 & set 2

# Union of sets
# set1.union(set2)

# elements in set1 but not in set2
# set.difference(set2)

# ==================================================================================

# ====================== CONDITIONS AND BOOLEANS ===================================

language = 'Python'

if language == 'book':
    print('That is true')
elif language == 'python':
    print('Correct its python')
else:
    print('it is not equal to python')

# Boolean operations (and or , not)


user = 'Admins'
logged_in = True

if user == 'Admins' and logged_in:
    print('success')
else:
    print('try again later')

# ==================================================================================

# ============================= LOOPS AND ITERATION ================================

nums = [1, 2, 4, 5, 6, 8, 89]
for num in nums:
    print(num)

# USING BREAK IN LOOP WHICH STOPS WHEN A NUMBER IS FOUND
for num in nums:
    if num == 5:
        print('found!')
        break
    print(num)

# Using Continue to continue in the loop even after finding a number
for num in nums:
    if num == 5:
        print('found!')
        continue
    print(num)

# LOOP IN LOOP
for num in nums:
    for letter in 'abc':
        print(num, letter)

num22 = [2, 3, 1]
nums = [1, 2, 4, 5, 6, 8, 89]

# Using loop in loop to multiply more numbers
for num11 in num22:
    for num222 in nums:
        print(num11 * num222)
# Looping through a certain number of times
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)  # returns 1-10

# While loop which literate till a condition is a met
o = 0
while o < 10:
    print(o)
    o += 1

# Infinite loop till we get certain number
person = 0
while True:
    if person == 8:
        break
    print(person)
    person += 1

value = True
while value:
    if zx == 5:
        break
    print(zx)

while 1:
    if x == 5:
        break
    print(x)
    x += 1

# ==================================================================================

print(range(10, 15))

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squaress = []
i = 0
while (i < len(squares) and squares[i] == 'orange'):
    new_squaress.append(squares[i])
    i = i + 1
print(new_squaress)

# Creating a new list using while loop
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while (i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)


# ==================================================================================

# CREATING FUNCTIONS

def my_fun(greeting, name='You'):
    return '{}, {} my function'.format(greeting, name)


print(my_fun('hi'))

my_fun()


# By using function it helps you not to repeat yourself (DRY)

# setting default value in our function
def my_new(greeting, name='You'):
    return '{}, {} my function'.format(greeting, name)


print(my_new('hi', 'CM'))

# Creating a function and docstringing it
def mul(a, b):
    """
    multiply a and b
    """
    C = a * b;
    return C
# Try my function
mul(2,5)
help(mul)


def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"


x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# fUNCTION THAT WILL USE TUPLE AS ARGUMENTS, WE USE * args
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

# Functions that will take dictionary we use **kwargs or **args
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])


printDictionary(Country='Canada', Province='Ontario', City='Toronto')

#
# =================================================================================

# EXCEPTION HANDLING
# TRY EXCEPT STATEMENT
# potential code before try catch

try:
# code to try to execute
except:
# code to execute if there is an exception

# code that will still execute if there is an exception

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a / b
    print("Success a=", a)
except:
    print("There was an error")


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

# TRY EXCEPT ELSE
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)


# try except else finally
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

# =================================================================================

# =========================== OBJECT AND CLASSES ===================================
# cLASS consist of attributes and methods (functions) while objects has its own
# properties and behavior (methods) so a class is an object. For example a car is
# an object which has many properties such as name, color. it also perform
# specific functions which include increase speed, decrease speed, apply brakes etc.

class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o     # These are the attributes of the class

    def work_do(self):
        if self.occupation =="tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoot movie")   # These are the functions



Tom = Human("Tom cruise","actor")
Tom.work_do()


# Import the library

import matplotlib.pyplot as plt

class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

        # Method

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

RedCircle = Circle(10, 'red')

RedCircle.radius = 1
RedCircle.radius

RedCircle.drawCircle()

# Test analysis

class analysedText(object):

    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?',
                                                                       '').replace(
            ',', '')

        # make text lowercase
        formattedText = formattedText.lower()

        print(formattedText)

        self.fmtText = formattedText



    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList):  # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0


text = analysedText("The boy, that came here is a good boy. Boy had mum.")
text.freqAll()
text.freqOf("boy")

##################################################################################

# MORE EXAMPLES OF CLASSES AND INSTANCES

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# cLASS Static method
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
##################################################################################
# CLASS METHOD
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
############################## STATIC METHOD #######################################
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

# functions contain arguments/ args
# a parameter is the variable listed in the brackets
# an arg is the value that is sent to the function
# when it is called

#this function does something, not excactly
#sure what but something

def my_function(fname, lname):
    fname = 'Simone'
    lname = 'Goldman'

    for x in fname, lname:
        print(fname + ' ' + lname)
        break
my_function('', '')

'''
If you do not know how many arguments that will
be passed into your function, add a * before the
parameter name in the function definition.
This way the function will receive a tuple of
arguments, and can access the items accordingly
'''

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

'''
keyword arguments (or kwargs):
You can also send arguments
with the key = value syntax.
This way the order of the arguments does not matter
'''

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



'''
If you do not know how many keyword arguments
that will be passed into your function, add two
asterisk: ** before the parameter name in the
function definition.
This way the function will receive a dictionary
of arguments, and can access the items accordingly
'''

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")









class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def func(self):
        print('Hi my name is ' + self.name + ', ' + str(self.age))
p1 = Person('Jeff',12)
p1.func()
p1.age = 20
p1.func()
#del p1.age #delete object property, age
#del p1 #deletes entire object

#class definitions cannot be empty, but if you for
#some reason have a class definition with no content
#put in the pass statement to avoid getting an error
class Person:
    pass

##
#call stacks, similar to a meandering convo

'''
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')
a()
'''
#a variable can only be local or global, not both
# more on local and global here
#https://automatetheboringstuff.com/2e/chapter3/#calibre_link-1213

#GLOBAL/LOCAL RULES
#1. if a variable is being used in global scope
#    ie outside of all functions, then its global
#2. if there is a global statment for that variable
#    in a function, then its global
#3. Otherwise, if vzriable used in statement in func
#    it is local
#4. If variable not used in assignment statement,
#   it is global
#note
def spam():
    global eggs
    eggs = 'spam' #global

def bacon():
    eggs = 'bacon' #local

def ham():
    print(eggs) #global

eggs = 42 #global
spam()
print(eggs)

#modify value stored in global, use global
#statement on that variable

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))



'''
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
'''
import sys
number = int(input())
def collatz(number):
    while number != 1:
        if number%2 == 0:
            number = number//2
            print(number)
            if number == 1:
                sys.exit()
        if number%2 !=0:
            number = 3*number+1
            print(number)
            if number ==1:
                sys.exit()
collatz(number)

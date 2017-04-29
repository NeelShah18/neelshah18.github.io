---
layout: post
title: OOP with Python
---

* History: Many computer scientists and programmers consider OOP to be a modern programming paradigm, the roots go back to 1960s. The first programming language to use objects was Simula 67. As the name implies, Simula 67 was introduced in the year 1967. A major breakthrough for object-oriented programming came with the programming language Smalltalk in the 1970s.

#### Following two concept is explain everything the use of OOPs.

1. Duplicate code is a Bad.

2. Code will always be changed.

#### Object-Oriented Programming has the following advantages:

* OOP provides a clear modular structure for programs which makes it good for defining abstract datatypes where implementation details are hidden and the unit has a clearly defined interface.
* OOP makes it easy to maintain and modify existing code as new objects can be created with small differences to existing ones.
* OOP provides a good framework for code libraries where supplied software components can be easily adapted and modified by the programmer. This is particularly useful for developing graphical user interfaces.

#### Terminology:

* **Class**: A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

* **Class variable**: A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.

* **Data member**: A class variable or instance variable that holds data associated with a class and its objects.

* **Instance variable**: A variable that is defined inside a method and belongs only to the current instance of a class.

* **Inheritance**: The transfer of the characteristics of a class to other classes that are derived from it.

* **Instance**: An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

* **Method**: A special kind of function that is defined in a class definition.

* **Object**: A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.

* **Function overloading**: The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.

#### Everything in class is python:
Even though we haven't talked about classes and object orientation in previous chapters, we have worked with classes all the time. In fact, everything is a class in Python.


```python
import math

x = 4
print(type(x))

def f(x):
    return x+1
print(type(f))
print(type(math))
'''As you can see, everything in python is class.'''
```

    <class 'int'>
    <class 'function'>
    <class 'module'>





    'As you can see, everything in python is class.'




```python
# Creating Classes

class Robot:
    pass

if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)
    print(y == x)
```

    True
    False



```python
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

neel = Customer(neel, 500)
print(neel.deposit(200))
print(neel.withdraw(150))

'''This is basic example of class in python with __init__, methods'''
```

    700
    550





    'This is basic example of class in python with __init__, methods'



The first method __init__() is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.

You declare other class methods like normal functions with the exception that the first argument to each method is self. Python adds the self argument to the list for you; you do not need to include it when you call the methods.

So what's with that self parameter to all of the Customer methods? What is it? Why, it's the instance, of course! Put another way, a method like withdraw defines the instructions for withdrawing money from some abstract customer's account. Calling jeff.withdraw(100.0) puts those instructions to use on the jeff instance.


```python
# one more example

class Robot:

    def __init__(self, name=None):
        self.name = name   

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")


x = Robot()
x.say_hi()
y = Robot("Marvin")
y.say_hi()
```

    Hi, I am a robot without a name
    Hi, I am Marvin


#### Public- Protected- and Private Attributes

Python uses a special naming scheme for attributes to control the accessibility of the attributes. So far, we have used attribute names, which can be freely used inside or outside of a class definition, as we have seen. This corresponds to public attributes of course.

There are two ways to restrict the access to class attributes:

* First, we can prefix an attribute name with a leading underscore "_". This marks the attribute as protected. It tells users of the class not to use this attribute unless, somebody writes a subclass. We will learn about inheritance and subclassing in the next chapter of our tutorial.

* Second, we can prefix an attribute name with two leading underscores "__". The attribute is now inaccessible and invisible from outside. It's neither possible to read nor write to those attributes except inside of the class definition itself.5

1) name--> Public--> These attributes can be freely used inside or outside of a class definition.

2) _name--> Protected--> Protected attributes should not be used outside of the class definition, unless inside of a subclass definition.

3) __name--> Private--> This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.


```python
# Attribute accessibility example
class A():

    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

x = A()
print(x.pub)
print(x.pub + " and my value can be changed")
print(x._prot)
x.__priv
```

    I am public
    I am public and my value can be changed
    I am protected



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-15-7b9b44920b69> in <module>()
         11 print(x.pub + " and my value can be changed")
         12 print(x._prot)
    ---> 13 x.__priv


    AttributeError: 'A' object has no attribute '__priv'


The error message is very interesting. One might have expected a message like "__priv is private". We get the message "AttributeError: 'A' object has no attribute '__priv'" instead, which looks like a "lie". There is such an attribute, but we are told that there isn't. This is perfect information hiding. Telling a user that an attribute name is private, means that we make some information visible, i.e. the existence or non-existence of a private variable.

#### Destructor:

What we said about constructors holds true for destructors as well. There is no "real" destructor, but something similar, i.e. the method __del__. It is called when the instance is about to be destroyed and if there is no other reference to this instance. If a base class has a __del__() method, the derived class's __del__() method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance.

***The destructor was called after the program ended, not when ft went out of scope inside make_foo.***



```python
class FooType(object):
    id = 0
    def __init__(self, id):
        self.id = id
        print(self.id, 'born')

    def __del__(self):
        print(self.id, 'died')


ft = FooType(1)
```

    1 born
    1 died


#### Inheritance

One of the major benefits of object oriented programming is reuse of code and one of the ways this is achieved is through the inheritance mechanism. Inheritance can be best imagined as implementing a type and subtype relationship between classes.

Suppose you want to write a program which has to keep track of the teachers and students in a college. They have some common characteristics such as name, age and address. They also have specific characteristics such as salary, courses and leaves for teachers and, marks and fees for students.

You can create two independent classes for each type and process them but adding a new common characteristic would mean adding to both of these independent classes. This quickly becomes unwieldy.



```python
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mr. Neel', 24, 30000)
s = Student('Mr. Water', 20, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
```

    (Initialized SchoolMember: Mr. Neel)
    (Initialized Teacher: Mr. Neel)
    (Initialized SchoolMember: Mr. Water)
    (Initialized Student: Mr. Water)

    Name:"Mr. Neel" Age:"24" Salary: "30000"
    Name:"Mr. Water" Age:"20" Marks: "75"


#### Polymorphism

In a child class we can change how some methods work whilst keeping the same name. We call this polymorphism or overriding and it is useful because we do not want to keep introducing new method names for functionality that is pretty similar in each class.




```python
class A():

    def __init__(self):
        self.__x = 1

    def message(self):
        print("message from A")


class B(A):

    def __init__(self):
        self.__y = 1

    def message(self):
        print("message from B")

try_1 = A()
try_1.message()

try_2 = B()
try_2.message()
```

    message from A
    message from B


**This is the end of the OOP concept.
Hope you like it and not bored!**

You can download all material from github account or website.

1) [Website: neelshah18.github.io](https://neelshah18.github.io/OOP-with-python.html)

2) [GitHub: neelshah18](https://github.com/NeelShah18/OOP-with-python)

**References:**

1) http://www.python-course.eu/object_oriented_programming.php

2) http://thepythonguru.com/python-inheritance-and-polymorphism/

3) https://pythonschool.net/oop/inheritance-and-polymorphism/

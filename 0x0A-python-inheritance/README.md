# 0x0A. Python - Inheritance
## ``` Python, OOP, Inheritance ```
## Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

## Requirements
## Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
## Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation ```(python3 -c 'print(__import__("my_module").__doc__)')```
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
## Documentation
Do not use the words import or from inside your comments, the checker will think you try to import some modules
## Files
|             File               |             Description                  |
|--------------------------------| ---------------------------------------- |
|**0-lookup.py**| function that returns the list of available attributes and methods of an object:
|**1-my_list.py, tests/1-my_list.txt**| Write a class MyList that inherits from list
|**2-is_same_class.py**| Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
|**3-is_kind_of_class.py**| unction that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
|**4-inherits_from.py**| function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise Fals
|**5-base_geometry.py**| Write an empty class BaseGeometry.
|**6-base_geometry.py**| Public instance method: def area(self): that raises an Exception with the message area() is not implemented into the class BaseGeometry
|**7-base_geometry.py, tests/7-base_geometry.txt**| adding Public instance method: def integer_validator(self, name, value): that validates value: you can assume name is always a string if value is not an integer: raise a TypeError exception, with the message <name> must be an integer if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0. Into the class BaseGeometry
|**8-rectangle.py**| rite a class Rectangle that inherits from BaseGeometry Instantiation with width and height: def __init__(self, width, height): width and height must be private. No getter or setter width and height must be positive integers, validated by integer_validator
|**9-rectangle.py**| adding the area() method must be implemented print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height> to the class Rectangle
|**10-square.py**| Write a class Square that inherits from Rectangle Instantiation with size: def __init__(self, size) size must be private. No getter or setter size must be a positive integer, validated by integer_validator the area() method must be implemented
|**11-saquare.py**| adding print() should print, and str() should return, the square description: [Square] <width>/<height> to the class square
|**100-my_int.py**| Write a class MyInt that inherits from int: MyInt is a rebel. MyInt has == and != operators inverted

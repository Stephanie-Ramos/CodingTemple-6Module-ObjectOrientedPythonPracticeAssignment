# Object-Oriented Python Practice Assignmnet

## Description

This project is a Python-based Student Management System created to demonstrate the use of object-oriented programming and Python data structures. The program stores student information, manages grades, and performs various operations using lists, dictionaries, sets, tuples, functions, exception handling, and regular expressions.

## Features

### Part 1: Class Definition

* Created a `Student` class.
* Added the following attributes:

  * `name`
  * `email`
  * `grades`
* Implemented methods:

  * `add_grade()`
  * `average_grade()`
  * `display_info()`

### Part 2: Working with Objects

* Created three student objects.
* Assigned initial grades.
* Added two additional grades to each student.
* Displayed student information and average grades.

### Part 3: Dictionary and Set Integration

* Created a dictionary that maps student emails to `Student` objects.
* Implemented a `get_student_by_email()` function using `.get()`.
* Created a set containing all unique grades across all students.

### Part 4: Tuple Practice

* Added a `grades_tuple()` method to the `Student` class.
* Converted grades into tuples.
* Demonstrated tuple immutability using exception handling.

### Part 5: List Operations

* Removed the last grade from each student's grade list using `.pop()`.
* Printed the first and last grades.
* Displayed the number of grades using `len()`.

### Part 6: Bonus Features

* Validated student email addresses using regular expressions.
* Counted the number of grades above 90 across all students.

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Lists
* Dictionaries
* Sets
* Tuples
* Regular Expressions (`re` module)

## Learning Objectives

This project demonstrates:

* Creating and using classes and objects
* Working with lists, dictionaries, sets, and tuples
* Using loops and functions
* Exception handling with `try` and `except`
* Data validation with regular expressions
* Basic data management techniques in Python

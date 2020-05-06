---
author: Cory Taylor
title: Functions and Classes
date: May 6, 2020
---

# Functions and Classes

---

## Goals of the Lesson

1. Define and call a named function
2. Read and identify different parts of a class definition
3. Instantiate a class, access properties, and call methods

---

## Lesson Overview

1. Functions
   1. Terminology
   2. Defining functions
   3. Calling functions
2. Classes
   1. Terminology
   2. Class definitions
   3. Instantiating and using classes

---

# Functions

---

## Function Terminology

* _Function_:
  1. A block of code
  2. That does something with data
* _Named function_: A function that is defined with the keyword `def`
* _Argument_ or _parameter_: Data that is passed into a function
* _Return value_:
  1. The result of a function
  2. Denoted by keyword `return`

---

## Defining Functions (0)

* Heads up: some examples here use basic math. Addition and multiplication, mostly.
* Why? Because arithmetic is easy to type!
* Functions can be any code, not just math.

---

## Defining Functions (1)

No arguments, no return value

```python
def greet():
    print('Hello!')


foo = greet()
# Hello!

foo
# None
```

---

## Building Blocks of Function Def'n

```python
  def greet( ) :
# [1]  [2] [3] [4]
```

1. Keyword `def`--signals that we're *def*ining a function
2. Function name
3. Argument list
4. Colon

---

## Defining Functions (2)

One argument and a return value

```python
def increment(x):
    return x + 1


foo = increment(3)
foo
# 4
```

---

## Function Exercise 1

* Write a function called `double(x)`.
* It should return `x * 2`.
* Use `increment(x)` as a model.

```python
def double(x):
    return x * 2

def other_double(x):
    _doubled = x * 2
    return _doubled
```

---

## Function Exercise 2

* Write a function called `add(x, y)`.
* It should return `x + y`.
* Use `increment(x)` as a model.

```python
def add(x, y):
    return x + y

# Why doesn't this work?
def add(x):
    return x + y
```

---

## Defining Functions (3)

Arguments with default values

```python
def make_greeting(name='world'):
    return 'Hello, ' + name + '!'


# Look ma, no arguments!
foo = make_greeting()
foo  # 'Hello, world!'

bar = make_greeting("y'all")
bar  # "Hello, y'all!"
```

---

## Function Exercise 3

* Rewrite `make_greeting(name)` to `make_greeting(greeting, name)`.
* Give default values for `greeting` and `name`.
* Return `greeting + ', ' + name + '!'`.

---

# Calling Functions

---

## Zero Arguments

Call a zero-argument function the way you'd expect: its name and empty parentheses

```python
def four():
    return 4


foo = four()
foo
# 4
```

---

## Positional Arguments (Args)

* _Positional arguments_: Supplying arguments in the order they appear in a function definition

```python
def concat_3(a, b, c):
    return a + b + c


foo = concat_3('1', '2', '3')
foo
# '123'
```

---

## Keyword Arguments (Kwargs)

* _Keyword arguments_: Supplying arguments by name
* Lets you supply arguments out of order

```python
def concat_3(a, b, c):
    return a + b + c


foo = concat_3(c='1', a='2', b='3')
foo
# '231'
```

---

## Mixing Args and Kwargs

* Supply positional arguments first, then keyword arguments.
* Valid:

    ```python
    concat_3('1', c='3', b='2')
    # '123'
    ```

* Invalid:

    ```python
    concat_3(a='1', '2', '3')
    ```

---

# Classes

---

## Class Terminology (1)

* _Class_:
  * A container for variables and functions
  * Useful for modeling the real world
* _Class definition_: Blueprint Python follows when building a class instance
* _Class instance_: If a definition is the blueprint, then an instance is the house.

---

## Class Terminology (2)

* _Property_: Variables stored in a class
* _Method_: Functions stored in a class
* _Dunder method_: Special methods that start with two underscores (*d*ouble *under*score)
* _Constructor_:
  * The general contractor that builds a house based on its blueprints
  * In Python, a dunder method called `__init__()`

---

## Concrete Example: Ziploc Bags

* Key properties that make Ziplocs useful:
  * Size
  * Contents
  * Whether they're open or closed
* Key actions:
  * Opening bag
  * Closing bag
  * Getting the contents

---

# Defining Classes

---

## Class Definition

Define a class using the keyword `class`.

```python
class Ziploc:
```

---

## Constructor

* Dunder method called `__init__()`
* Note the first parameter: `self`
* Must be the first parameter in method definitions
* Lets Python access the data stored inside the class

```python
class Ziploc:
    def __init__(self, contents=None, is_open=True):
```

---

## Setting Properties in Constructor

* Set `self.prop_name = value`
* Lets you pass arguments into the constructor and have them become part of the class's data.

```python
class Ziploc:
    def __init__(self, contents=None, is_open=True):
        self.contents = contents
        self.is_open = is_open
```

---

## Class Exercise 1

* Add positional argument called `size` to `Ziploc` constructor.
* Set `self.size = size` inside constructor.

---

## Adding Methods

* Just like adding a constructor (because constructors are methods, too)
* Note the `self` parameter.

```python
class Ziploc:
    def __init__(self, size, contents=None, is_open=True):
        self.size = size
        self.contents = contents
        self.is_open = is_open

    def open(self):
        if self.is_open:
            print('The bag is already open!')
        else:
            print('Opening bag.')
            self.is_open = True
```

---

## Class Exercise 2

* Add a method called `close()` to `Ziploc`.
* Use `Ziploc.open()` as a model.
* Accept zero arguments (except for `self`).
* Check whether `self.is_open is True`. If so, set `self.is_open = False`.
* Return no value.

---

## Class Exercise 3

* Add a method called `get_contents()` to `Ziploc`.
* Accept zero arguments (except for `self`).
* Call `self.open()`.
* Set `_contents = self.contents`.
* Set `self.contents = None`.
* Return `_contents`.

---

# Using Classes

---

## Instantiating

```python
# All three are equivalent:
sandwich_bag = Ziploc(size='sandwich', contents='PB & J', is_open=False)
sandwich_bag = Ziploc('sandwich', contents='PB & J', is_open=False)
sandwich_bag = Ziploc.__init__('sandwich', contents='PB & J', is_open=False)
```

N.B.: We don't supply anything for `self`. Python does that for us.

---

## Accessing Properties

Access properties using dot notation.

```python
sandwich_bag.contents  # 'PB & J'

sandwich_bag.contents = 'Ham & Swiss'
```

---

## Using Methods

```python
yum = sandwich_bag.get_contents()  # Method call--note parens

yum  # 'Ham & Swiss'
sandwich_bag.contents  # None
```

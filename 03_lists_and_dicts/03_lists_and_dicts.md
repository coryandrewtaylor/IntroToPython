---
author: Cory Taylor
title: Lists and Dictionaries
date: April 27, 2020
---

# Lists and Dictionaries

---

## Goal of the Lesson

Write a program that keeps track of a to-do list

---

## Lesson Overview

1. Error handling
2. Lists: overview
3. Indexing and slicing
4. List operations
5. List methods
6. Dictionaries: overview
7. Dictionary operations
8. Dictionary methods
9. Loops, `enumerate()`

---

# Handling Errors and Exceptions

---

## `try/except...`

* Python tries to run the code in the `try` block.
* If a given error is thrown, the code in the `except` block runs.

```python
try:
    num = input('Enter a number: ')
    float(num)
except ValueError:
    print('Must type a number.')

# Enter a number: hello
# Must type a number.
```

---

## `try/except/finally`

* Like a normal `try...except...`
* `finally` block runs whether `try` or `except` runs successfully
* Use case: making sure files get closed even if there's an error reading them

```python
try:
    num = input('Enter a number: ')
    float(num)
except ValueError:
    print('Must type a number.')
finally:
    print('I print regardless.')

# Enter a number: 10
# I print regardless.
```

---

# Lists

---

## About Lists

* Type: `list`
* Denoted by square brackets (`[` and `]`)
* Values are mutable and ordered
* Can contain objects of any type
* Can mix and match types within a list

```python
empty_lst = []
int_list = [1, 2, 3]
str_list = ['a', 'b', 'c']
any_list = [1, 'b', None, [2, 'b']]
```

---

## `list()`

Converts other collections into lists

```python
my_str = 'abcd'
list(my_str)
# ['a', 'b', 'c', 'd']

my_tuple = (1, 'a', None,)
list(my_tuple)
# [1, 'a', None]
```

---

# Indexing and Slicing

---

## Indexing

* *Indexed* collections: elements can be accessed by number
* Indexes start at `0`
  * First item at `0`, second at `1`, last at `len(coll) - 1`
* Access an element using *subscript notation*
* Throws an `IndexError` if the subscript is larger than `len(coll) - 1`

```python
my_list = ['a', 'b', 'c', 'd']

my_list[1]    # 'b'

len(my_list)  # 4
my_list[4]    # IndexError: list index out of range
```

---

## Negative Indexing

* Lets you access elements of a collection in reverse order
* Negative indexes start at `-1`
  * Last item at `-1`, second-to-last at `-2`, first at `-len(coll)`
* Throws an `IndexError` if the subscript is smaller than `-len(coll)`

```python
my_list = ['a', 'b', 'c', 'd']

my_list[-1]  # 'd'
my_list[-4]  # 'a'
my_list[-5]  # IndexError: list index out of range
```

---

## Slicing

* *Slice*: a section of an indexed collection
* Uses subscript notation with start and stop indexes separated by a colon: `coll[start:stop]`
  * Starts *at* the start index
  * Stops *before* the stop index
  * In math: $[\text{start}, \text{stop})$
* Works with positive and negative indexes
* Shorthand: empty start/stop indices

```python
my_list = ['a', 'b', 'c', 'd']

my_list[0:2]    # ['a', 'b']
my_list[:2]     # ['a', 'b']
my_list[-3:-1]  # ['b', 'c']
my_list[1:]     # ['b', 'c', 'd']
my_list[:-1]    # ['a', 'b', 'c']
```

---

# List Operations

---

## Updating Item Values

* Use an assignment expression to change the value of a list item
* Only works with items already in the list

```python
my_list = ['a', 'b', 'c', 'd']

my_list[0] = 'z'
my_list
# ['z', 'b', 'c', 'd']

my_list[4] = 'foo'
# IndexError: list assignment index out of range
```

---

## Concatenating Lists

* Like strings, can concatenate lists using `+`
* Creates a new list, so have to assign result to a variable

```python
list_1 = ['a', 'b', 'c']
list_2 = ['foo', 'bar']
list_3 = list_1 + list_2

list_3
# ['a', 'b', 'c', 'foo', 'bar']
```

---

## List Membership

* Use the `in` operator to see whether an item exists in a list

```python
my_list = ['a', 'b', 'c']

'a' in my_list  # True
'z' in my_list  # False
```

---

# List Methods

---

## `list.copy()`

* Copies the contents of a list
* Lets you assign the list's contents to a new variable
* Without `.copy()`, both variables point to the same list--can cause hard-to-find bugs

```python
foo = ['a', 'b', 'c']
bar = foo
bar[0] = 'z'
print(foo)  # ['z', 'b', 'c']

foo = ['a', 'b', 'c']
bar = foo.copy()
bar[0] = 'z'
print(foo)  # ['a', 'b', 'c']
```

---

## `list.append()`

* Adds a single item to the end of a list
* Updates the list *in place*: No new list created, so no assignment expression necessary

```python
my_list = ['a', 'b', 'c', 'd']
my_list.append('foo')

my_list
# ['a', 'b', 'c', 'd', 'foo']
```

---

## `list.pop()`

* Removes the item at a given index
* Updates in place
* Returns the value that was removed

```python
my_list = ['a', 'b', 'c', 'd']
popped_val = my_list.pop(3)

my_list
# ['a', 'b', 'c']

popped_val
# 'd'
```

---

## List Documentation

https://devdocs.io/python~3.7/library/stdtypes#list

https://docs.python.org/3.7/library/stdtypes.html#common-sequence-operations

https://docs.python.org/3.7/library/stdtypes.html#mutable-sequence-types

---

# Dictionaries

---

## About Dictionaries

* Type: `dict`
* Mutable, unordered collections of key-value (K-V) pairs
* Denoted by braces (`{` and `}`)
* Keys and values separated by colons
* K-V pairs comma-separated
* Keys must be immutable (strings, numbers, tuples); values can be anything

```python
empty_dict = {}

my_dict = {
    'a': 'foo',
    'b': 'bar',
    'c': 'baz'
}
```

---

## `dict()`

* Creates a dict from a list of *keyword arguments* (*kwargs*)
* N.B.:
  * K-V pairs expressed as assignment operations
  * Keys must follow rules for variable names
  * Keys are not wrapped in quotes

```python
my_dict = dict(a='foo', b='bar', c='baz')
comparison = {
    'a': 'foo',
    'b': 'bar',
    'c': 'baz'
}

my_dict == comparison
# True
```

---

## Nesting

* Dict values can be of any type, including lists and other dicts

```python
colors = {
    'black': {
        'hex': '0x000000',
        'rgb': [0, 0, 0],
    },
    'white': {
        'hex': '0xffffff',
        'rgb': [255, 255, 255],
    },
    'red': {
        'hex': '0xff0000',
        'rgb': [255, 0 0],
    }
}
```

---

# Dict Operations

---

## Accessing Values

* Like a paper dictionary: Use a key to look up a value
* Subscripting is the most common approach
* Throws a `KeyError` if the key is not present in the dict

```python
my_dict = {
    'a': 'foo',
    'b': 'bar',
    'c': 'baz'
}

my_dict['a']
# 'foo'

my_dict['z']
# KeyError: 'z'
```

---

## Accessing Nested Values

* Chain subscripts to access nested values

```python
colors = {
    'red': {
        'hex': '0xff0000',
        'rgb': [255, 0 0],
    }
}

colors['red']['hex']
# '0xff0000'

colors['red']['rgb'][0]
# 255
```

---

## Dict Membership

* To test if an item is a \_\_\_\_\_ in a dict, use \_\_\_\_\_:
  * key: `item in dict_name`.
  * value: `item in dict_name.values()`

---

# Dict Methods

---

## `dict.get()`

* Another way to access dict values
* Two ways to use it
  1. `dict_name.get(key)`
  2. `dict_name.get(key, default)`
* Approach (2) lets you avoid a `KeyError`

```python
my_dict = dict(a='foo', b='bar', c='baz')

my_dict.get('a')  # 'foo'
my_dict.get('z')  # KeyError: 'z'

my_dict.get('a', None)  # 'foo'
my_dict.get('z', None)  # None
```

---

## `dict.pop()`

* Works like `list.pop()` and `dict.get()` combined
* Removes specified item from the dict and returns it
* Two ways of using:
  1. `dict_name.pop(key)`
  2. `dict_name.pop(key, default)`
* Approach (2) lets you avoid a `KeyError`

---

## `dict.copy()`

* Works just like `list.copy()`
* Avoids hard-to-find bugs where two variables are changing the same dict

---

## Dict Documentation

https://devdocs.io/python~3.7/library/stdtypes#dict

---

# Loops

---

## About Loops

* Let you apply the same logic repeatedly
* `while` loops run until a condition is `False`
* `for` loops iterate over the items in a collection

---

## while Loops

* Syntax: `while condition:`
* Can create infinite loops

```python
while True:
    do_something()
```

---

## Controlling Loops

* `break` command ends a loop
* `continue` stops current iteration and starts beginning of next iteration
* Both are useful inside conditionals

```python
while True:
    do_something()

    if some_condition:
        break  # Stops loop entirely
    elif other_condition:
        continue  # Skips to do_something()

    do_something_else()
```

---

## for Loops

* Apply the same logic to each item in a collection, one at a time
* Syntax: `for loop_var in collection:`
* `loop_var` placeholder:
  * A normal variable name
  * Disappears once the loop is complete
  * Label for the current item

---

## How for Loops Work

```python
# Print numbers 0 to 4 individually
for i in range(5):
    print(i)

# Unrolled equivalent
i = 0
print(i)
i = 1
print(i)
i = 2
print(i)
i = 3
print(i)
i = 4
print(i)
```

---

## Iterating Over Lists

```python
letters = ['a', 'b', 'c', 'd']

for letter in letters:
    print(letter)
```

---

## `enumerate()`

* Accepts a collection
* Generates a series of `(index, item)` tuples
* Can use multiple assignment in `loop_var` position

```python
letters = ['a', 'b', 'c', 'd']

for i, letter in enumerate(letters):
    print(letter, 'is letter number', i)

# Equivalent to
for val in enumerate(letters):
    i = val[0]
    letter = val[1]
    print(letter, 'is letter number', i)
```

---

## Iterating Over Dicts: Keys

* Syntax: `for loop_var in dict_name:`
* Use case: modifying all the entries in a dict

```python
colors = {
    'black': {'hex': '0x000000'},
    'white': {'hex': '0xffffff'},
    'red': {'hex': '0xff0000'}
}

for c in colors:
    if 'hex' in colors[c]:
        _hex_code = colors[c]['hex']
        _hex_int = int(_hex_code, base=16)
        _oct_code = oct(_hex_int)
        colors[c]['oct'] = _oct_code
```

---

## Iterating Over Dicts: Keys + Values

* Syntax: `for k, v in dict_name.items()`
* Rewrite of previous example:

```python
colors = {
    'black': {'hex': '0x000000'},
    'white': {'hex': '0xffffff'},
    'red': {'hex': '0xff0000'}
}

for c, codes in colors.items():
    if 'hex' in codes:
        _hex_int = int(codes['hex'], base=16)
        codes['oct'] = oct(_hex_int)
        colors[c] = codes
```

---

# Exercise

Write a to-do list program

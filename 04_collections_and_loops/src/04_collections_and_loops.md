---
author: Cory Taylor
title: Collections and Loops
date: April 27, 2020
---

# Collections and Loops

---

## Goals of the Lesson

Gain a solid understanding of (1) collection types, (2) loop constructs, and (3) error handling

---

## Lesson Overview

1. Collections overview, mutability, ordering
2. Strings as collections
3. Indexing and slicing
4. Membership testing
5. Tuples
6. Lists
7. Dicts
8. Loops (`while`, `for`)
9. Handling errors

---

# Collections

---

## About Collections

* AKA *data structures*
* A container for one or more *items*/*elements* of data
* Examples:
  * `str`
  * `tuple`
  * `list`
  * `dict`

---

## Mutability

* Attribute of every Python type (not just collections!)
* *Immutable*: Results of an operation must be assigned to a variable
* *Mutable*: Can change the data without creating a new variable (updating in place)
* `str`, `int`, `float`, `tuple` are all immutable
* `list` and `dict` are mutable

---

## Ordering

* Attribute of collection types
* *Ordered* collections: Elements stored in a particular order
* *Unordered* collections: Elements stored in no particular order
* `str`, `tuple`, `list` are ordered
* `dict` is unordered

---

# Strings

---

## Strings as Collections

* Can only contain letters, numbers, and symbols
  
    ```python
    type(None)  # <class 'NoneType'>
    str(None)  # 'None'
    ```

* Immutable: results of string operations must be assigned to a variable

    ```python
    foo = 'bar'
    foo.upper()  # 'BAR'
    print(foo)   # 'bar'
    ```

* Ordered: position of characters matters

    ```python
    'abcd' == 'dcba'  # False
    ```

---

# Indexing and Slicing

---

## Indexing

* How to access elements in ordered collections
* Indexes start at `0`
  * First item at `0`, second at `1`, last at `len(coll) - 1`
* Access an element using *subscript notation*

```python
foo = 'abcd'

foo[0]  # 'a'
foo[1]  # 'b'
foo[2]  # 'c'
foo[3]  # 'd'
```

---

## Negative Indexing

* Lets you access elements of a collection in reverse order
* Negative indexes start at `-1`
  * Last item at `-1`, second-to-last at `-2`, first at `-len(coll)`

```python
foo = 'abcd'

foo[-1]  # 'd'
foo[-2]  # 'c'
foo[-3]  # 'b'
foo[-4]  # 'a'
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
foo = 'abcd'

foo[0:2]    # 'ab'
foo[:2]     # 'ab'
foo[-3:-1]  # 'bc'
foo[1:]     # 'bcd'
foo[:-1]    # 'abc'
```

---

# Membership

---

## Testing for Membership

* Use the `in` operator to test whether an item is present in a collection

```python
foo = 'abcd'
'a' in foo  # True
'z' in foo  # False
```

---

# Tuples

---

## About Tuples

* Denoted by parentheses: `(` and `)`

    ```python
    empty_tuple = ()
    ```

* Immutable: Results of tuple operations must be assigned to a variable
* Ordered: Can access elements by index; position of elements matters

    ```python
    foo = ('a', 'b', 'c',)
    bar = ('c', 'b', 'a',)

    foo[0]   # 'a'
    foo[:2]  # ('a', 'b')

    foo == bar  # False
    ```

* Can contain objects of any type; membership is testable

    ```python
    baz = (1, 'b', None,)
    1 in baz
    # True
    ```

---

## Tuple Unpacking

* Elements of a tuple can be assigned to different variables in a single assignment statement
* Number of variables must match number of tuple elements

```python
tpl = ('a', 'b',)
foo, bar = tpl

print(foo)  # 'a'
print(bar)  # 'b'
```

---

# Lists

---

## About Lists

* Denoted by square brackets: `[` and `]`

    ```python
    empty_list = []
    ```

* Mutable: Many list operations don't require a new variable (see "List Methods" section)
* Ordered: Can access elements by index; position of elements matters

    ```python
    foo = ['a', 'b', 'c']
    bar = ['c', 'b', 'a']

    foo[0]   # 'a'
    foo[:2]  # ['a', 'b']

    foo == bar  # False
    ```

* Can contain objects of any type; membership is testable

    ```python
    baz = [1, 'b', None]
    1 in baz
    # True
    ```

---

## `list()`

Converts other collections into lists

```python
foo = 'abcd'
list(foo)
# ['a', 'b', 'c', 'd']

bar = (1, 'a', None,)
list(bar)
# [1, 'a', None]
```

---

# List Operations

---

## Updating Item Values

* Use an assignment expression to change the value of a list item

```python
foo = ['a', 'b', 'c', 'd']

foo[0] = 'z'
foo
# ['z', 'b', 'c', 'd']
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

# Dicts

---

## About Dicts (1)

* Denoted by braces: `{` and `}`
* Keys and values separated by colons
* K-V pairs comma-separated
* Keys must be immutable; values can be anything

```python
empty_dict = {}

spqr = {
    'a': 'foo',
    'b': 'bar',
    'c': 'baz'
}
```

---

## About Dicts (2)

* Mutable: Many dict operations don't require a new variable (see "Dict Methods" section)
* Unordered: Access values by key

    ```python
    spqr = {
        'a': 'foo',
        'b': 'bar'
    }

    spqr['a']  # 'foo'
    ```

* Membership tests are different for keys, values, and K-V pairs

    ```python
    spqr = {
        'a': 'foo',
        'b': 'bar'
    }

    # All True:
    'a' in spqr
    'foo' in spqr.values()
    ('a', 'foo') in spqr.items()
    ```

---

## `dict()`

* Creates a dict from a list of *keyword arguments* (*kwargs*)
* N.B.:
  * K-V pairs expressed as assignment operations
  * Keys must follow rules for variable names
  * Keys are not wrapped in quotes

```python
spqr = dict(a='foo', b='bar', c='baz')
comparison = {
    'a': 'foo',
    'b': 'bar',
    'c': 'baz'
}

spqr == comparison
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

# Dict Methods

---

## `dict.get()`

* Another way to access dict values
* Two ways to use it
  1. `dict_name.get(key)`
  2. `dict_name.get(key, default)`
* Approach (2) lets you avoid a `KeyError`

```python
spqr = dict(a='foo', b='bar', c='baz')

spqr.get('a')  # 'foo'
spqr.get('z')  # KeyError: 'z'

spqr.get('a', None)  # 'foo'
spqr.get('z', None)  # None
```

---

## `dict.pop()`

* Works like `list.pop()` and `dict.get()` combined
* Removes specified item from the dict and returns it
* Two ways of using:
  1. `dict_name.pop(key)`
  2. `dict_name.pop(key, default)`
* Approach (2) lets you avoid a `KeyError`

```python
spqr = dict(a='foo', b='bar', c='baz')
popped = spqr.pop('c')

spqr
# {'a': 'foo', 'b': 'bar'}

popped
# 'baz'
```

---

## `dict.copy()`

* Works just like `list.copy()`
* Avoids hard-to-find bugs where two variables are changing the same dict

```python
foo = {'a': 1, 'b': 2}
bar = foo
bar['c'] = 3
print(foo)
# {'a': 1, 'b': 2, 'c': 3}

foo = {'a': 1, 'b': 2}
bar = foo.copy()
bar['c'] = 3
print(foo)
# {'a': 1, 'b': 2}
```

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
* Example of infinite loop: the REPL

```python
while True:
    code = input('>>> ')
    result = eval(code)
    print(result)
```

---

## Controlling Loops

* `break` command ends a loop
* `continue` stops current iteration and starts beginning of next iteration
* Both are useful inside conditionals

```python
while True:
    code = input('>>> ')

    if code == 'quit()':
        break  # Stops REPL
    elif code == 'ctrl-C':
        continue  # Goes back to input('>>> ')

    result = eval(code)
    print(result)
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
foo = [0, 1, 2, 3, 4]
for i in foo:
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
* Can use tuple unpacking in `loop_var` position

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

```python
colors = {
    'black': {'hex': '0x000000'},
    'white': {'hex': '0xffffff'},
    'red': {'hex': '0xff0000'}
}

for c in colors:
    if 'hex' in colors[c]:
        print('Hex code for ', c, 'is', colors[c]['hex'])
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
        print('Hex code for', c, 'is', codes['hex'])
```

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

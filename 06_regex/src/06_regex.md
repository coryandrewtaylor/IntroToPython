---
author: Cory Taylor
title: Regular Expressions
date: May 8, 2020
---

# Regular Expressions

---

## Goals of the Lesson

1. Learn basic regular expression syntax
2. Work with regular expressions in Python
3. Write a regular expression to identify email addresses

---

## Lesson Overview

1. What is/why regex?
2. Regex syntax
   1. Character literals
   2. Special characters
   3. Character classes
   4. Groups and ranges
   5. Quantifiers
3. Regex in Python: `re`
   1. Raw strings
   2. `re.compile()`
   3. `re.search()`
   4. `re.sub()`

---

# About Regex

---

## What is Regex?

* A special programming language
* Designed specifically to match strings

---

## Why Use Regex?

* It's expressive.
* It's *fast*.
* It can help you solve tricky problems with data.

---

# Regex Syntax

---

## Character Literals

* Everyday strings "are the simplest regular expressions; they simply match themselves." [1]
* The pattern `John` will match `'John Doe`', but not `'Jon Snow'` or `'john doe'`.

---

## Escaped Character Literals

* Some characters have special meanings in regex.
* To match these characters literally, you have to escape them.

---

| Pattern | Matches |
|---------|---------|
| `\.`    | `.`     |
| `\^`    | `^`     |
| `\$`    | `$`     |
| `\*`    | `*`     |
| `\+`    | `+`     |
| `\?`    | `?`     |
| `\(`    | `(`     |
| `\[`    | `[`     |
| `\{`    | `{`     |
| `\|`    | `|`     |

Table adapted from [1].

---

## Special Characters

An incomplete list:

| Pattern | Meaning         |
|---------|-----------------|
| `\n`    | Newline         |
| `\r`    | Carriage return |
| `\t`    | Tab             |

Table adapted from [2].

---

## Character Classes

* _Character class_: A character or escape sequence that matches a range of characters

| Pattern | Matches                                            |
|---------|----------------------------------------------------|
| `.`     | Any character except `\n`                          |
| `\w`    | Any letter, digit, underscore                      |
| `\W`    | Any character *except* letters, digits, underscore |
| `\d`    | A digit                                            |
| `\D`    | Any character *except* digits                      |
| `\s`    | A whitespace character                             |
| `\S`    | Any non-whitespace character                       |

Table adapted from [1] and [2].

---

## Anchors

* _Anchor_: A character or escape sequence that dictates where a match should occur within a string.

| Pattern | Meaning              |
|---------|----------------------|
| `^`     | Start of string/line |
| `$`     | End of string/line   |
| `\b`    | Word boundary        |
| `\B`    | Not a word boundary  |

Table adapted from [1]

---

## Groups

* `|` allows multiple patterns to be matched: `John|Jon` matches `'John Doe'` and `'Jon Snow'`
* `()` denotes a subgroup: `Jo(hn|n)` is a simpler version of the above

---

## Ranges

* `[]` lets you define a custom character class: `[Jj]ohn` matches `'john'` and `'John'`
* Inside brackets, `-` denotes a range of characters: `[A-Z]` matches any English capital letter

---

## Quantifiers

| Pattern  | Quantity         |
|----------|------------------|
| `*`      | 0 or more        |
| `+`      | 1 or more        |
| `?`      | 0 or 1           |
| `{m, n}` | *m* to *n* times |

---

# Regex in Python

---

## Raw Strings

* Python has several special kinds of strings, each denoted by a letter that comes immediately before the opening quote.
* Raw strings are best for regex, because they don't require backslashes to be escaped.

```python
# Normal string:
'\\\\'  # Evaluates to '\\'

# Raw string:
r'\\'   # Evaluates to '\\'
```

---

## `re`

* Python's regex functionality lives in a module called `re`.
* In order to use `re`, you have to `import` it.
* Put this line at the top of your program:

```python
import re
```

---

## `re.compile()`

* Creates a class instance based on a regex pattern
* Beneficial if you're using the regex a lot or if the pattern is very complex.

```python
email_pattern = r'.*@.*'
email_re = re.compile(email_pattern)
```

---

## `re.search()`

* Returns the occurrences of the pattern inside a string.

```python
my_email = 'foo@bar.edu'


```

---

## `re.sub()`

* Like `str.replace() only better.

---

# References

[^1] [re--Regular expression operations--Python 3.7.7 documentation](https://docs.python.org/3.7/library/re.html#module-re)

[^2] [Regular Expressions Cheat Sheet - Almost Perfect Email Regex](https://emailregex.com/regular-expressions-cheat-sheet/index.html)
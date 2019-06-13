# Strings, Lists, and Tuples

> "Good programming is good writing." - John Shore

There's some overlap among Python's strings, lists, and tuples.  In a way, you could think of strings as lists of characters.  Many list operations work exactly the same over strings like subscripting to get a particular item. We can ask for the first (or "zeroth") element from a string:

````
>>> name = 'Curly'
>>> name[0]
'C'
````

Or from a list:

````
>>> names = ['Larry', 'Moe', 'Curly', 'Shemp']
>>> names[0]
'Larry'
````

"Slice" operations let you take a range of items. Notice that we can operate on a string literal (in quotes):

````
>>> names[2:4]
['Curly', 'Shemp']
>>> 'Curly'[2:4]
'rl'
````

Functions like `join` that take lists can also work on strings:

````
>>> ', '.join(names)
'Larry, Moe, Curly, Shemp'
>>> ', '.join(names[0])
'L, a, r, r, y'
````

You can ask if a list contains a certain member, and you can also ask if a string contains a certain character or substring:

````
>>> 'Moe' in names
True
>>> 'r' in 'Larry'
True
>>> 'url' in 'Curly'
True
>>> 'x' in 'Larry'
False
>>> 'Joe' in names
False
````

You can iterate with a `for` loop over both the items in a list:

````
>>> names = ['Larry', 'Moe', 'Curly', 'Shemp']
>>> for name in names:
...   print(name)
...
Larry
Moe
Curly
Shemp
````

Or the characters in a word:

````
>>> for letter in 'Curly':
...   print(letter)
...
C
u
r
l
y
````

Just as in bash, we can create a counter, increment it inside our loop, and print the element number before the element:

````
>>> names = ['Larry', 'Moe', 'Curly', 'Shemp']
>>> i = 0
>>> for name in names:
...   i += 1
...   print(i, name)
...
1 Larry
2 Moe
3 Curly
4 Shemp
````

Because we so often want this behavior, there is a function called `enumerate` that takes a list/string and returns the index/position along with the item/character. Since it's so annoying to deal with zero-offset counting, we can tell `enumerate` to `start` at 1:

````
>>> names = ['Larry', 'Moe', 'Curly', 'Shemp']
>>> for i, name in enumerate(names, start=1):
...     print('{:3} {}'.format(i, name))
...
  1 Larry
  2 Moe
  3 Curly
  4 Shemp
>>> for i, letter in enumerate('Curly', start=1):
...     print('{:3} {}'.format(i, letter))
...
  1 C
  2 u
  3 r
  4 l
  5 y
````

You can turn a list around with the `reversed` function:

````
>>> reversed(names)
<list_reverseiterator object at 0x109e490f0>
````

What we have here is a failure to communicate. You expected to see the list of names in the reverse order, but what you got was a promise from Python to give you that list when you actually need it. In the REPL, we can use the `list` function:

````
>>> list(reversed(names))
['Shemp', 'Curly', 'Moe', 'Larry']
````

So you can also use that to reverse a word:

````
>>> list(reversed('cat'))
['t', 'a', 'c']
````

OK, well, I wanted the word "tac" and not the list of letters in "tac"! We can put them back into a word by calling the `join` *function* of the *string element* that we want to put between the letter (which is an empty string). Notice that I don't have to use `list` because the `join` function will iterate on the `reversed` result:

````
>>> ''.join(reversed('cat'))
'tac'
````

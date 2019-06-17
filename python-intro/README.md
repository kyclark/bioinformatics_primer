# Programming with Python

> “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” - Martin Fowler

## Hello

Let's use our familiar "Hello, World!" to get started:

````
$ cat -n hello.py
     1	#!/usr/bin/env python3
     2
     3	print('Hello, World!')
````

The first thing to notice is the "shebang" on line 1. I'm going to use `env` to find the first `python3` binary in the user's `$PATH`. In `bash`, we could use either `echo` or `printf` to print to the terminal (or a file). In Python, we have `print()` noting that we must use parentheses now to invoke functions. 

## Variables

It's not so interesting to just say "Hello, World!" all the time. Let's make a program that will say "hello" to some value that we pass in. This value can change each time we run the program, so it's common to call this a "variable."

Let's use the REPL (Read-Evaluate-Print-Loop, pronounced "reh-pul") to play with variables. Type `python` (or `python3` or `ipython`) to get into a REPL:

````
>>> name = 'Duderino'
>>> print('Hello,', name)
Hello, Duderino
````

Here I'm showing that we can create variable called `name` by assigning it some value like "Duderino." Unlike `bash`, we don't have to worry about spaces around the `=`. You can put any number of spaces around the equal sign, but it's most common (and readable) to put just one on each side. Notice that `print` will accept more than one argument and will put spaces between the arguments. You can tell it to use some other "separator" by indicating the `sep` keyword argument. Notice the Pythonic style is that there are *no* spaces around the `=` for keywords:

````
>>> print('Hello', name, sep=', ')
Hello, Duderino
````

It's not easy to tell, but `print` is also putting a newline on the end. We can change that with the `end` keyword argument:

````
>>> print('Hello', name, sep=', ', end='!')
Hello, Duderino!>>>
````

Unlike in `bash`, we cannot use a variable directly in a `print` statement or we get the equivalent of George Burns telling Gracie "Say 'Good night,' Gracie" and she says "Good night, Gracie!":

````
>>> print('Hello, name')
Hello, name
````

We could to use the `+` operator to concatenate it to the literal string "Hello, ":

````
>>> print('Hello, ' + name)
Hello, Duderino
````

## Types: Strings and Numbers

As you might expect, the "plus" operator `+` is also used to perform numeric addition:

````
>>> n = 10
>>> n + 1
11
````

The `name` variable above is of the type `str` (string) because we put the value in quotes (single or double, it doesn't matter). 

````
>>> name = 'The Dude'
>>> type(name)
<class 'str'>
````

Numbers don't have quotes. Number can be integers (`int`) or floating-point numbers (`float`) if they have a decimal somewhere or you write them in scientific notation:

````
>>> type(10)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type(1.)
<class 'float'>
>>> type(2.864e-10)
<class 'float'>
````

The "plus" operator behaves completely differently with different *types* of arguments as long as the arguments are both strings or both numbers. Things go wobbly when you mix them:

````
>>> 'Hello, ' + 'Mr. Lebowski'
'Hello, Mr. Lebowski'
>>> 1 + 2
3
>>> 1 + 'Mr. Lebowski'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
````

## Lists

Before we go further, I will introduce a different variable type called a "list" as we are going to need that immediately. You create a list by putting values in `[]` (square brackets or just "brackets"):

````
>>> vals = ['foo', 'bar', 'baz']
>>> vals
['foo', 'bar', 'baz']
```` 

You can get the length of a list using the `len` function:

````
>>> len(vals)
3
````

But note that, like so many other languages, Python starts counting at `0`, so the first element is in the "zeroth" position. The value at position `1` is actually the *second* value.

````
>>> vals[0]
'foo'
>>> vals[1]
'bar'
````

We'll talk much more about lists in the next chapter. I needed to tell you that so I could tell you this next bit.

## Command-line Arguments: sys.argv is a list

Now let's get our "hello" program to greet an argument passed from the command line. We discussed in the `bash` section that programs can take *positional* arguments, e.g. `ls` can accept the name of the directory you wish to list or `wc` can take the name of a file to count. *Positional* arguments mean the first argument, the second argument, and so on. In the command `ls ~`, the `~` (tilde which means `$HOME` in `bash`) is the one and only positional argument. In the command `ls /bin /usr/bin/`, there are two positional arguments, `/bin` and `/usr/bin/`.

Named options have some sort of prefix, e.g., `find` can take a `-maxdepth` argument to indicate how many levels deep to search. Lastly, commands may also take flags like the `-l` flags to `ls` that indicates you wish to see the "long" listing. 

To get access to the positional arguments to our program, we need to `import sys` which is a package of code that will interact with the system. Those arguments will be a *list*:

````
$ cat -n hello_arg.py
     1    #!/usr/bin/env python3
     2
     3    import sys
     4
     5    args = sys.argv
     6    print('Hello, ' + args[1] + '!')
````

From the `sys` module, we call the `argv` function to get the "argument vector."  This is a list, and, like `bash`, the name of the script is the first argument (in the zeroth position) -- `args[0]`. That means the first *actual* "argument" to the script is in `args[1]`.

````
$ ./hello_arg.py Geddy
Hello, Geddy!
````

But there is a problem if we fail to pass any arguments:

````
$ ./hello_arg.py
Traceback (most recent call last):
  File "./hello_arg.py", line 6, in <module>
    print('Hello, ' + args[1] + '!')
IndexError: list index out of range
````

We tried to access something in `args` that doesn't exist, and so the entire program came to a halt ("crashed"). As in `bash`, we need to check how many arguments we have. Before I show you how to do that, let me explain something about *slicing* lists. Inside the `[]`, you can indicate a start and stop positon like so:

````
>>> vals
['foo', 'bar', 'baz']
>>> vals[1:]
['bar', 'baz']
>>> vals[1:2]
['bar']
````

In the last example, you see that the stop position is not inclusive. Even though you've seen that Python gets very upset by asking for a position in a list that does not exist, it has no problem giving you nothing when you ask for a *slice* that doesn't exist:

````
>>> vals[1000:]
[]
````

So we can use that to ask for `sys.argv[1:]` to get all the *actual* arguments to our program, skipping over the name of the program itself:


````
$ cat -n hello_arg2.py
     1	#!/usr/bin/env python3
     2
     3	import sys
     4
     5	args = sys.argv[1:]
     6
     7	if len(args) < 1:
     8	    print('Usage:', sys.argv[0], 'NAME')
     9	    sys.exit(1)
    10
    11	name = args[0]
    12	print('Hello, ' + name + '!')
````

If there are fewer than 1 argument, then we print a usage statement and use `sys.exit` to send the operating system a non-zero exit status, just like in `bash`. It works much better now:

````
$ ./hello_arg2.py
Usage: ./hello_arg2.py NAME
$ ./hello_arg2.py Alex
Hello, Alex!
````

Here is the same functionality but using some new functions, `str.format` so we can introduce a different way to join strings, and `os.path.basename` so we can get the name of the program without any leading path information like `./`:

````
$ cat -n hello_arg3.py
     1	#!/usr/bin/env python3
     2
     3	import sys
     4	import os
     5
     6	args = sys.argv[1:]
     7
     8	if len(args) != 1:
     9	    script = os.path.basename(sys.argv[0])
    10	    print('Usage: {} NAME'.format(script))
    11	    sys.exit(1)
    12
    13	name = args[0]
    14	print('Hello, {}!'.format(name))
$ ./hello_arg3.py
Usage: hello_arg3.py NAME
$ ./hello_arg3.py Neil
Hello, Neil!
````

## The main() thing

Many languages (e.g., Perl, Rust, Haskell) have the idea of a `main` module/function where all the processing starts. If you define a `main` function using `def main`, most people reading your code would understand that the program *ought* to begin there. (I say "ought" because Python won't actually make that happen. You still have to *call* the `main` function to make your program run!) I usually put my `main` first and then call it at the end of the script with this `__name__ == '__main__'` business. This looks a bit of a hack, but it is fairly Pythonic.

````
$ cat -n hello_arg4.py
     1	#!/usr/bin/env python3
     2
     3	import sys
     4	import os
     5
     6	def main():
     7	    args = sys.argv[1:]
     8
     9	    if len(args) != 1:
    10	        script = os.path.basename(sys.argv[0])
    11	        print('Usage: {} NAME'.format(script))
    12	        sys.exit(1)
    13
    14	    name = args[0]
    15	    print('Hello, {}!'.format(name))
    16
    17
    18	if __name__ == '__main__':
    19	    main()
$ ./hello_arg4.py
Usage: hello_arg4.py NAME
$ ./hello_arg4.py '2013 Rock and Roll Hall of Fame Inductees'
Hello, 2013 Rock and Roll Hall of Fame Inductees!
````

## Function Order

Note that you cannot put call to `main()` before `def main` because you cannot call a function that hasn't been defined (lexically) in the program yet. To add insult to injury, this is a **run-time error** -- meaning the mistake isn't caught by the compiler when the program is parsed into byte-code; instead the program just crashes.

````
$ cat -n func-def-order.py
     1    #!/usr/bin/env python3
     2
     3    print('Starting the program')
     4    foo()
     5    print('Ending the program')
     6
     7    def foo():
     8        print('This is foo')
$ ./func-def-order.py
Starting the program
Traceback (most recent call last):
  File "./func-def-order.py", line 4, in <module>
    foo()
NameError: name 'foo' is not defined
````

To contrast:

````
$ cat -n func-def-order2.py
     1    #!/usr/bin/env python3
     2
     3    def foo():
     4        print('This is foo')
     5
     6    print('Starting the program')
     7    foo()
     8    print('Ending the program')
$ ./func-def-order2.py
Starting the program
This is foo
Ending the program
````

## Handle All The Args!

If we like, we can greet to any number of arguments:

````
$ cat -n hello_arg5.py
     1	#!/usr/bin/env python3
     2
     3	import sys
     4	import os
     5
     6	def main():
     7	    names = sys.argv[1:]
     8
     9	    if len(names) < 1:
    10	        script = os.path.basename(sys.argv[0])
    11	        print('Usage: {} NAME [NAME2 ...]'.format(script))
    12	        sys.exit(1)
    13
    14	    print('Hello, {}!'.format(', '.join(names)))
    15
    16	if __name__ == '__main__':
    17	    main()
$ ./hello_arg5.py
Usage: hello_arg5.py NAME [NAME2 ...]
$ ./hello_arg5.py Geddy Alex Neil
Hello, Geddy, Alex, Neil!
````

Notice on line 14 to see how we can `join` all the arguments on a comma + space.

## Conditionals

So far we've been using an `if` condition to see if we have enough arguments. If you want to test for more than one condition, you can use `elif` (else if) and `else` ("otherwise" or the "default" branch if all others fail). Here we'll use the `input` function to present the user with a prompt and get their input:

````
$ cat -n if-else.py
     1	#!/usr/bin/env python3
     2
     3	name = input('What is your name? ')
     4	age = int(input('Hi, ' + name + '. What is your age? '))
     5
     6	if age < 0:
     7	    print("That isn't possible.")
     8	elif age < 18:
     9	    print('You are a minor.')
    10	else:
    11	    print('You are an adult.')
$ ./if-else.py
What is your name? Ken
Hi, Ken. What is your age? -4
That isn't possible.
$ ./if-else.py
What is your name? Lincoln
Hi, Lincoln. What is your age? 29
You are an adult.
````

On line 3, we can put the first answer directly into the `name` variable; however, on line 4, I need to convert the answer to an integer with `int` because I will need to compare it numerically, cf:

````
>>> 4 < 5
True
>>> '4' < 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() < int()
>>> int('4') < 5
True
````

Things go very badly if we blindly try to coerce a string into an `int`:

````
$ ./if-else.py
What is your name? Doreen
Hi, Doreen. What is your age? Ageless
Traceback (most recent call last):
  File "./if-else.py", line 4, in <module>
    age = int(input('Hi, ' + name + '. What is your age? '))
ValueError: invalid literal for int() with base 10: 'Ageless'
````

Later we'll talk about how to avoid problems like this.

## Loops

As in bash, we can use `for` loops in Python. Here's another way to greet all the people:

````
$ cat -n hello_arg6.py
     1	#!/usr/bin/env python3
     2
     3	import sys
     4	import os
     5
     6	def main():
     7	    names = sys.argv[1:]
     8
     9	    if len(names) < 1:
    10	        prg = os.path.basename(sys.argv[0])
    11	        print('Usage: {} NAME [NAME2 ...]'.format(prg))
    12	        sys.exit(1)
    13
    14	    for name in names:
    15	        print('Hello, ' + name + '!')
    16
    17
    18	if __name__ == '__main__':
    19	    main()
$ ./hello_arg6.py
Usage: hello_arg6.py NAME [NAME2 ...]
$ ./hello_arg6.py Salt Peppa
Hello, Salt!
Hello, Peppa!
````

You can use a `for` loop on anything that is like a list! A string is a list of characters:

````
>>> for letter in "abc":
...    print(letter)
...
a
b
c
````

The `range` function returns something that can be "iterated" like a list:

````
>>> for number in range(0, 5):
...    print(number)
...
0
1
2
3
4
````

Lists, of course:

````
>>> for word in ['foo', 'bar']:
...    print(word)
...
foo
bar
````

You can use the `str.split` function to split a string (the default is to split on spaces):

````
>>> for word in 'We hold these truths'.split():
...    print(word)
...
We
hold
these
truths
````

And we can use the `open` function to open a file and read each line using a `for` loop:

````
>>> for line in open('input1.txt'):
...    print(line, end='')
...
this is
some text
from a file.
````

The last example either needs to suppress the newline from `print` or do `rstrip()` on the line to remove it as the text coming from the file has a newline.

## Stubbing New Programs with new.py

Every program we've seen so far has had the same basic structure:

* Shebang
* import modules
* define main()
* call main()

Additionally we keep having to write the same few lines of code to get the arguments from `sys.argv[1:]` and then test that we have the right number and then print a usage and `sys.exit(1)`. Rather than type all that boilerplate or copy-paste from other programs, let's use a program to help us create new programs.

Included in the `bin` directory of the GitHub repo, there is a program called `new.py` that will stub out all this code for you. Make sure you either add that directory to you `$PATH` or copy that program into your existing `$PATH`, e.g., I like to have `$HOME/.local/bin` for programs like this:

````
$ which new.py
/Users/kyclark/.local/bin/new_py.py
````

Now run it with no arguments. As you might expect, it gives you a usage statement:

````
$ new.py
usage: new.py [-h] [-s] [-f] program
new.py: error: the following arguments are required: program
````

Give it the name of a new program (either with or without `.py`):

````
$ new.py foo
Done, see new script "foo.py."
$ cat -n foo.py
     1	#!/usr/bin/env python3
     2	"""
     3	Author : kyclark
     4	Date   : 2019-06-13
     5	Purpose: Rock the Casbah
     6	"""
     7
     8	import argparse
     9	import os
    10	import sys
    11
    12
    13	# --------------------------------------------------
    14	def get_args():
    15	    """Get command-line arguments"""
    16
    17	    parser = argparse.ArgumentParser(
    18	        description='Argparse Python script',
    19	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    20
    21	    parser.add_argument('positional',
    22	                        metavar='str',
    23	                        help='A positional argument')
    24
    25	    parser.add_argument('-a',
    26	                        '--arg',
    27	                        help='A named string argument',
    28	                        metavar='str',
    29	                        type=str,
    30	                        default='')
    31
    32	    parser.add_argument('-i',
    33	                        '--int',
    34	                        help='A named integer argument',
    35	                        metavar='int',
    36	                        type=int,
    37	                        default=0)
    38
    39	    parser.add_argument('-f',
    40	                        '--flag',
    41	                        help='A boolean flag',
    42	                        action='store_true')
    43
    44	    return parser.parse_args()
    45
    46
    47	# --------------------------------------------------
    48	def main():
    49	    """Make a jazz noise here"""
    50
    51	    args = get_args()
    52	    str_arg = args.arg
    53	    int_arg = args.int
    54	    flag_arg = args.flag
    55	    pos_arg = args.positional
    56
    57	    print('str_arg = "{}"'.format(str_arg))
    58	    print('int_arg = "{}"'.format(int_arg))
    59	    print('flag_arg = "{}"'.format(flag_arg))
    60	    print('positional = "{}"'.format(pos_arg))
    61
    62
    63	# --------------------------------------------------
    64	if __name__ == '__main__':
    65	    main()
````

What happens if you try to initialize a script when one already exists with that name?

````
$ new_py.py foo
"foo.py" exists.  Overwrite? [yN] n
Will not overwrite. Bye!
````

Unless you answer "y", the script will not be overwritten. You could also use the `-f|--force` flag to force the overwritting of an existing file. 

In my experience, perhaps 20-50% of the effort to solve most of the exercises can be handled by using `argparse` well. You can specify an exact number of positional arguments, you can specify named arguments that must be constrained to a list of choices, you can force one argument to be an `int` and another to be a `float`, you can get Boolean flags or ensure that arguments are existing files that can be opened and read. I urge you to read the documentation for `argparse` thoroughly. I often find the REPL is quite useful for this:

````
>>> import argparse
>>> help(argparse)
````

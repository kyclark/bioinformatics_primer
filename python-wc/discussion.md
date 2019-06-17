The program needs to take a list of files, so we use the `nargs='+'` to indicate one or more and `type=argparse.FileType('r')` to say they must be "readable" (`'r'`) files. We can use a `for fh in args.file` to iterate over the file handles (hence the name `fh`). We want to initialize counters for `chars`, `words`, and `lines` with the value `0` which we can do with a shorthand unpacking of the tuple `(0, 0, 0)` (parentheses not strictly necessary) on line 30. We can then iterate each line in the open file handle with `for line in fh` and do:

1. Increment `lines` by `1`
2. Increment `chars` by the length of the `line` (number of characters)
3. Increment `words` by the length of the list created by splitting the `line` on spaces

Finally we need to print output similar to the actual `wc` program which appears to right-justify each of the numbers for lines, words, and characters in a column 8-characters wide followed by a space and then the name of the file. The call `'{:8}'.format()` will format a string into 8 characters, but they will be left-justified:

````
>>> '{:8}'.format('hello')
'hello   '
````

We can add `>` to right-justify. (Think of it like an arrow pointing to the right where you want the text.)

````
>>> '{:>8}'.format('hello')
'   hello'
````

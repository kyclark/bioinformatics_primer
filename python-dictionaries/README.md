# Introduction to Python Dictionaries

> Sometimes I feel like my job is deeply meaningful and then I remember that at the end of the day most of what I do is asking students to read error messages from compilers. -- Kristopher Micinski

In addition to lists and tuples, Python has a data type called a "dictionary" that allows you to associate some "key" (often a string but it could be a number or even a tuple) to some "value" (which can be anything such as a string, number, tuple, list, set, or another dictionary).  The same data structure in other languages is also called a map, hash, and associative array.

You can define the define a dictionary with all the key/value pairs using the `{}` ("curly") braces:

````
>>> patch = {'species': 'dog', 'age': 4}
>>> patch
{'species': 'dog', 'age': 4}
````

Or you can use the `dict` function and "keyword" arguments (which, in Pythonic style, do not use spaces around the `=` but the whitespace is not actually significant!):

````
>>> patch = dict(species='dog', age=4)
>>> patch
{'species': 'dog', 'age': 4}
````

You might be tempted to use the `{}` curly brackets to access the keys (e.g., if you were coming from Perl or you thought the language might be somehow internally consistent), but Python uses the `[]` square brackets to access dictionary fields just like lists and tuples:

````
>>> patch['species']
'dog'
````

Since a dictionary key may be an integer, it can lead to dictionaries looking like arrays:

````
>>> patch[0] = 'food'
>>> patch[0]
'food'
````

Note that the data types of keys of the dictionary, like lists, may be heterogenous:

````
>>> patch
{'species': 'dog', 'age': 4, 0: 'food'}
>>> list(map(type, patch.keys()))
[<class 'str'>, <class 'str'>, <class 'int'>]
````

As may be the values:

````
>>> type(patch['species'])
<class 'str'>
>>> patch['age']
4
>>> type(patch['age'])
<class 'int'>
>>> patch['likes'] = ['walking', 'running', 'car trips']
>>> patch
{'species': 'dog', 'age': 4, 0: 'food', 'likes': ['walking', 'running', 'car trips']}
<class 'list'>
>>> list(map(type, patch.values()))
[<class 'str'>, <class 'int'>, <class 'str'>, <class 'list'>]
````

You can directly use the dictionary values like the data types they are. Here we `join` the `list` that is in the `likes` slot:

````
>>> 'Patch is {} and likes {}.'.format(patch['age'], ', '.join(patch['likes']))
'Patch is 4 and likes walking, running, car trips.'
````

If you want to know if a key exists, use `in` just as we did for list membership:

````
>>> 'likes' in patch
True
>>> 'dislikes' in patch
False
````

Just as you should not request a list position that does not exist in the list, you should not ask for a key that does not exist in a dictionary or you program will asplode at runtime:

````
>>> patch['dislikes']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'dislikes'
````

Better to check first:

````
>>> if 'dislikes' in patch:
...   print(patch['dislikes'])
... else:
...   print('Patch likes everything!')
...
Patch likes everything!
````

Or use the `get` method of the dictionary:

````
>>> patch.get('dislikes')
````

Wait, what did we get?

````
>>> type(patch.get('dislikes'))
<class 'NoneType'>
````

To find all the methods you can call on a dictionary, in the REPL type:

````
>>> help(dict)
````

Type `q` to "quit" the help. Use `/` to initiate a search, e.g., "/pop" to see how you can `pop` similar to the method in the `list` class.

If we return to our previous chapter's DNA base counter, we can use dictionaries for this:

````
$ cat -n dna3.py
     1	#!/usr/bin/env python3
     2
     3	import sys
     4	import os
     5
     6	def main():
     7	    args = sys.argv[1:]
     8
     9	    if len(args) != 1:
    10	        print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    11	        sys.exit(1)
    12
    13	    dna = args[0]
    14	    count = {}
    15	    for base in dna.lower():
    16	        if not base in count:
    17	            count[base] = 0
    18	        count[base] += 1
    19
    20	    counts = []
    21	    for base in "acgt":
    22	        num = count[base] if base in count else 0
    23	        counts.append(str(num))
    24
    25	    print(' '.join(counts))
    26
    27	if __name__ == '__main__':
    28	    main()
$ cat dna.txt
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
$ ./dna3.py `cat dna.txt`
20 12 17 21
````

This has the great advantage of not having to declare four variables to count the four bases. True, we're only checking (in line 21) for those four, but we can now count all the letters in any string.

Notice that we create a new dict on line 14 with empty curlies `{}`. On line 16, we have to check if the base exists in the dict; if it doesn't, we initialize it to 0, and then we increment it by one. In line 22, we have to be careful when asking for a key that doesn't exist. If we were counting a string of DNA like "AAAAAA," then there would be no C, G or T to report, so we have to use an `if/then` expression:

````
>>> seq = 'AAAAAA'
>>> counts = {}
>>> for base in seq:
...   if not base in counts:
...     counts[base] = 0
...   counts[base] += 1
...
>>> counts
{'A': 6}
>>> counts['G']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'G'
>>> g = counts['G'] if 'G' in counts else 0
````

Or we can use the `get` method of a dictionary to safely get a value by a key even if the key doesn't exist:

````
>>> counts.get('G')
>>> type(counts.get('G'))
<class 'NoneType'>
````

If you look at "dna4.py," you'll see it's exactly the same as "dna3.py" with this exception:

````
    23	counts = []
    24	for base in "acgt":
    25	    num = count.get(base, 0)
    26	    counts.append(str(num))
````

The `get` method will not blow up your program, and it accepts an optional second argument for the default value when nothing is present:

````
>>> cat.get('likes')
>>> type(cat.get('likes'))
<class 'NoneType'>
>>> cat.get('likes', 'Cats like nothing')
'Cats like nothing'
````

## Truthiness

Note that you might be tempted to write:

````
>>> cat.get('likes') or 'Cats like nothing'
'Cats like nothing'
````

Which appears to do the same thing, but compare with this:

````
>>> d = {'x': 0, 'y': '', 'z': None}
>>> for k in sorted(d.keys()):
...   print('{} = "{}"'.format(k, d.get(k) or 'NA'))
...
x = "NA"
y = "NA"
z = "NA"
>>> for k in sorted(d.keys()):
...   print('{} = "{}"'.format(k, d.get(k, 'NA')))
...
x = "0"
y = ""
z = "None"
````

This is a minor but potentially pernicious error due to Python's idea of Truthiness (tm):

````
>>> 1 == True
True
>>> 0 == False
True
````

The integer `1` is not actually the same thing as the boolean value `True`, but Python will treat it as such.  Vice verse for `0` and `False`.  The only true way to get around this is to explicitly check for `None`:

````
>>> for k in sorted(d.keys()):
...   val = d.get(k)
...   print('{} = "{}"'.format(k, 'NA' if val is None else val))
...
x = "0"
y = ""
z = "NA"
````

To get around the check, we could initialize the dict:

````
$ cat -n dna5.py
     1    #!/usr/bin/env python3
     2    """Tetra-nucleotide counter"""
     3
     4    import sys
     5    import os
     6
     7    args = sys.argv[1:]
     8
     9    if len(args) != 1:
    10        print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    11        sys.exit(1)
    12
    13    dna = args[0]
    14
    15    count = {'a': 0, 'c': 0, 'g': 0, 't': 0}
    16
    17    for base in dna.lower():
    18        if base in count:
    19            count[base] += 1
    20
    21    counts = []
    22    for base in "acgt":
    23        counts.append(str(count[base]))
    24
    25    print(' '.join(counts))
````

## Back To Our Program

Now when we check on line 18, we're only going to count bases that we initialized; further, we can then just use the `keys` method to get the bases:

````
$ cat -n dna5.py
     1    #!/usr/bin/env python3
     2    """Tetra-nucleotide counter"""
     3
     4    import sys
     5    import os
     6
     7    args = sys.argv[1:]
     8
     9    if len(args) != 1:
    10        print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    11        sys.exit(1)
    12
    13    dna = args[0]
    14
    15    count = {'a': 0, 'c': 0, 'g': 0, 't': 0}
    16
    17    for base in dna.lower():
    18        if base in count:
    19            count[base] += 1
    20
    21    counts = []
    22    for base in sorted(count.keys()):
    23        counts.append(str(count[base]))
    24
    25    print(' '.join(counts))
````

This kind of checking and initializing is so common that there is a standard module to define a dictionary with a default value.  Unsurprisingly, it is called "defaultdict":

````
$ cat -n dna6.py
     1    #!/usr/bin/env python3
     2    """Tetra-nucleotide counter"""
     3
     4    import sys
     5    import os
     6    from collections import defaultdict
     7
     8    args = sys.argv[1:]
     9
    10    if len(args) != 1:
    11        print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    12        sys.exit(1)
    13
    14    dna = args[0]
    15
    16    count = defaultdict(int)
    17
    18    for base in dna.lower():
    19        count[base] += 1
    20
    21    counts = []
    22    for base in "acgt":
    23        counts.append(str(count[base]))
    24
    25    print(' '.join(counts))
````

On line 16, we create a `defaultdict` with the `int` type (not in quotes) for which the default value will be zero:

````
>>> from collections import defaultdict
>>> counts = defaultdict(int)
>>> counts['a']
0
````

Finally, I will show you the `Counter` that will do all the base-counting for you, returning a `defaultdict`:

````
>>> from collections import Counter
>>> c = Counter('AACTAC')
>>> c['A']
3
>>> c['G']
0
````

And here is it in the script:

````
 $ cat -n dna7.py
     1    #!/usr/bin/env python3
     2    """Tetra-nucleotide counter"""
     3
     4    import sys
     5    import os
     6    from collections import Counter
     7
     8    args = sys.argv[1:]
     9
    10    if len(args) != 1:
    11        print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    12        sys.exit(1)
    13
    14    dna = args[0]
    15
    16    count = Counter(dna.lower())
    17
    18    counts = []
    19    for base in "acgt":
    20        counts.append(str(count[base]))
    21
    22    print(' '.join(counts))
````

So we can take that and create a program that counts all characters either from the command line or a file:

````
$ cat -n char_count1.py
     1    #!/usr/bin/env python3
     2    """Character counter"""
     3
     4    import sys
     5    import os
     6    from collections import Counter
     7
     8    args = sys.argv
     9
    10    if len(args) != 2:
    11        print('Usage: {} INPUT'.format(os.path.basename(args[0])))
    12        sys.exit(1)
    13
    14    arg = args[1]
    15    text = ''
    16    if os.path.isfile(arg):
    17        text = ''.join(open(arg).read().splitlines())
    18    else:
    19        text = arg
    20
    21    count = Counter(text.lower())
    22
    23    for letter, num in count.items():
    24        print('{} {:5}'.format(letter, num))
$ ./char_count1.py input.txt
a    20
g    17
c    12
t    21
````

## Methods

The `keys` from a dict are in no particular order:

````
>>> c = Counter('AAACTAGGGACTGA')
>>> c
Counter({'A': 6, 'G': 4, 'C': 2, 'T': 2})
>>> c.keys()
dict_keys(['A', 'C', 'T', 'G'])
````

If you want them sorted, you must be explicit:

````
>>> sorted(c.keys())
['A', 'C', 'G', 'T']
````

Note that, unlike a list, you cannot call `sort` which makes sense as that will try to sort a list in-place:

````
>>> c.keys().sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict_keys' object has no attribute 'sort'
````

You can also just call `values` to get those:

````
>>> c.values()
dict_values([6, 2, 2, 4])
````

Often you will want to go through the `items` in a dict and do something with the key and value:

````
>>> for base, count in c.items():
...   print('{} = {}'.format(base, count))
...
A = 6
C = 2
T = 2
G = 4
````

But if you want to have the `keys` in a particular order, you can do this:

````
>>> for base in sorted(c.keys()):
...   print('{} = {}'.format(base, c[base]))
...
A = 6
C = 2
G = 4
T = 2
````

Or you can notice that `items` returns a list of tuples:

````
>>> c.items()
dict_items([('A', 6), ('C', 2), ('T', 2), ('G', 4)])
````

And you can call `sorted` on that:

````
>>> sorted(c.items())
[('A', 6), ('C', 2), ('G', 4), ('T', 2)]
````

Which means this will work:

````
>>> for base, count in sorted(c.items()):
...   print('{} = {}'.format(base, count))
...
A = 6
C = 2
G = 4
T = 2
````

Note that `sorted` will sort by the first elements of all the tuples, then by the second, and so forth:

````
>>> genes = [('Indy', 4), ('Boss', 2), ('Lush', 10), ('Boss', 4), ('Lush', 1)]
>>> sorted(genes)
[('Boss', 2), ('Boss', 4), ('Indy', 4), ('Lush', 1), ('Lush', 10)]
````

If we want to sort the bases instead by their frequency, we have to use some trickery like a list comprehension to first reverse the tuples:

````
>>> [(x[1], x[0]) for x in c.items()]
[(6, 'A'), (2, 'C'), (2, 'T'), (4, 'G')]
>>> sorted([(x[1], x[0]) for x in c.items()])
[(2, 'C'), (2, 'T'), (4, 'G'), (6, 'A')]
````

But what is particularly nifty about Counters is that they have built-in methods to help you with such actions:

````
>>> c.most_common(2)
[('A', 6), ('G', 4)]
>>> c.most_common()
[('A', 6), ('G', 4), ('C', 2), ('T', 2)]
````

You should read the documentation to learn more ([https://docs.python.org/3/library/collections.html\](https://docs.python.org/3/library/collections.html%29).

## Character Counter with the works

Finally, I'll show you a version of the character counter that takes some other arguments to control how to show the results:

````
$ cat -n char_count2.py
     1	#!/usr/bin/env python3
     2	"""
     3	Author : Ken Youens-Clark <kyclark@email.arizona.edu>
     4	Date   : 2019-02-06
     5	Purpose: Character Counter
     6	"""
     7
     8	import argparse
     9	import os
    10	import sys
    11	from collections import Counter
    12
    13
    14	# --------------------------------------------------
    15	def get_args():
    16	    """get command-line arguments"""
    17	    parser = argparse.ArgumentParser(
    18	        description='Character counter',
    19	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    20
    21	    parser.add_argument('input', help='Filename or string to count', type=str)
    22
    23	    parser.add_argument(
    24	        '-c',
    25	        '--charsort',
    26	        help='Sort by character',
    27	        dest='charsort',
    28	        action='store_true')
    29
    30	    parser.add_argument(
    31	        '-n',
    32	        '--numsort',
    33	        help='Sort by number',
    34	        dest='numsort',
    35	        action='store_true')
    36
    37	    parser.add_argument(
    38	        '-r',
    39	        '--reverse',
    40	        help='Sort in reverse order',
    41	        dest='reverse',
    42	        action='store_true')
    43
    44	    return parser.parse_args()
    45
    46
    47	# --------------------------------------------------
    48	def warn(msg):
    49	    """Print a message to STDERR"""
    50	    print(msg, file=sys.stderr)
    51
    52
    53	# --------------------------------------------------
    54	def die(msg='Something bad happened'):
    55	    """warn() and exit with error"""
    56	    warn(msg)
    57	    sys.exit(1)
    58
    59
    60	# --------------------------------------------------
    61	def main():
    62	    """Make a jazz noise here"""
    63	    args = get_args()
    64	    input_arg = args.input
    65	    charsort = args.charsort
    66	    numsort = args.numsort
    67	    revsort = args.reverse
    68
    69	    if charsort and numsort:
    70	        die('Please choose one of --charsort or --numsort')
    71
    72	    if not charsort and not numsort:
    73	        charsort = True
    74
    75	    text = ''
    76	    if os.path.isfile(input_arg):
    77	        text = ''.join(open(input_arg).read().splitlines())
    78	    else:
    79	        text = input_arg
    80
    81	    count = Counter(text.lower())
    82
    83	    if charsort:
    84	        letters = sorted(count.keys())
    85	        if revsort:
    86	            letters.reverse()
    87
    88	        for letter in letters:
    89	            print('{} {:5}'.format(letter, count[letter]))
    90	    else:
    91	        pairs = sorted([(x[1], x[0]) for x in count.items()])
    92	        if revsort:
    93	            pairs.reverse()
    94
    95	        for n, char in pairs:
    96	            print('{} {:5}'.format(char, n))
    97
    98
    99	# --------------------------------------------------
   100	if __name__ == '__main__':
   101	    main()
````


## Sequence Similarity

We can use dictionaries to count how many words are in common between any two texts.  Since I'm only trying to see if a word is present, I can use a `set` which is like a `dict` where the values are just "1."  Here is the code:

````
$ cat -n common_words.py
     1    #!/usr/bin/env python3
     2    """Count words in common between two files"""
     3
     4    import os
     5    import re
     6    import sys
     7    import string
     8
     9    # --------------------------------------------------
    10    def main():
    11        files = sys.argv[1:]
    12
    13        if len(files) != 2:
    14            msg = 'Usage: {} FILE1 FILE2'
    15            print(msg.format(os.path.basename(sys.argv[0])))
    16            sys.exit(1)
    17
    18        for file in files:
    19            if not os.path.isfile(file):
    20                print('"{}" is not a file'.format(file))
    21                sys.exit(1)
    22
    23        file1, file2 = files[0], files[1]
    24        words1 = uniq_words(file1)
    25        words2 = uniq_words(file2)
    26        common = words1.intersection(words2)
    27        num_common = len(common)
    28        msg = 'There {} {} word{} in common between "{}" and "{}."'
    29        print(msg.format('is' if num_common == 1 else 'are',
    30                         num_common,
    31                         '' if num_common == 1 else 's',
    32                         os.path.basename(file1),
    33                         os.path.basename(file2)))
    34
    35        for i, word in enumerate(sorted(common)):
    36            print('{:3}: {}'.format(i + 1, word))
    37
    38    # --------------------------------------------------
    39    def uniq_words(file):
    40        regex = re.compile('[' + string.punctuation + ']')
    41        words = set()
    42        for line in open(file):
    43            for word in [regex.sub('', w) for w in line.lower().split()]:
    44                words.add(word)
    45
    46        return words
    47
    48    # --------------------------------------------------
    49    if __name__ == '__main__':
    50        main()
````

Let's see it in action using a common nursery rhyme and a poem by William Blake (1757-1827):

````
$ cat mary-had-a-little-lamb.txt
Mary had a little lamb,
It's fleece was white as snow,
And everywhere that Mary went,
The lamb was sure to go.
$ cat little-lamb.txt
Little Lamb, who made thee?
Dost thou know who made thee?
Gave thee life, & bid thee feed
By the stream & o'er the mead;
Gave thee clothing of delight,
Softest clothing, wooly, bright;
Gave thee such a tender voice,
Making all the vales rejoice?
Little Lamb, who made thee?
Dost thou know who made thee?
Little Lamb, I'll tell thee,
Little Lamb, I'll tell thee,
He is called by thy name,
For he calls himself a Lamb.
He is meek, & he is mild;
He became a little child.
I a child, & thou a lamb,
We are called by his name.
Little Lamb, God bless thee!
Little Lamb, God bless thee!
$ ./common_words.py mary-had-a-little-lamb.txt little-lamb.txt
There are 4 words in common between "mary-had-a-little-lamb.txt" and "little-lamb.txt."
  1: a
  2: lamb
  3: little
  4: the
````

Well, that's pretty uninformative.  Sure "a" and "the" are shared, but we don't much care about those.  And while "little" and "lamb" are present, it hardly tells us about how prevalent they are.  In the nursery rhyme, they occur a total of 3 times, but they make up a significant portion of the Blake poem.  Let's try to work in word frequency:

````
$ cat -n common_words2.py
     1    #!/usr/bin/env python3
     2    """Count words/frequencies in two files"""
     3
     4    import os
     5    import re
     6    import sys
     7    import string
     8    from collections import defaultdict
     9
    10    # --------------------------------------------------
    11    def word_counts(file):
    12        """Return a dictionary of words/counts"""
    13        words = defaultdict(int)
    14        regex = re.compile('[' + string.punctuation + ']')
    15        for line in open(file):
    16            for word in [regex.sub('', w) for w in line.lower().split()]:
    17                words[word] += 1
    18
    19        return words
    20
    21    # --------------------------------------------------
    22    def main():
    23        """Start here"""
    24        args = sys.argv[1:]
    25
    26        if len(args) != 2:
    27            msg = 'Usage: {} FILE1 FILE2'
    28            print(msg.format(os.path.basename(sys.argv[0])))
    29            sys.exit(1)
    30
    31        for file in args[0:2]:
    32            if not os.path.isfile(file):
    33                print('"{}" is not a file'.format(file))
    34                sys.exit(1)
    35
    36        file1 = args[0]
    37        file2 = args[1]
    38        words1 = word_counts(file1)
    39        words2 = word_counts(file2)
    40        common = set(words1.keys()).intersection(set(words2.keys()))
    41        num_common = len(common)
    42        verb = 'is' if num_common == 1 else 'are'
    43        plural = '' if num_common == 1 else 's'
    44        msg = 'There {} {} word{} in common between "{}" ({}) and "{}" ({}).'
    45        tot1 = sum(words1.values())
    46        tot2 = sum(words2.values())
    47        print(msg.format(verb, num_common, plural, file1, tot1, file2, tot2))
    48
    49        if num_common > 0:
    50            fmt = '{:>3} {:20} {:>5} {:>5}'
    51            print(fmt.format('#', 'word', '1', '2'))
    52            print('-' * 36)
    53            shared1, shared2 = 0, 0
    54            for i, word in enumerate(sorted(common)):
    55                c1 = words1[word]
    56                c2 = words2[word]
    57                shared1 += c1
    58                shared2 += c2
    59                print(fmt.format(i + 1, word, c1, c2))
    60
    61            print(fmt.format('', '-----', '--', '--'))
    62            print(fmt.format('', 'total', shared1, shared2))
    63            print(fmt.format('', 'pct',
    64                             int(shared1/tot1 * 100), int(shared2/tot2 * 100)))
    65
    66    # --------------------------------------------------
    67    if __name__ == '__main__':
    68        main()
````

And here it is in action:

````
$ ./common_words2.py mary-had-a-little-lamb.txt little-lamb.txt
There are 4 words in common between "mary-had-a-little-lamb.txt" (22) and "little-lamb.txt" (113).
  # word                     1     2
------------------------------------
  1 a                        1     5
  2 lamb                     2     8
  3 little                   1     7
  4 the                      1     3
    -----                   --    --
    total                    5    23
    pct                     22    20
````

It is interesting (to me, at least) that the shared content actually works out to about the same proportion no matter the direction.  Imagine comparing a large genome to a smaller one -- what is a significant portion of shared sequence space from the smaller genome might be only a small fraction of the larger one.  Here we see that just those few words make up an equivalent proportion of both texts because of how repeated the words are in the Blake poem.

This is all pretty good as long as the words are spelled the same, but take the two texts here that show variations between British and American English:

````
$ cat british.txt
I went to the theatre last night with my neighbour and had a litre of
beer, the colour and flavour of which put us into such a good humour
that we forgot our labours.  We set about to analyse our behaviour,
organise our thoughts, recognise our faults, catalogue our merits, and
generally have a dialogue without pretence as a licence to improve
ourselves.
$ cat american.txt
I went to the theater last night with my neighbor and had a liter of
beer, the color and flavor of which put us into such a good humor that
we forgot our labors.  We set about to analyze our behavior, organize
our thoughts, recognize our faults, catalog our merits, and generally
have a dialog without pretense as a license to improve ourselves.
$ ./common_words2.py british.txt american.txt
There are 34 words in common between "british.txt" (63) and "american.txt" (63).
  # word                     1     2
------------------------------------
  1 a                        4     4
  2 about                    1     1
  3 and                      3     3
  4 as                       1     1
  5 beer                     1     1
  6 faults                   1     1
  7 forgot                   1     1
  8 generally                1     1
  9 good                     1     1
 10 had                      1     1
 11 have                     1     1
 12 i                        1     1
 13 improve                  1     1
 14 into                     1     1
 15 last                     1     1
 16 merits                   1     1
 17 my                       1     1
 18 night                    1     1
 19 of                       2     2
 20 our                      5     5
 21 ourselves                1     1
 22 put                      1     1
 23 set                      1     1
 24 such                     1     1
 25 that                     1     1
 26 the                      2     2
 27 thoughts                 1     1
 28 to                       3     3
 29 us                       1     1
 30 we                       2     2
 31 went                     1     1
 32 which                    1     1
 33 with                     1     1
 34 without                  1     1
    -----                   --    --
    total                   48    48
    pct                     76    76
````

Obviously we will miss all those words because the are not spelled exactly the same.  Neither are genomes.  So we need a way to decide if two words or sequences are similar enough.  One way is through sequence alignment:

````
l a b o u r      c a t a l o g u e      p r e t e n c e     l i t r e
| | | |   |      | | | | | | |          | | | | | |   |     | | | 
l a b o   r      c a t a l o g          p r e t e n s e     l i t e r
````

Try writing a sequence alignment program (no, really!), and you'll find it's really quite difficult.  Decades of research have gone into Smith-Waterman and BLAST and BLAT and LAST and more.  Alignment works very well, but it's computationally expensive.  We need a faster approximation of similarity.  Enter k-mers!

A k-mer is a `k` length of "mers" or contiguous sequence (think "polymers").  Here are the 3/4-mers in my last name:

````
$ ./kmer_tiler.py youens
There are 4 3-mers in "youens."
youens
you
 oue
  uen
   ens
$ ./kmer_tiler.py youens 4
There are 3 4-mers in "youens."
youens
youe
 ouen
  uens
````

If instead looking for shared "words" we search for k-mers, we will find very different results, and the length of the k-mer matters.  For instance, the first 3-mer in my name, "you" can be found 81 times in my local dictionary, but the 4-mer "youe" not at all.  The longer the k-mer, the greater the specificity.  Let's try our English variations with a k-mer counter:

````
$ ./common_kmers.py british.txt american.txt
There are 112 kmers in common between "british.txt" (127) and "american.txt" (127).
  # kmer                     1     2
------------------------------------
  1 abo                      2     2
  2 all                      1     1
...
111 whi                      1     1
112 wit                      2     2
    -----                   --    --
    total                  142   133
    pct                     86    86
````

Our word counting program thought these two texts only 76% similar, but our kmer counter thinks they are 86% similar.


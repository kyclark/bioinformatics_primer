# Hello: Named Command-line Options

Write a Python program called `hello.py` that accepts three named arguments, `-g|--greeting` which is the greeting, `-n|--name` which is the name, and `-e|--excited` which is a flag to indicate whether to use a "!" in the output `<greeting>, <name><punctuation>`.

````
$ ./hello.py -h
usage: hello.py [-h] [-g str] [-n str] [-e]

Greetings and saluatations

optional arguments:
  -h, --help            show this help message and exit
  -g str, --greeting str
                        The greeting (default: Hello)
  -n str, --name str    The name (default: World)
  -e, --excited         Whether to use an "!" (default: False)
$ ./hello.py
Hello, World.
$ ./hello.py -g Howdy
Howdy, World.
$ ./hello.py -n Stranger
Hello, Stranger.
$ ./hello.py --name Pig --greeting "That'll do"
That'll do, Pig.
$ ./hello.py -n Gracie -g 'Good Night' -e
Good Night, Gracie!
````

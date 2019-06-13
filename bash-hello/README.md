# "Hello" in bash

Create a bash script called `hello.sh` that accepts one or two arguments. If there are no arguments, it should print a "Usage" and exit *with an error code*. Your program will expect to receive a "greeting" in `$1` and possibly a name in `$2`; if there is no second argument, use "Human" as the default. If there are more than two arguments, print a "Usage" and exit *with an error code*. Print the greeting, a comma and space, the name, and an exclamation point.


````
$ ./hello.sh
Usage: hello.sh GREETING [NAME]
$ ./hello.sh That\'ll do pig
Usage: hello.sh GREETING [NAME]
$ ./hello.sh "That'll do" pig
That'll do, pig!
$ ./hello.sh "Top o' the morning"
Top o' the morning, Human!
$ ./hello.sh "Greetings" "Earthling"
Greetings, Earthling!
````


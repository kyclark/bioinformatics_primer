# head.sh

Write a bash script called `head.sh` that mimics the `head` utility where it will print the first few lines of a file.  The script should expect one required argument (the file) and a second optional argument of the number of lines, defaulting to 3. If are no arguments, it should print a "Usage" and exit *with an error code* Your program will expect to receive an argument in `$1` and maybe a second in `$2`. If the first argument is not a file, it should notify the user and exit *with an error code*. If the second argument is missing, use the value "3". Print the number of lines requested by the user by iterating over the lines in the file and exiting the loop appropriately. Do not use the actual `head` command!

````
$ ./head.sh
Usage: head.sh FILE NUM
$ ./head.sh files/issa.txt
Selected Haiku by Issa

Don’t worry, spiders,
$ ./head.sh files/issa.txt 5
Selected Haiku by Issa

Don’t worry, spiders,
I keep house
casually.
````

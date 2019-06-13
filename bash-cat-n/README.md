# cat_n.sh

Write a bash program called `cat_n.sh` that mimics the behavior of `cat -n` where it will print the line number and line of an input file. If there are no arguments, it should print a "Usage" and exit *with an error code*. Your program will expect to receive an argument in `$1`. If the argument is not a file, it should notify the user and exit *with an error code*. It will iterate over the lines in the file and print the line number, a space, and the line of the file. Your output will differ from regular `cat -n` as I won't expect you to right-align the numbers. 

````
$ ./cat_n.sh
Usage: cat-n.sh FILE
$ ./cat_n.sh foo
foo is not a file
$ ./cat_n.sh files/sonnet-29.txt
1 Sonnet 29
2 William Shakespeare
3
4 When, in disgrace with fortune and men’s eyes,
5 I all alone beweep my outcast state,
6 And trouble deaf heaven with my bootless cries,
7 And look upon myself and curse my fate,
8 Wishing me like to one more rich in hope,
9 Featured like him, like him with friends possessed,
10 Desiring this man’s art and that man’s scope,
11 With what I most enjoy contented least;
12 Yet in these thoughts myself almost despising,
13 Haply I think on thee, and then my state,
14 (Like to the lark at break of day arising
15 From sullen earth) sings hymns at heaven’s gate;
16 For thy sweet love remembered such wealth brings
17 That then I scorn to change my state with kings.
````

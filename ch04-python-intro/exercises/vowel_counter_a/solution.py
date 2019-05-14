#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com.>
Date   : 2019-05-14
Purpose: Count vowels in a string
"""

import os
import sys


# --------------------------------------------------
def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STR'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    word = args[0]
    lc_word = word.lower()

    # Method 1:
    # Create a variable to hold the count
    # Use a `for` loop to go through each character in the word
    # If that character is in the list of vowels, increment the counter
    count = 0
    for char in word.lower():
        if char in 'aeiou':
            count += 1

    # Method 2:
    # Create a variable to hold the count
    # Use a `for` loop to go through the list of vowels
    # Increment the count with the `str.count` function that will
    # find how many times the vowel occurs in the word
    # count = 0
    # for vowel in "aeiou":
    #     count += lc_word.count(vowel)

    # Method 3:
    # Use a list comprehension instead of a `for` loop to get a list 
    # of integers which are the counts for each vowel
    # Then use the `sum` function to add them together
    # count = sum([lc_word.count(v) for v in "aeiou"])

    # Method 4:
    # Replace the list comprehension with a `map`
    # count = sum(map(lc_word.count, "aeiou"))

    print('There {} {} vowel{} in "{}."'.format(
        'are' if count > 1 or count == 0 else 'is',
        count,
        '' if count == 1 else 's',
        word))


# --------------------------------------------------
if __name__ == '__main__':
    main()

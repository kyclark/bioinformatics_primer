#!/usr/bin/env python3
"""tests for article.py"""

from subprocess import getstatusoutput
import random
import string
import os

prg = './article.py'


# --------------------------------------------------
def test_usage():
    """usage"""
    rv, out = getstatusoutput(prg)
    assert rv > 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def make_word(start_vowel):
    vowels = 'aeiouAEIOU'
    cons = list(filter(lambda c: c not in vowels, string.ascii_letters))
    first = random.choice(vowels if start_vowel else cons)
    return first + ''.join(
        random.sample(string.ascii_letters, k=random.randint(5, 10)))


# --------------------------------------------------
def test_works():
    for _ in range(10):
        start_vowel = random.choice([True, False])
        word = make_word(start_vowel)
        rv, out = getstatusoutput('{} {}'.format(prg, word))
        assert rv == 0
        expected = '{} {}'.format('an' if start_vowel else 'a', word)
        assert out == expected

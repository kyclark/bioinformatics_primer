#!/usr/bin/env python3
"""tests for first_lines.py"""

import re
import os.path
from subprocess import getstatusoutput, getoutput

prg = './first_lines.py'


def test_usage():
    """usage"""

    (retval, out) = getstatusoutput(prg)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_bad_input():
    """fails on bad input"""

    rv, out = getstatusoutput('{} foo'.format(prg))
    assert rv == 0
    assert out.rstrip() == '"foo" is not a directory'


def test_good_input1():
    expected1 = """
dickinson
'T is so much joy! 'T is so much joy! ........ 4.txt
A precious, mouldering pleasure 't is ....... 10.txt
A wounded deer leaps highest, ................ 8.txt
Glee! The great storm is over! ............... 5.txt
I know some lonely houses off the road ...... 15.txt
If I can stop one heart from breaking, ....... 6.txt
Much madness is divinest sense .............. 11.txt
Our share of night to bear, .................. 2.txt
Some things that fly there be, -- ........... 14.txt
Soul, wilt thou toss again? .................. 3.txt
Success is counted sweetest .................. 1.txt
The heart asks pleasure first, ............... 9.txt
The soul selects her own society, ........... 13.txt
Within my reach! ............................. 7.txt
"""

    rv1, out1 = getstatusoutput('{} dickinson'.format(prg))
    assert rv1 == 0
    assert out1.strip() == expected1.strip()

def test_good_input2():
    expected2 = """
blake
Cruelty has a human heart, ............................. 4.txt
I dreamt a dream! What can it mean? .................... 5.txt
I was angry with my friend: ............................ 1.txt
Never seek to tell thy love, ........................... 6.txt
Sweet dreams form a shade, ............................. 7.txt
To see a World in a Grain of Sand ...................... 3.txt
Tyger! Tyger! burning bright, .......................... 2.txt
"""

    rv2, out2 = getstatusoutput('{} blake -w 60'.format(prg))
    assert rv2 == 0
    assert out2.strip() == expected2.strip()

def test_good_input3():
    expected3 = """
"foo" is not a directory
dickinson
'T is so much joy! 'T is so much joy! ............................ 4.txt
A precious, mouldering pleasure 't is ........................... 10.txt
A wounded deer leaps highest, .................................... 8.txt
Glee! The great storm is over! ................................... 5.txt
I know some lonely houses off the road .......................... 15.txt
If I can stop one heart from breaking, ........................... 6.txt
Much madness is divinest sense .................................. 11.txt
Our share of night to bear, ...................................... 2.txt
Some things that fly there be, -- ............................... 14.txt
Soul, wilt thou toss again? ...................................... 3.txt
Success is counted sweetest ...................................... 1.txt
The heart asks pleasure first, ................................... 9.txt
The soul selects her own society, ............................... 13.txt
Within my reach! ................................................. 7.txt
whitman
A sight in camp in the daybreak gray and dim, .................... 1.txt
I have said that the soul is not more than the body, ............. 2.txt
Passing stranger! you do not know how longingly I look upon you, . 4.txt
Shut not your doors to me, proud libraries, ...................... 5.txt
We two, how long we were fool’d, ................................. 3.txt
"""

    rv3, out3 = getstatusoutput('{} dickinson foo whitman -w 70'.format(prg))
    assert rv3 == 0
    assert out3.strip() == expected3.strip()

#!/usr/local/bin/python

import sys # Load a library module
print(sys.platform)

print("My first simple Python script!")
print('Spam!' * 8)

for x in 'spam':
  print(x)

print('%s, eggs, and %s' % ('spam', 'SPAM!')) 

import math
print(math.pi)

import random
print(random.random())
print(random.choice([1, 2, 3, 4]))

M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists
     [4, 5, 6], # Code can span lines if bracketed
     [7, 8, 9]]

print(M[1][2])

squares = []
for x in [1, 2, 3, 4, 5]: # This is what a list comprehension does
   squares.append(x ** 2)

print(squares[3])

a = 3 # It's an integer
print(a) 
a = 'spam' # Now it's a string
print(a) 
a = 1.23 # Now it's a floating point
print(a) 

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True) # Change sort order
print(L)

table = {'Holy Grail': '1975', # Key=>Value (title=>year)
'Life of Brian': '1979',
'The Meaning of Life': '1983'}

print(table['Holy Grail'])

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T) # Make a list from a tuple's items
tmp.sort() # Sort the list
print(T)
print(tmp)

bob = ('Bob', 40.5, ['dev', 'mgr']) # Tuple record
print(bob)
('Bob', 40.5, ['dev', 'mgr'])
print(bob[0], bob[2]) # Access by position

#The indention rule ...
#The indentation rule may seem unusual at first glance to programmers accustomed to
#C-like languages, but it is a deliberate feature of Python, and it’s one of the main ways
#that Python almost forces programmers to produce uniform, regular, and readable

# Explain the difference between the following commented out code fragments in C and in Python...
# 
# In c that doesn't use indention ->
#if (x)
#if (y)
#statement1;
#else
#statement2;

# In Python that does ->
# if x:
#    if y:
#      statement1
# else:
#    statement2

while True:
   reply = input('Enter text:')
   if reply == 'stop': break
   print(reply.upper())

while True:
   reply = input('Enter number:')
   if reply == 'stop': break
   print(int(reply) ** 2)
print('Done doing squares')

while True:
   reply = input('Enter number v2:')
   if reply == 'stop':
     break
   elif not reply.isdigit():
     print('Bad!' * 8)
   else:
     print(int(reply) ** 2)
print('Even more done doing squares')

L = [1, 2, 3, 4, 5]
for i in range(len(L)):
   L[i] += 10
print(L)

def times(x, y): # Create and assign function
   return x * y # Body executed when called

print(times(2,12))

def tricky(x, y): # Create and assign function
   z = 2
   return x * y + z # Body executed when called

z = 3
print(tricky(2,3))

X = 99
def func1():
   global X
   X = 88 

def func2():
   global X
   X = 77

def func3():
   X = 3

func1()

func2()

func3()

print(X) # What is x ?

def f(a): # a is assigned to (references) the passed object
   a = 99 # Changes local variable a only

b = 88
f(b) # a and b both reference same 88 initially
print(b)

f = lambda x, y, z: x + y + z
d = f(2, 3, 4)
print(d)

key = 'got'
s= {'already': (lambda: 2 + 2),
'got': (lambda: 2 ** 4),
'one': (lambda: 2 ** 6)}[key]()

print(s)

# Both howdy functions simply sum N integers, with N defaulted to 10 million.
def howdy1(N=10000000):
    total = 0
    for i in range(N):
        total += i
    return total
 
def howdy2(N=10000000):
    total = sum(range(N))
    return total

print(howdy1())

print(howdy2())

import time
t0 = time.time()  # start time
print(howdy1())
t1 = time.time()  # time
print("howdy1(): %f" % (t1 - t0))
print(howdy1())
t2 = time.time()  # time
print("howdy2(): %f" % (t2 - t1))

# try running this from Linux and Windows - same processing time
# on the same machine?

import module1 # File a.py
module1.spam('gumby') # Prints "gumby spam" ? 

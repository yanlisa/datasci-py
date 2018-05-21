'''
Loops and recursion.
'''
from util import *

'''
Exercise 1:
Implement a half-life function that uses a while loop.
f(a,t) = a * (1/2)^t
Input:
  a: a float
  t: an integer or float
Returns:
  f(a,t)
'''
def half_life_while(a, t):
  return 1 # delete this line and write your code

'''
Exercise 2:
Implement a half-life function that uses a for loop.
'''
def half_life_for(a, t):
  return 1 # delete this line and write your code

'''
Exercise 3:
Implement factorial using recursion.
Recall that n! = n * (n - 1) * ... 1
For simplicity, assume that 0! = (-1)! = 0.
Input:
  n: an integer
Returns:
  the value of n!
'''
def factorial_recur(n):
  return 0 # delete this line and write your code

'''
Exercise 4:
Implement fibonacci using recursion.
Input:
  n: an integer
Returns:
  the nth fibonacci number
'''
def fib(n):
  return 1 # delete this line and write your code

'''
Exercise 5:
Implement the combination function.
  Recall nCr = n!/((n-r)!r!)

Write your own function and call it combination.
Use the factorial_iter function located in util.py; it has already
  been imported for you so you just need to call factorial_iter(number)
Input: 
  n: an integer
  r: an integer
Output:
  the value of n choose r
'''

############################# Test cases ######################################
def test_factorial():
  test_cases = [3, 5, -1, 1, 10]
  print('>>> Testing recursive factorial...')
  for test_case in test_cases:
    recur_val = factorial_recur(test_case)
    iter_val = factorial_iter(test_case)
    if recur_val != iter_val:
      print('{}!\tFAIL: Expected {} but got {}'.format(
            test_case, iter_val, recur_val))
    else:
      print('{}!\tPASS: {}'.format(test_case, recur_val))
  print()

def test_fib():
  test_cases = [1, 2, 3, 4]
  print('>>> Testing recursive fibonacci...')
  for test_case in test_cases:
    print('fib({}) = {}'.format(test_case, fib(test_case)))
  print()

def test_half_life():
  test_cases = [(100, 2), (1, 4), (50, 75)]
  print('>>> Testing half-life...')
  for a, t in test_cases:
    print('a:{}, t:{}\t{}, {}'.format(
      a, t, half_life_while(a, t), half_life_while(a, t)))
  print()
################################## main #######################################
if __name__ == "__main__":
  test_half_life()
  test_factorial()
  test_fib()

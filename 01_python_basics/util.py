import math
import os
import operator
import time

##### For problem 1
def max_list_positive(items):
  max_item = -1
  for item in items:
    if item > max_item:
      max_item = item
  return max_item

def simple_max_list(items):
  # edit the below line by returning a call to the max() function
  return [] # delete this line and replace

##### For problem 2
def factorial_iter(n):
  if n < 1: return 0
  prod = 1
  for i in range(1, n+1):
    prod *= i
  return prod

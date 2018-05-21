import csv
import math
import os
import operator
import time
import numpy as np

##### For lecture
"""
Write a function that takes in a list of lists
and writes a csv to a specified filepath such that
the first list in the list corresponds to the elements
in the first row, and so on.

Note that the sublists (i.e., the elements in the argument)
do not have to all have the same length. In addition, the
elements of each sublist do not have to be strings.

You should also account for the case where an element in
a sublist can contain commas. For these cases, you should
encapsulate the element with double quotes. You can assume
that all elements do not have double quotes to begin with.

Finally, you should print out confirmation that you wrote
to a destination file by including the following at the end
of your implementation:
  if log:
    print('Wrote csv to', fpath)

Input:
  fpath: a filepath (a string)
  tups: list of lists, where each element may not necessarily be a string
Returns:
  nothing

Hints:
  Use csv.writer. Look at the example in the Python documentation:
  https://docs.python.org/3/library/csv.html#csv.writer
"""
def write_csv(fpath, tups, log=True):
  # your code here
  pass # delete this line


"""
You should write all of your functions in this file. That way we can
use parts of this file later in the course.
"""
# this line imports numpy as np, csv, os, etc.
from util import *
################################ Constants ####################################
# degree -> salaries
# college -> salaries
# Note that we do not save the percent change between starting/mid salary.
START_SAL, MED_SAL, MID_10, MID_25, MID_75, MID_90 = range(6)

################################ Loading ######################################
"""
Write your load_degrees(...) function here.
Hints:
- use f.readline() to read the first line, then
- use csv.reader() to parse the rest of the file
- use s.replace(old, new) to remove commas from the dollar amounts
- use s.strip(characters) to remove leading/trailing characters like $ sign
- use items.index(s) to find the index of a particular string.
- use items.pop(n) to remove the nth element from the string (indexed from 0)
- if your list of strings is called line,
       use line[1:] to access the second element onwards
"""
def load_degrees(degree_fpath):
  degree_dict = {}
  headers = []
  # your code here
  return headers, degree_dict

"""
Write your load_colleges(...) function here.
Hints:
- some schools appear in both CSVs, but their salary values are the 
  same in both sheets. However, you should make sure you still parse those 
  lines as they will contain information about the school region or type.
- the headers for the college_dict values will
  be the same as those for the degree_dict from load_degrees(...), so we
  do not need to redefine those.
- ```type``` is a keyword, so use a different name (e.g., college_type)
- N/A should be represented as -1.
- For the latter two dictionaries, check if the type/region exists in
  the dictionary first. If it doesn't, create an empty list as the value.
  Then add the college name to the list.
- If a school already exists in college_dict, you can either use the 
  ```continue``` keyword to go to the next line, or you can encapsulate what
  you have in a conditional.
"""
def load_colleges(salaries_type_fpath ,salaries_region_fpath):
  college_dict, type_to_colleges, region_to_colleges = {}, {}, {}
  # your code here

  return college_dict, type_to_colleges, region_to_colleges

"""
Write your write_colleges(...) function here.
The CSV should be sorted by the name of the college.
Hints:
- Create a new dictionary with college names as the keys, and
  the college region and college type as values.
- The default is N/A for both college region and college type.
- Go through the college keys in **sorted order** and create
  a list of lists, where each sublist is a row of the target csv.
- Use the write_csv function from util that you implemented in lecture.
"""
def write_colleges(college_fpath, salary_headers,
                college_dict, type_to_colleges, region_to_colleges):
  tups = []
  # your code here

  write_csv(college_fpath, tups, log=True)


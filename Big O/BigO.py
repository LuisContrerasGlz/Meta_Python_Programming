# O(1) - Constant Runtime

# returning the first element in the given data
def returnFirst(elements):
   return elements[0]


# O(n) - Linear Runtime

# searching for a particular value in a data set using an iteration
def constainsValue(elements, value):
  for element in elements:
    if (element == value):
        return True;
    return False

# O(n^2 ) - Quadratic Runtime
# a nested iteration or loop to check if the data set contains duplicates.

def constainsDuplicate(elements):
  for element in elements:
     for item in elements:
       if element == item:
        return True
  return False



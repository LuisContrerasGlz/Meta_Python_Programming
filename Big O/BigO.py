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

# O(log n) - Logarithmic runtime, E.G binary search

# O(n log n) - Linearithmic runtime, Most sorting algorithms have a runtime complexity of O(n log n)

# O(2^n ) - Exponential runtime, ecursive solution for finding Fibonacci numbers.

def fibonacci(num):
      if (num <= 1):
        return 1

      return fibonacci(num - 2) + fibonacci(num - 1)

# O(n!) - Factorial runtime, Any algorithm that performs permutation on a given data set is an example of O(n!)


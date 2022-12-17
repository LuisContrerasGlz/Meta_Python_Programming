# O(1) - Constant Runtime, your algorithm runs the same time, regardless of the given input data set.

# returning the first element in the given data
def returnFirst(elements):
   return elements[0]


# O(n) - Linear Runtime, occurs when the runtime grows in proportion with the size of the input data set. n is the size of the input data set.

# searching for a particular value in a data set using an iteration
def constainsValue(elements, value):
  for element in elements:
    if (element == value):
        return True;
    return False

# O(n^2 ) - Quadratic Runtime, algorithm whose runtime is directly proportional to the square of the size of the input data set. 
# a nested iteration or loop to check if the data set contains duplicates.

def constainsDuplicate(elements):
  for element in elements:
     for item in elements:
       if element == item:
        return True
  return False

# O(log n) - Logarithmic runtime, E.G binary search
# The runtime it takes for the algorithm to run will plateau no matter the size of the input data set. 

# O(n log n) - Linearithmic runtime, depends on running a logarithm operation n times. Most sorting algorithms have a runtime complexity of O(n log n)

# O(2^n ) - Exponential runtime, where for each increase in the size of the data set, the runtime is doubled. Recursive solution for finding Fibonacci numbers.

def fibonacci(num):
      if (num <= 1):
        return 1

      return fibonacci(num - 2) + fibonacci(num - 1)

# O(n!) - Factorial runtime, the algorithm runs in factorial time. 
# The factorial of a non-negative integer (n!) is the product of all positive integers less than or equal to n. This is a pretty terrible runtime. 
# Any algorithm that performs permutation on a given data set is an example of O(n!)


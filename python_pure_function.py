# We create a list 
my_list = [1,2,3]

# We create a pure function which will copy the original list and append an item to it 

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

# Test the function by using it

new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)
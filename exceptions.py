# IndexError
try:
    item = items[6]
    print(item)
except: 
    print("The index does not exist in the list.")

# ZeroDivisionError

def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)
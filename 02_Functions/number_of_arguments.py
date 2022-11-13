def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number #line 4 and 5 identical
        # or use this total *= number 
    return total

print(multiply(1,2,3,4))

# () creates tupples = similar to lists and they are a collection of objects/elements and they CAN'T be modified. Can't add or change (unmutable)
# [] creates lists

# Example 2
def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total 
        
print(multiply(1,2,3,4))

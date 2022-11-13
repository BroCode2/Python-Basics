def increment(num, by):
    return num + by 


print(increment(5, by=2)) #by is a keyword argument and it makes your code more readable

#optional parameters, all the optional parameter should come after the required parameters.
def increment(num, by=2): # set the parameter to a specific value, in this case it is set to 1
    return num + by 


print(increment(5))
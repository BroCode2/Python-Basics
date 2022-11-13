# it refers to the region of the code where a variable is defined
# local variables vs global variables-- local ones has a short lifetime. 
# ex: 1


#GLOBAL VARIABLE 
message = "Hello"

def greet(name):
    global message # not a good practice to use GLOBAL inside a function as it may create a bug for other functions that rely on the original global variable. 
    message = "b"

greet("Kemal")
print(message)

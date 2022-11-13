# There are two type of fucntions 
# 1 Perform a task 
# 2 Return a value
# format print(f"{name}")_formatted_striung

# 1 Perform a task
def greet(name):
    print(f"{name}") # usable but limited

# 2 Return a value, gives you more options 
round(1.9)

#how to turn Perform a task TYPE into Return a value 

def get_greeting(name):
    return f"Hi {name}" # note there are no brackets ()


message = get_greeting("Kemal") #because this is a VALUE, assign it to a variable
print(message) 

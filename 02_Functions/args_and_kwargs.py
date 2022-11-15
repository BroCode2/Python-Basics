# positional and keyword arguments: *args and **kwargs
# args = positional argument: basically collects all the positional arguments into the variable. 
# kwargs = keyword argument:

def student_info(*args, **kwargs):
    print (args)
    print (kwargs)
  

student_info("Math", "Art", "Science", "ELA", name="Kemal", age=40)
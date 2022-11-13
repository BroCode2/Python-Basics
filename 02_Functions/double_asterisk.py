def save_user(**user):
    print(user["name"])

save_user(id=1, name="john", age=40) 

# out put {'id': 1, 'name': 'john', 'age': 40} and this is called a DICTIONARY
# another data structure 
# when you use a double asterisk(**) python will automaticall will packege them into a dictionary using curly bracket notation
# after you write your arguments, you can access each argument by using square brackets in line # 2

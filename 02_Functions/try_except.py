try:
    hour = int(input("Enter hours here: "))
    rate = int(input("Enter rate here: "))
    pay = hour * rate 
    print (pay)
except:
    print("Enter a numeric number")
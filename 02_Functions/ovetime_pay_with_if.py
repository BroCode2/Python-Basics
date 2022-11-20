
try:
    hours = int(input("Hours worked: "))
    rate = 10

    if int(hours) <= 40:
        print("You have earned: ", hours * rate)

    elif int(hours) > 40:
        print("You have earned: ", (int(hours) - 40) * (int(rate) * 1.5) + int(rate) * 40)

except:
    print ("enter numeric values only")

# Ex 2

hours = int(input("Enter hours: "))
rate = 10
overtime = (hours - 40) * (rate * 1.5) + rate * 40
payment = hours * rate 

if hours > 40:
    print ("You have earned: ", overtime)
else:
    print(payment)
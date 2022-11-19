
try:
    hours = int(input("Hours worked: "))
    rate = 10

    if int(hours) <= 40:
        print("You have earned: ", hours * rate)

    elif int(hours) > 40:
        print("You have earned: ", (int(hours) - 40) * (int(rate) * 1.5) + int(rate) * 40)

except:
    print ("enter numeric values only")

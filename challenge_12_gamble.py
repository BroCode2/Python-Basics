"""Create a function that takes three arguments prob, prize, pay and returns True if prob * prize > pay; otherwise return False."""

def gamble(prob, prize, pay):
    if prob*prize > pay:
        return True
    else:
        return False
        
print(gamble(0.1,5,4))
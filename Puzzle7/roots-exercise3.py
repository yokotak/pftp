#Programming for the Puzzled -- Srini Devadas
#Hip To Be a Square Root
#Given a number, find the square root to within a given error
#Use bisection search.

##Find the square root to within a certain error using bisection search
def bisectionSearchForSquareRoot(x, epsilon):
    if x < 0:
        print ('Sorry, imaginary numbers are out of scope!')
        return
    
    numGuesses = 0
    #Small change to fix issue with numbers less than 1
    #need pos/neg selecthion -> start ans =
    low = min(-x, -1.0)
    high = max(x, 1.0)

    ans = (high + low)/2.0
    while abs(ans**3 + ans**2 - x) >= epsilon:
        a = abs(ans**2 * (ans + 1) - x)
        if ans**3 + ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
        numGuesses += 1
        #print('low = ', low, 'high = ', high, 'guess = ', ans)
    print ('numGuesses =', numGuesses)
    print (ans, 'is close to square root of', x)

    return

bisectionSearchForSquareRoot(11, .01)

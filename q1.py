def computeMinimumPayment( balance ):
    rate = .021                     # The rate of 2.1%
    if rate * balance > 10:        # The rate times the balance if greater then 10
        return rate * balance    # Mimimum payment is equal to 2.1% times the balance
    elif balance < 10:         # If the above didnt work
        return balance
    else:
        return 10# show what the mimimum is to pay off

#I was thinking wrong all the time. I was thinking we had to imput in a value and get a return on the-
#that value with all included. I was overthinking till i saw the video.
        

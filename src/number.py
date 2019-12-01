
def print_usage():
    print("In this game, you think of a number from 1 through n and I will try to guess what it is. After each guess, enter h if my guess is too high, l if too low, or c if correct.")

def get_guess(fmin,fmax):
    return int(fmin) + int((fmax-fmin)/2)

print_usage()

while True:
    limit = input("Please enter an integer: ")
    if not limit.isdigit():
        print("This is not an integer.  Try again...")
    else:
        break

again = True
while again:
    lmin = 0
    lmax = int(limit)
    num_guesses = 0
    while True:
        diff = lmax - lmin
        if diff == 0:
            guess = lmax
            print("Your number is {}. It took me {} guesses.".format(guess,num_guesses))
            break
        else:    
            guess = get_guess(lmin,lmax)
        num_guesses += 1
        answer = input("{}? ".format(guess))

        if answer == "h":
            lmax = guess - 1
            print("guess,max: {},{}".format(guess,lmax))
        elif answer == "l":
            lmin = guess + 1
            print("guess,min: {},{}".format(guess,lmin))
        elif answer == "c":
            print("Your number is {}.  It took me {} guesses.".format(guess,num_guesses))
            break
        elif answer == "q":
            break
        else:
            print("{} is an invalid response.  Try again...".format(answer))
    
    play = input("Do you want to play again? ")
    if play.upper() == 'Y':
        continue
    else:
        again = False

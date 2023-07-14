import random

def computer_guess(x):
    high = x
    low = 1
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is the {guess} High(H) or Low(L) or Correct(C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer guessed correctly {guess}")
    
computer_guess(100)
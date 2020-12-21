import random

def guess_a_number(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 - {x}: '))
        if guess>random_number:
            print("Sorry, guess again. To high.")
        elif guess<random_number:
            print("Sorry, guess again. To low.")
    print(f'Congratulations. You have guessed a number. This number is {random_number}.')

guess_a_number(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'Y':
        guess = random.randint(low, high)
        feedback = input(f'Computer: My number is {guess}, this number is low (L), high (H) or is good (Y)?: ').upper()
        if feedback == "L":
            low = guess + 1
        elif feedback == "H":
            high = guess - 1
    print(f"Yeah! I guees a number: {guess}")

computer_guess(1000)
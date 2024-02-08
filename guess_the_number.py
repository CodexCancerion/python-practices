import random

secret = random.randint(1, 10)
fount_it = False
count = 1
while count <= 3:
    guess = int(input(f'[{count}/3] Enter your guess: '))
    count += 1
    if guess == secret:
        print(f"You got it... in just {count-1} guesses")
        fount_it = True
        break
    else:
        if guess > secret:
            print('Your guess is greater')
            continue
        elif guess < secret:
            print('Your guess is lower')
            continue

if not fount_it:
    print("You didn't get it in 3 guesses")
    print(f'Secret is {secret}')
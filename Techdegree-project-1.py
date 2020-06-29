import random


def start_game():
    import sys
    # to invoke sys.exit when player does not want to play another game
    print('Welcome to the Number Guessing Game! \nCan you guess the number I have in mind?')
    scores = []
    while True:
        answer = random.randint(1, 100)
        # generate random answer for each game, limit possible range to integer 1-100 for playability
        attempt_count = 1
        while True:
            try:
                guess = int(input('Pick a number between 1 and 100! \nYour guess: '))
                while guess != answer:
                    if guess > answer:
                        attempt_count += 1
                        print("It's lower")
                        guess = int(input('Try again! \nYour guess: '))
                    elif guess < answer:
                        attempt_count += 1
                        print("It's higher")
                        guess = int(input('Try again! \nYour guess: '))
                print('Got it!This game is over! Your attempt number is {}'.format(attempt_count))
                scores.append(attempt_count)
                break
            except ValueError:
                print('Invalid Guess! Must be an integer! Try again!')
                continue
                # catch ValueError on guess input, allow to correct by asking again without incrementing attempt_count
        best_score = min(scores)
        # create variable for best score, define it as the lowest number of attempts to win the game
        while True:
            confirmation = str.upper(input('Would you like to play again? Y/N: '))
            if confirmation == 'Y':
                print('Best Score is {}'.format(best_score))
                break
            elif confirmation == 'N':
                sys.exit('Bye then!')
            else:
                print('Don\'t recognize your input!')
                continue
                # catch input other than Y/N and allow user to correct by asking again


start_game()

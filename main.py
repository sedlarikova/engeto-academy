import random
import time

def generate_digits(digits: int) -> list:
    # TODO: max 9 digits (low priority)
    """
    Random generator. Returns list of required length containing digits w/o repetition.
    Prints out an info message
    :param digits: number digits generated
    :return: list of digits w/o repetition
    """
    numbers_list = list(range(10))
    digits_list = []

    for i in range(digits):
        pop_number = random.randint(0, len(numbers_list)-1)

        # first letter cannot be zero (according to game rules)
        while pop_number == 0 and i == 0:
            pop_number = random.randint(0, len(numbers_list)-1)

        digits_list.append(numbers_list.pop(pop_number))

    print(f'I\'ve generated a random 4 digit number for you.')
    return digits_list


def get_guess(digits: int) -> list:
    """
    get input from user and validates it
    :param digits:
    :return: list of 4 string digits w/o repetition
    """
    incorrect_input = True

    while incorrect_input:
        guess = input('>>>')

        # check repetition
        repetition = False
        for i in range(len(guess)):
            repetition = True if guess.count(guess[i]) != 1 else repetition

        if len(guess) == digits and guess.isdigit() and not repetition:  # needs 4 digits
            incorrect_input = False
        else:
            print('Wrong input! (insert 4 numbers w/o repetition)')

    return list(guess)


def guess_eval(number: list, guess: list, round_number: int) -> bool:
    """
    guess evaluation. Prints out status. returns True/False statement
    :param number: random number to be guessed, list of integers
    :param guess: player's guess, list of strings
    :param round_number: game round
    :return: True/False statement whether there is a exact match.
    """
    bulls, cows = 0, 0
    wrong_guess = True

    # bulls and cows count
    for i in range(len(number)):
        if int(guess[i]) == number[i]:
            bulls += 1
        elif int(guess[i]) in number:
            cows += 1

    # game status eval
    wrong_guess = False if bulls == 4 else wrong_guess

    # print message
    print_message(wrong_guess, bulls, cows, round_number)

    return wrong_guess  # return false = winning; true = game continues


def print_message(wrong_guess: bool, bulls: int, cows: int, round_number: int):
    """
    decides what status print function to call (and calls it)
    :param wrong_guess: game status
    :param bulls: number of guessed bulls
    :param cows: number of guessed cows
    :param round_number: round of the game
    :return: None
    """
    if wrong_guess:
        print_status(bulls, cows)
    else:
        print_win(round_number)


def print_status(bulls: int, cows: int):
    """
    prints out status message
    :param bulls: number of guessed bulls
    :param cows: number of guessed cows
    :return: None
    """
    bulls_string = "bull"
    bulls_string = 'bulls' if bulls != 1 else bulls_string
    cows_string = "cow"
    cows_string = 'cows' if cows != 1 else cows_string
    print(f'{bulls} {bulls_string}, {cows} {cows_string}')


def print_win(round_number: int):
    """
    prints out winning message
    :param round_number: round of the game
    :return: None
    """
    guess_string = "guess"
    guess_string = 'guesses' if round_number != 1 else guess_string
    print(f'Correct, you\'ve guessed the number in {round_number} {guess_string}!')


def game_evaluation_create_dict() -> dict:
    """
    :return: dictionary of verbal score evaluation
    """
    eval_list = ['just a happy coincidence', 'amazing', 'average', 'not so good']
    eval_dict = {}
    eval_dict[1] = eval_list[0]
    for i in range(2, 25):
        if i <= 5:
            index = 1
        elif i < 15:
            index = 2
        else:
            index = 3
        eval_dict[i] = eval_list[index]

    return eval_dict


def calc_time(start_time) -> str:
    end_time = time.time()
    seconds = end_time - start_time
    time_list = []
    if seconds >= 3600:
        hours = round(seconds // 3600)
        time_list.append(str(hours) + ' hr')
        seconds -= hours * 3600
    if seconds >= 60:
        minutes = round(seconds // 60)
        time_list.append(str(minutes) + ' min')
        seconds -= minutes * 60
    if round(seconds) >= 1:
        time_list.append(str(round(seconds)) + ' sec')

    return ' '.join(time_list)

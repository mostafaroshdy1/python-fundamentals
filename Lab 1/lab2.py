import random

# # Q1
# def reduce_adjacent_duplicates(input_list):
#     resultSet = set(input_list)
#     return list(resultSet)

# input_list = [1, 2, 2, 3, 3, 4, 2, 4, 5]
# print(reduce_adjacent_duplicates(input_list))


# # Q2
# def divide_string(s):
#     length = len(s)
#     if length % 2 == 0:
#         front_half = s[: length // 2]
#         back_half = s[length // 2 :]
#     else:
#         front_half = s[: length // 2 + 1]
#         back_half = s[length // 2 + 1 :]
#     return front_half, back_half

# def combine_strings(a, b):
#     a_front, a_back = divide_string(a)
#     b_front, b_back = divide_string(b)
#     return a_front + b_front + a_back + b_back

# a = "abcde"
# b = "12345"
# print(combine_strings(a, b))


# Q3
# def isUnique(list):
#     return len(list) == len(set(list))

# print(isUnique([2, 4, 5, 5, 7, 9]))
# print(isUnique([1, 5, 7, 9]))

# Q4
# def bubbleSort(list):
#     for i in range(len(list)):
#         for j in range(len(list) - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#     return list

# print(bubbleSort([99, 100, 50, 10, 5, 3, 8, 2, 6, 4, 7, 9, 1]))


def guess_game():
    """Implements a number guessing game with 10 tries."""
    random_number = random.randint(1, 100)
    tries = 10
    guessed_numbers = set()

    while tries > 0:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_guess < 1 or user_guess > 100:
            print("Number out of range. Please try again.")
            continue

        if user_guess in guessed_numbers:
            print("You already guessed that number. Try again.")
            continue

        guessed_numbers.add(user_guess)
        tries -= 1

        if user_guess == random_number:
            print("Congratulations! You guessed the number in", 10 - tries, "tries!")
            if input("Play again? (y/n): ").lower() == "y":
                guess_game()  # Start a new game
            else:
                print("Thanks for playing!")
                break  # Exit the game
        elif user_guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    if tries == 0:
        print("You ran out of tries. The number was", random_number)
        if input("Play again? (y/n): ").lower() == "y":
            guess_game()  # Start a new game
        else:
            print("Thanks for playing!")


guess_game()

import random
from hangman_art import stages, logo
from hangman_words import word_list

random_index = random.randint(0, len(word_list))
random_word = word_list[random_index]
random_list = list(random_word)
result_list = ["_"]*len(random_list)
print(logo)
print(str(result_list))


position = 0
number_correct = 0
got_it = False
lives = 6

while number_correct < len(random_list) and lives > 0:
    user_input = input("Please input a letter: ")
    for letter in random_list:
        if letter == user_input:
            result_list[position] = user_input
            number_correct = number_correct + 1
            got_it = True
        position = position + 1
    if number_correct == len(random_list):
        break
    if got_it == False:
        lives = lives - 1
    else:
        got_it = False

    print(str(result_list))
    print(stages[lives])
    position = 0

if lives == 0:
    print(f"You lose. The word you guessed is {random_word}.")
else:
    print("You win.")




import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
placeholder = list(placeholder)
number_of_lives = 6

# TODO-1: - Use a while loop to let the user guess again.
print(f"you have {number_of_lives} lives")
while "_" in placeholder:
    while number_of_lives > 0 and "_" in placeholder:
        placeholder = list(placeholder)
        guess = input("Guess a letter: ").lower()
        if guess in chosen_word:
            print("Correct")
            print(f"You have {number_of_lives} lives left")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    placeholder[i] = guess
            display = "".join(placeholder)  # joins placeholder and turns into a string
            print(display)
        else:
            print("Wrong")
            number_of_lives -= 1
            print(f"you have {number_of_lives} lives left")
            if number_of_lives == 0:
                print("You lose")
if "_" not in placeholder:
    print("Well done, you won!")

# chosen_word = list(chosen_word)


# display = ""

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"



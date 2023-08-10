import random


# INTRO: ----------------------------------------------------->
def rules():
    return ("You can choose a category or I will do it for you\n"
            "I will think of a word. Will show you how long it is.\n"
            "You will have to give me a letter.\n"
            "You will have the right of 10 wrong guesses.\n"
            "If you blow all of them I will hang you!\n"
            "If you guess a letter I will uncover it in the word. if you uncover all - You Are A Free Man!"
            "\n"
            "- Small caps or capital letter does not matter.\n"
            "\n"
            "- If you give a letter more than once I will not count it as a mistake\n")


def lore():
    return f"The story is simple:\n" \
           "The other dayyou did something...\n" \
           "I don't know what it was. I am not here to judge.\n" \
           "You went to trail and I am your judge.\n" \
           "You are way too cute to let you be hanged for your crimes - big or small.\n" \
           "So I am giving you a chance to save yourself with a child's game of...\n" \
           "*** H A N G M A N ***\n" \
           "\n"


print("Welcome to HANGMAN, by Val!\n"
      "Do you need me to tell you the Rules, or may be some Lore before we start?\n"
      "\n"
      "R for rules\n"
      "L for story time\n"
      "C key to continue\n"
      "-> ")

# print(f"-> Your choice is {input()} <-")
help_ask = input().upper()
continue_playing = True
while continue_playing:
    if help_ask == "R":
        print(rules())
        print(f"Should we continue?\n"
              f"C to continue\n"
              f"L for Lore")
        help_ask = input()
        if help_ask == "C":
            continue_playing = False
            continue
    elif help_ask == "L":
        print(lore())
        print(f"Should we continue?\n"
              f"C to continue\n"
              f"R for Rules")
        help_ask = input()
        if help_ask == "C":
            continue_playing = False
            continue
    else:
        continue_playing = False
# START: ------------------------------------------------------>
print("Choose category you want your word to be from. \n"
      "Write down the letter of the proper choice:")
category_input = input(
    "- V - Veggies \n"
    "- F - Fruits \n"
    "- W - WoW \n"
    "- L - League of Legends characters \n"
    "- R - By my choice \n"
    "-> ").upper()
categories = {
    "V": ("BROCCOLI", "CABBAGE", "CARROT", "TOMATO", "ZUCCHINI",
          "EGGPLANT", "PEPPER", "SPINACH"),

    "F": ("APPLE", "WATERMELON", "MANGO", "PEAR", "PINEAPPLE",
          "STRAWBERRY", "BANANA"),

    "W": ("RAZAGETH", "VULPERA", "LEEROY JENKINS", "GOLDSHIRE", "ARTHAS",
          "ELUNE", "DRACTHYR"),

    "L": ("VIEGO", "TWISTED FAITH", "MALPHITE", "FIDDLESTICKS", "THRESH",
          "YASUO", "KASSADIN", "KATARINA", "LEBLANC", "MAOKAI",
          "MORGANA", "GRAVES")
}

while category_input not in categories.keys() and category_input != "R":
    print(f"Sorry! You picked up * {category_input} * which is not still in our list.\n"
          "Try again from the one I offered, or just * R * and I will do it for you")
    category_input = input("Choose the category: \n"
                           "-> ")

if category_input == "R":
    random_category = random.choice(list(categories.values()))
    correct_word = random.choice(random_category)
else:
    correct_word = random.choice(categories[category_input])

print(f"Thank you!\n"
      f"Your word is:")
# print(f" === {correct_word} ===")
empty_word = " ".join(len(correct_word) * "_")  # _ _ _ _ _

empty_word_cleared = empty_word.split(" ")  # [_,_,_,_,_]
word = list(correct_word)  # Yasuo ['Y', 'A', 'S', 'U', 'O']
if " " in word:
    empty_word_cleared[word.index(" ")] = " "

print(" ".join(empty_word_cleared))

# HANGING: --------------------------------------------------------------------->
def draw_hangman(count):
    hangman = [
        """
    
    
    
    
    
    
            _____""",
        """
    
              |
              |
              |
              |
              |
            __|__""",
        """
        _______
              |
              |
              |
              |
              |
            __|__""",
        """
        _______
         |    |
              |
              |
              |
              |
            __|__""",
        """
        _______
         |    |
         0    |
              |
              |
              |
            __|__""",
        """
        _______
         |    |
         0    |
        /     |
              |
              |
            __|__""",
        """
        _______
         |    |
         0    |
        / \   |
              |
              |
            __|__""",
        """
        _______
         |    |
         0    |
        / \   |
         |    |
              |
            __|__""",
        """
        _______
         |    |
         0    |
        / \   |
         |    |
        /     |
            __|__""",
        """
        _______
         |    |
         0    |
        / \   |
         |    |
        / \   |
            __|__"""
    ]
    return hangman[count - 1]


guess = input("What is your first guess?\n-> ").upper()

count_wrong = 0
state = False


while not state:
    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                empty_word_cleared[word.index(guess)] = guess  # A - 1 inx
                word[word.index(guess)] = " "
        print(" ".join(empty_word_cleared))
    else:
        count_wrong += 1
        print(draw_hangman(count_wrong))
        print(" ".join(empty_word_cleared))

    if count_wrong >= 10:
        state = True
        print(f"You couldn't uncover the word {correct_word}. You will hang!")
    if "_" not in empty_word_cleared:
        state = True
        print(f"was the word!\n"
              f"YOU WIN!" )

    guess = input("What is your next guess?\n-> ").upper()

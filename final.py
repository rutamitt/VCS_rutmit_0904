import random
import hangman_picture

one_list = []
two_list = []
three_list = []
letter_list = []
random_word = []

hangmanpics = hangman_picture.hangmanpics
guess = str
y = ''
n = ''
h = ''

# Lygio pasirinkimas tarp 1-3
def game():
    del one_list[0:10000]
    del two_list[0:10000]
    del three_list[0:10000]
    del letter_list[0:10000]
    del random_word[0:10000]
    i = 0
    print ("Welcome to Hangerman! Before you start please enter your preferences:")
    print (
        "Level 1 - a word contains 4 or less letters, level 2 - between 5 and 8 letters & level 3 - more than 8 letters")

    index = True
    while index == True:
        try:
            level = int(raw_input("Enter your level:"))
            if level >= 4:
                print 'Level is not available. Please choose 1-3'
            else:
                index = False
        except ValueError:
            print 'Invalid input type, try again'


    if level == 1:
        use = one_list
    elif level == 2:
        use = two_list
    elif level == 3:
        use = three_list

    index = True
    while index == True:
        try:
            mistakes = int(raw_input("Enter maximum number (1-6) of possible mistakes: "))
            if level >= 7:
                print 'Number of mistakes is not available. Please choose 1-6'
            else:
                index = False
        except ValueError:
            print 'Invalid input type, try again'


    words_file = open("words.txt", "r")

    for word in words_file.readlines():
        word_length = word.__len__()
        if word_length <= 5:  # kodel cia reikia rasyti penkis o ne keturis, ty visur plius vienas -- nes enteris yra kaip zenklas
            one_list.append(word.strip())
        elif 6 <= word_length <= 9:
            two_list.append(word.strip())
        elif word_length >= 10:
            three_list.append(word.strip())  # faile words yra enteriai kurie atsivaziuoja kaip \n, strip juos nuima

    for word in random.choice(use):
        for letter in word:
            random_word.append(letter)
    hidden_string = list("-" * (random_word.__len__()))

    while mistakes > letter_list.__len__():
        guess = raw_input("Guess a letter: ")
        if guess in random_word:
            print (guess, "Correct!")
            u = 0
            for h in random_word:
                if h == guess:
                    hidden_string[u] = guess
                    print(hidden_string)
                u += 1
        else:
            letter_list.append(guess)
            print ("Incorrect :(")
            print(hangmanpics[7 - mistakes + i])
            i += 1


end = "y"

game()

while end == "y":
    print 'game is over, do you want to try again?'
    end = str(raw_input("Press 'y' for yes or 'n' for no: "))
    if end == "y":
        game()
    else:
        print 'bye!'

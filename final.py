# limitation 1: galima speti tik paraidziui, ty negalima ivesti viso pilno zodzio
# limitation 2: antra karta spejant ta pacia neteisinga raide, tai uzskaitoma kaip nauja klaida


import random
import hangman_picture


hangmanpics = hangman_picture.hangmanpics


def game():                      # sukuriama funkcija game(), kurioje bus aprasyta viso zaidimo eiga
    one_list = []                # apibreziami listai one, two & three, i kuriuos bus padeti 1,2 ir 3 levelio zodziai
    two_list = []
    three_list = []
    letter_list = []             # listas, i kuri pridedamos neteisingai spetos raides
    random_word = []             # listas, i kuri paraidziui ikeliamas atsitiktinis zodis
    i = 0
    print ("Welcome to Hangerman! Before you start please enter your preferences:")
    print (
        "Level 1 - a word contains 4 or less letters, level 2 - between 5 and 8 letters & level 3 - more than 8 letters")

    index = True                                                            # nurodome, kad indexo reiksme TRUE, jog ciklas pradetu suktis
    while index:                                                            # Ciklas praso ivesti leveli ir tada ji tikrina pagal if salyga,
        try:                                                                # Jei inputas nepatenka i rezius (0<x<4) arba yra ne integer,
            level = int(raw_input("Enter your level:"))                     # yra isprintinama atitinkama zinute ir ciklas pasileidzia is naujo
            if level >= 4 or level < 1:
                print 'Level is not available. Please choose 1-3'
            else:
                index = False
        except ValueError:
            print 'Invalid input type, try again'


    if level == 1:               # 'use' - kintamasis,kurio reiksmes priklauso nuo userio inputo,
        use = one_list           # pagal pasirinkta leveli 'use' priskiriamas vienas is triju zodziu listu, kurie
    elif level == 2:             # sioje stadijoje yra vis dar tusti
        use = two_list
    elif level == 3:
        use = three_list

    index = True
    while index:                                                                              # sio ciklo tikslas apibrezti maximalu galimu klaidu skaiciu
        try:                                                                                  # userio inputas yra tikrinamas kaip ir pries tai buvusiame cikle
            mistakes = int(raw_input("Enter maximum number (1-6) of possible mistakes: "))    # jei jis nepatenka i rezi arba yra neteisingo tipo,
            if mistakes >= 7 or mistakes < 1:                                                 # userio yra paprasoma ivesti is naujo
                print 'Number of mistakes is not available. Please choose 1-6'
            else:
                index = False
        except ValueError:
            print 'Invalid input type, try again'

    words_file = open("words.txt", "r")       # tam kad galetume operuoti textinio failo (kuriame yra visi galimi zaidimo zodziai) duomenimis
                                              # naudojama built-in funkcija, kuri leidzia perskaityti faila
    for word in words_file.readlines():       #Siame cikle zodziui is zodziu failo, yra paskaiciuojamas jo ilgis
        word_length = word.__len__()          # ir pagal tai jis priskiriamas prie vieno is triju zodziu listu
        if word_length <= 5:
            one_list.append(word.strip())
        elif 6 <= word_length <= 9:
            two_list.append(word.strip())
        elif word_length >= 10:
            three_list.append(word.strip())  # faile words yra enteriai kurie atsivaziuoja kaip \n, strip juos nuima

    for word in random.choice(use):                            # random choice parenka atsitiktini zodi is pasirinkto naudoti zodziu listo
        for letter in word:                                    # tada random_word listui priskiriamos visos random zodzio raides
            random_word.append(letter)
    hidden_string = list("-" * (random_word.__len__()))        # hidden_string apibrezia uzslept raidziu skaiciu, jas pakeisdamas i '-'
    print(hidden_string)

    while mistakes > letter_list.__len__():                    # cia aprasomas spejimo ciklas, kuris vyksta tol, kol neteisingai atspetu raidziu skaicius yra
        guess = raw_input("Guess a letter: ")                  # mazesnis uz pasirinkta galimu klaidu skaiciu
        if guess in random_word:
            print (guess, "Correct!")                          # jei spejimas yra teisingas, mes patikriname kiekviena raide (h) spejamo zodzio raidziu liste
            u = 0                                              # jei u-toji raide sutampa su spejimu, hidden_stringe ja pakeiciame musu spejimu (guess)
            for h in random_word:
                if h == guess:
                    hidden_string[u] = guess
                    print(hidden_string)
                u += 1
        else:                                                  # jei spejimas neteisingas, pridedame ji prie letter_list  ir ispaisome sekanti hangerman paveiksleli
            letter_list.append(guess)                          # kur parenkamas is bendro skaiciaus atemus pasrinkita galimu klaidu skaicius ir
            print ("Incorrect :(")                             # atsizvelgiant, kelinta karta neteisingai buvo speta
            print(hangmanpics[7 - mistakes + i])
            i += 1
            print(hidden_string)
            print("Remaining guesses: "), mistakes - i         # po kiekvieno neteisingo spejimo ispausdina, kiek liko spejimu



game()                                                         # inicijuojame zaidima, iskviesdami jo funkcija

end = "y"                                                      # salyga, reikalinta ciklui pradeti veikti

while end == "y":                                              # po game() prasideda ciklas, kurio tikslas yra arba paleisti zaidima is naujo
    print 'game is over, do you want to try again?'            # arba sustbadyti, tai padaroma userio inputo pagalba pasirenktant norima veiksma y/n
    end = str(raw_input("Press 'y' for yes or 'n' for no: "))
    if end == "y":
        game()
    else:
        print 'bye!'




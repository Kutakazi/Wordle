def prelaunch(): #Fully Working
    allowedwords = []
    with open('allowed_words.txt') as f:
        for line in f:
            allowedwords.append(line.strip())

    possiblewords = []
    with open('possible_words.txt') as f:
        for line in f:
            possiblewords.append(line.strip())
    return allowedwords, possiblewords

def start(): #Fully Working
    print('Wordle Bot 1.1 by Alan Lu')
    print("Have you started the game? ('Y/N')")
    gamestart = ''
    while gamestart == '':
        gamestart = input()
        if gamestart.lower() == 'y':
            print('How many times have you guessed?')
            number = int(input(''))
            return number
        elif gamestart.lower() == 'n':
            return 0
        else:
            print('Invalid input')
            print("Have you started the game? ('Y/N')")
            gamestart = ''

def userans(guess, num, prevguess): #Fully Working
    if num != -1:
        print('Enter the results. G for Green. Y for Yellow. X for Grey. e.g.(XXGYX)')
        enter = input()
        prevguess.append(enter.upper() + guess)
        num += 1
        return prevguess, num
    else:
        return prevguess, num

def remove(prevguess, num, possiblewords, allowedwords): #NEEDS FIX
    if prevguess[num - 1][:5] == 'GGGGG':
        print('Good Job')
        num = -1
    else:
        listx, listy, listxy, listxg, listyg = duplicate(prevguess)

def duplicate(prevguess): #NEEDS FIX
    dupe = {}
    for i in prevguess[-1][5:]:
        dupe[i] = dupe.get(i, 0) + 1
    dupes = {}
    for i in dupe:
        if dupe[i] > 1:
            for nu, a in enumerate(prevguess[-1][5:]):
                if a == i:
                    dupes[i] = dupes.get(i, '') + prevguess[-1][nu]

    removalx = []
    removaly = []
    removalg = []
    print(dupes.keys())
    for letternum, letter in enumerate(prevguess[num - 1][:5]):
        if letter in dupes.keys():
            print(keys)
        elif letter == 'X':  # X is stored as letter + number
            removalx.append(prevguess[num - 1][letternum + 5].lower() + str(letternum))
        elif letter == 'Y':  # Y is stored as letter + number
            removaly.append(prevguess[num - 1][letternum + 5].lower() + str(letternum))
        elif letter == 'G':  # G is stored as letter + number
            removalg.append(prevguess[num - 1][letternum + 5].lower() + str(letternum))


def stop(num): #Fully Working
    print("Do you want to continue? ('Y/N')")
    enter = ''
    while enter == '':
        enter = input()
        if enter.lower() == 'n':
            num = -1
            return num
        elif enter.lower() == 'y':
            return num
        else:
            print('Invalid input')
            print("Do you want to continue? ('Y/N')")
            enter = ''

def guessbot(num, possiblewords, allowedwords): #NEEDS TO WORK
    if num == 0:
        guess = 'SALET'
    elif len(possiblewords) == 1:
        guess = possiblewords[0].upper()
        num = -1
        print(f'The answer is {guess}.')
    else: #Guessing Logic [MOST IMPORTANT PART]
        frequencey = {}
        for words in possiblewords:
            for letter in words:
                frequencey[letter] = frequencey.get(letter, 0) + 1
        frequencey = {k: v for k, v in sorted(frequencey.items(), key=lambda item: item[1])}
        #Weightings for each letter (pain)
        #Weightings will work by giving the top 5 numbers more weight
        #e.g. Most frequent x2.5, 2nd most frequent, x2.
        final = ''
        total = 0
        for word in possiblewords:
            semi = 0
            for letters in word:
                for letter, number in frequencey.items():
                    if letter == letters:
                        semi = semi = number
            if semi > total:
                total = semi
                final = word
        guess = final.upper()
    if num != -1:
        print(f'Guess {num + 1} is {guess}.')
    return guess, num

def recording(num, prevguess, allowedwords, possiblewords):
    solid = num + 1
    num = 0
    for number in range(1, solid):
        print(f'Word you guessed for {number}')
        guess = input().upper()
        prevguess, num = userans(guess, num, prevguess)
        prevguess, num, possiblewords, allowedwords = remove(prevguess, num, possiblewords, allowedwords)
    return num, prevguess, allowedwords, possiblewords

allowedwords, possiblewords = prelaunch()
#num = start()
num = 1
prevguess = []
if num != 0:
    num, prevguess, allowedwords, possiblewords = recording(num, prevguess, allowedwords, possiblewords)
while num != -1:
    guess, num = guessbot(num, possiblewords, allowedwords)
    if num != -1:
        num = stop(num)
        prevguess, num = userans(guess, num, prevguess)
    if num != -1:
        prevguess, num, possiblewords, allowedwords = remove(prevguess, num, possiblewords, allowedwords)
        num = stop(num)
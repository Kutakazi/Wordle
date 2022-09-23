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
    print('Wordle Bot 1.0 by Alan Lu')
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

def remove(prevguess, num, possiblewords, allowedwords): #WORKING!!!
    if prevguess[num - 1][:5] == 'GGGGG':
        print('Good Job')
        num = -1
    else:
        removalx = []
        removaly = []
        removalg = []
        for letternum, letter in enumerate(prevguess[num - 1][:5]):
            if letter == 'X': #x is stored as letter + number
                removalx.append(prevguess[num - 1][letternum + 5].lower() + str(letternum))
            elif letter == 'Y': #Y is stored as letter + number
                removaly.append(prevguess[num - 1][letternum + 5].lower() + str(letternum))
            elif letter == 'G': #G is stored as letter + number
                removalg.append(prevguess[num - 1][letternum + 5].lower() + str(letternum))
        listx, listy, listxy, listxg, listyg= duplicate(removalx, removaly, removalg)
        if len(listx) > 0: #Remove X
            possiblewords = [i for i in possiblewords if all(e not in i for e in listx)]
        if len(listy) > 0:  # Remove words that do not contain Y
            possiblewords = [i for i in possiblewords if all(e in i for e in listy)]
        if len(removalg) > 0: #Remove G FULLY WORKING
            for string in removalg:
                letter, number = string
                count = 0
                while len(possiblewords) != count:
                    if letter == possiblewords[count][int(number)]:
                        count += 1
                    else:
                        possiblewords.remove(possiblewords[count])
        if len(removaly) > 0: #Y again to remove Y letters that are in the Y letter spot
            for string in removaly:
                letter, number = string
                count = 0
                while len(possiblewords) != count:
                    if letter == possiblewords[count][int(number)]:
                        possiblewords.remove(possiblewords[count])
                    else:
                        count += 1
        if len(listxg) >0: #XG, Remove X from other slots (Letter, G location)
            nlist = ['0', '1', '2', '3', '4']
            for string in listxg:
                letter, number = string
                nlist.remove(number)
                count = 0
                while len(possiblewords) != count:
                    for n in nlist:
                        bn = 0
                        if letter == possiblewords[count][int(n)]:
                            bn += 1
                    if bn == 0:
                        count += 1
                    else:
                        possiblewords.remove(possiblewords[count])
        if len(listyg) >0: #YG, Check if letter in slot that is not Y or G and it only has 2 letters (Letter, Y Location, G Location)
            nlist = ['0', '1', '2', '3', '4']
            for string in listyg:
                letter, numbery, numberg = string
                nlist.remove(numbery)
                nlist.remove(numberg)
                count = 0
                while len(possiblewords) != count:
                    if possiblewords[count].count(letter) != 2:
                        possiblewords.remove(possiblewords[count])
                    else:
                        for n in nlist:
                            bn = 0
                            if letter == possiblewords[count][int(n)]:
                                pass
                            else:
                                bn += 1
                        if bn == 2:
                            possiblewords.remove(possiblewords[count])
                        else:
                            count += 1
        if len(listxy) >0: #XY, Check if one letter in word and letter not on X or Y.
            nlist = ['0', '1', '2', '3', '4']
            for string in listxy:
                letter, numberx, numbery = string
                nlist.remove(numberx)
                nlist.remove(numbery)
                count = 0
                while len(possiblewords) != count:
                    for n in nlist:
                        bn = 0
                        if letter == possiblewords[count][int(n)]:
                            pass
                        else:
                            bn += 1
                    if bn >= 1:
                        count += 1
                    else:
                        possiblewords.remove(possiblewords[count])
        print('Possible answer/s are:')
        print(' '.join(possiblewords).upper())
    return prevguess, num, possiblewords, allowedwords

def duplicate(removalx, removaly, removalg): #WORKING!!!!!!!
    listx = []
    listxy = []
    listxg = []
    listy = []
    listyg = []
    if len(removalx) > 0:
        for string in removalx:
            letter, number = string
            count = 0
            if len(removaly) > 0:
                for string2 in removaly:
                    letter2, number2 = string2
                    if letter == letter2:
                        count += 1
                    else:
                        if len(removalg) > 0:
                            for string3 in removalg:
                                letter3, number3 = string3
                                if letter == letter3:
                                    count += 1
                                elif count == 0:
                                    listx.append(letter)
                        elif count == 0:
                            listx.append(letter)
            elif len(removalg) > 0:
                for string3 in removalg:
                    letter3, number3 = string3
                    if letter == letter3:
                        count += 1
                    elif count == 0:
                        listx.append(letter)
            elif count == 0:
                listx.append(letter)
    if len(removaly) > 0 and len(removalg) > 0:#y ( Y will doublecount because of YY but no effect to script (i hope))
        for string in removaly:
            letter, number = string
            if letter in removalg:
                pass
            else:
                listy.append(letter)
    elif len(removaly) > 0:
        for string in removaly:
            letter, number = string
            listy.append(letter)
    if len(removalx) > 0 and len(removalg) > 0:
        for string in removalx: #xg
            letter, number = string
            for string2 in removalg:
                letter2, number2 = string2
                if letter == letter2 and number != number2:
                    if letter + number2 in listxg:
                        pass
                    else:
                        listxg.append(letter + number2)
    if len(removaly) > 0 and len(removalg) > 0:
        for string in removaly: #yg
            letter, number = string
            for string2 in removalg:
                letter2, number2 = string2
                if letter == letter2 and number != number2:
                    if letter + number + number2 in listyg:
                        pass
                    else:
                        listyg.append(letter + number + number2)
    if len(removalx) > 0 and len(removaly) > 0:
        for string in removalx: #xy
            letter, number = string
            for string2 in removaly:
                letter2, number2 = string2
                if letter == letter2 and number != number2:
                    if letter + number + number2 in listxy:
                        pass
                    else:
                        listxy.append(letter + number + number2)
    return listx, listy, listxy, listxg, listyg

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

def guessbot(num, possiblewords, allowedwords):
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
num = start()
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
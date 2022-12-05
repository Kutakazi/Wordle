possiblewords = []
allowedwords = []
dict = {}
import removal

def main(possible, allowed):
    global possiblewords
    global allowedwords
    possiblewords = possible
    allowedwords = allowed
    possiblewords = possible
    allowedwords = allowed
    guess()

def guess():
    global possiblewords
    global allowedwords
    global dict
    dict = {}
    for possible in possiblewords: # section gets the best guess by going through each possible answer and allowed word
        for allowed in allowedwords:
            result = identify(possible, allowed)
            tempallowedwords, temppossiblewords = removal.main(list(allowed.upper()), result, allowedwords, possiblewords)
            dict[allowed] = dict.get(allowed, 0) + len(temppossiblewords)
    for word in dict.keys():
        dict[word] = dict[word] / len(possiblewords)
    sort = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])} # this section sorts for the best guess
    for guess, number in sort.items():
        break
    # print(sort) # for example to show why this section may be required
    topguess = [key for key, value in sort.items() if value == number]
    if len(topguess) > 1: # only called for when there is more than one word with the same number of average turns to reach answer
        filtered = [word for word in topguess if word in possiblewords]
        if len(filtered) != 0: # if there is a word that is in the possible answers
            final = list(filtered)
        else: # else should have been unneeded but specific python issue
            final = list(topguess)
    else: # else should have been unneeded but specific python issue
        final = topguess
    print(f'Best Guess/es Are:')
    print(f'{" ".join(final).upper()}')

def identify(possible, allowed):
    result = ['.','.','.','.','.']
    possible = [letter for letter in possible]
    allowed = [letter for letter in allowed]
    possible, allowed, result = identifyg(possible, allowed, result)
    result = identifyy(possible, allowed, result)
    result = list(''.join(result).replace('.', 'x'))
    return result

def identifyg(possible, allowed, result):
    for pos, letter in enumerate(possible):
        if letter == allowed[pos]:
            result[pos] = 'g'
            possible[pos] = '.'
            allowed[pos] = '.'
    return possible, allowed, result

def identifyy(possible, allowed, result):
    for letter in possible:
        if letter in allowed and letter != '.':
            num = ''.join(possible).count(letter)
            for pos, item in enumerate(allowed):
                if item == letter and num > 0:
                    allowed[pos] = '.'
                    result[pos] = 'y'
                    num += -1
    return result
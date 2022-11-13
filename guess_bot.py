possiblewords = []
allowedwords = []
dict = {}
import removal

def main(possible, allowed, turn):
    global possiblewords
    global allowedwords
    possiblewords = possible
    allowedwords = allowed
    if len(possiblewords) > 1:
        possiblewords = possible
        allowedwords = allowed
        guess()
    else:
        print('Error')
    return turn

def guess():
    global possiblewords
    global allowedwords
    global dict
    dict = {}
    for possible in possiblewords:
        for allowed in allowedwords:
            result = identify(possible, allowed, possiblewords)
            tempallowedwords, temppossiblewords = removal.main(list(allowed.upper()), result, allowedwords, possiblewords)
            dict[allowed] = dict.get(allowed, 0) + len(temppossiblewords)
    for word in dict.keys():
        dict[word] = dict[word] / len(possiblewords)
    sort = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
    print(f'Best Guess/es Are:')
    print(f'{" ".join(list(sort.keys())[0:5]).upper()}')

def identify(possible, allowed, possiblewords):
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
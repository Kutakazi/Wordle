possiblewords = []
allowedwords = []
dict = {}
# def main(possible, allowed):
#     global possiblewords
#     global allowedwords
#     possiblewords = possible
#     allowedwords = allowed
#     guess()

# def guess():
    # global possiblewords
    # global allowedwords
    # global dict
    # dict = {}
    # for possible in possiblewords:
    #     tempdict = {}
    #     for allowed in allowedwords:
    #         results = identify(possible,allowed,possiblewords)

def identify(possible, allowed, possiblewords):
    result = ['.','.','.','.','.']
    possible = [letter for letter in possible]
    allowed = [letter for letter in allowed]
    possible, allowed, result = identifyg(possible, allowed, result)
    possible, allowed, result = identifyx(possible, allowed, result)
    possible, allowed, result = identifyy(possible, allowed, result)

def identifyg(possible, allowed, result):
    for pos, letter in enumerate(possible):
        if letter == allowed[pos]:
            result[pos] = 'g'
            possible[pos] = '.'
            allowed[pos] = '.'
    return possible, allowed, result

def identifyx(possible, allowed, result):
    for letter in possible:
        if letter in allowed and letter != '.':
            print(letter)
x
identify('salet', 'treat', 'aaaaa')
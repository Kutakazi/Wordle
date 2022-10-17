from collections import defaultdict

def prelaunch():
    global allowedwords
    global possiblewords
    allowedwords = open('allowed_words.txt').read().strip().split('\n')
    possiblewords = open('possible_words.txt').read().strip().split('\n')

def query():
    global turn
    global guess
    global results
    turn += 1
    print(f'Word Guessed For Turn {turn}')
    guess = list(input().upper())
    print(f'Results For {"".join(guess)}')
    results = list(input().lower())

def reset():
    global guess
    global results
    global dictg
    global dicty
    global resultx
    global resulty
    global resultg
    guess = []
    results = []
    dictg = defaultdict()
    dicty = defaultdict()
    resultg = []
    resulty = []
    resultx = set({})

def seperate():
    global guess
    global results
    global dictg
    global dicty
    global resultx
    global resulty
    global resultg
    for num, result in enumerate(results):
        if result == 'g':
            dictg[num] = guess[num]
            resultg.append(guess[num])
        if result == 'y':
            dicty[num] = guess[num]
            resulty.append(guess[num])
        if result == 'x':
            resultx.add(guess[num])

def remove():
    global dictg
    global dicty
    global resultx
    global resulty
    global resultg
    positions = [0, 1, 2, 3, 4]
    for pos, g in dictg.items():
        positions.remove(pos)
        removeg(g, pos)
    for x in resultx:
        if x not in resulty and x not in resultg:
            removex(x)
        else:
            num = resulty.count(x) + resultg.count(x)
            removex(x, True, num)
    for pos in dicty.keys():
        positions.remove(pos)
    for pos, y in dicty.items():
        removey(y, pos, positions)

def removeg(g, pos):
    global possiblewords
    possiblewords = [word for word in possiblewords if g.lower() == word[pos]]

def removex(x, special=None, num=None):
    global possiblewords
    if special == True:
        possiblewords = [word for word in possiblewords if word.count(x.lower()) == num]
    else:
        possiblewords = [word for word in possiblewords if x.lower() not in word]
def removey(y, pos):
    global possiblewords
    possiblewords = [word for word in possiblewords if y.lower() != word[pos] and y.lower() in word]

def normal():
    reset()
    query()
    seperate()
    remove()

def hard():
    pass

def main():
    global turn
    prelaunch()
    while turn < 6:
        reset()
        normal()


allowedwords = []
possiblewords = []
turn = 0
guess = []
results = []
dictg = defaultdict()
dicty = defaultdict()
resultg = []
resulty = []
resultx = set({})
main()

# sortedy = sorted(resulty.keys())
#     for i in sortedy:
#         print(resulty[i])
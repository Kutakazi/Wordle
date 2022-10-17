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
    global sety
    guess = []
    results = []
    dictg = defaultdict()
    dicty = defaultdict()
    resultg = []
    resulty = []
    resultx = set({})
    sety = set({})

def seperate():
    global guess
    global results
    global dictg
    global dicty
    global resultx
    global resulty
    global resultg
    global sety
    for num, result in enumerate(results):
        if result == 'g':
            dictg[num] = guess[num]
            resultg.append(guess[num])
        if result == 'y':
            dicty[num] = guess[num]
            resulty.append(guess[num])
            sety.add(guess[num])
        if result == 'x':
            resultx.add(guess[num])

def remove():
    global dictg
    global dicty
    global resultx
    global resulty
    global resultg
    global sety
    positions = [0, 1, 2, 3, 4]
    for pos, g in dictg.items():
        positions.remove(pos)
        removeg(g, pos)
    for x in resultx:
        numx = resulty.count(x) + resultg.count(x)
        removex(x, numx)
    for y in sety:
        numy = resulty.count(y)
        tempoarypositions = positions
        for pos, value in dicty.items():
            if value == y:
                tempoarypositions.remove(pos)
        removey(y, tempoarypositions, numy)

def removeg(g, pos):
    global possiblewords
    possiblewords = [word for word in possiblewords if g.lower() == word[pos]]

def removex(x, num):
    global possiblewords
    possiblewords = [word for word in possiblewords if word.count(x.lower()) == num]

def removey(y, pos, num):
    global possiblewords
    for word in possiblewords:
        tempoary = []
        for position in pos:
            tempoary.append(word[position])
        print(tempoary)
        possiblewords = [word for word in possiblewords if word.count(y.lower()) == num] # WORK FROM HERE

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
sety = set({})
main()

# sortedy = sorted(resulty.keys())
#     for i in sortedy:
#         print(resulty[i])
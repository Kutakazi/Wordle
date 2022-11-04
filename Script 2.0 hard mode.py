from collections import defaultdict
import guess_bot

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

def remove(hard=False):
    global dictg
    global dicty
    global resultx
    global resulty
    global resultg
    global sety
    positions = [0, 1, 2, 3, 4]
    for pos, g in dictg.items():
        positions.remove(pos)
        removeg(g, pos, hard)
    for x in resultx:
        numx = resulty.count(x) + resultg.count(x)
        removex(x, numx, hard)
    for y in sety:
        numy = resulty.count(y)
        tempoarypositions = positions
        for pos, value in dicty.items():
            if value == y:
                tempoarypositions.remove(pos)
        removey(y, tempoarypositions, numy, pos, hard)

def removeg(g, pos, hard):
    global possiblewords
    possiblewords = [word for word in possiblewords if g.lower() == word[pos]]
    if hard == True:
        global allowedwords
        allowedwords = [word for word in allowedwords if g.lower() == word[pos]]

def removex(x, num, hard):
    global possiblewords
    possiblewords = [word for word in possiblewords if word.count(x.lower()) == num]
    if hard == True:
        global allowedwords
        allowedwords = [word for word in allowedwords if word.count(x.lower()) == num]

def removey(y, positions, num, pos, hard): # NEED REFINING / NOT EFFICIENT
    global possiblewords
    possiblewords = [word for word in possiblewords if y.lower() != word[pos]]
    tempwordlist = []
    for word in possiblewords:
        tempoary = []
        for position in positions:
            tempoary.append(word[position])
        if tempoary.count(y.lower()) >= num:
            tempwordlist.append(word)
    possiblewords = tempwordlist
    if hard == True:
        global allowedwords
        allowedwords = [word for word in allowedwords if y.lower() != word[pos]]
        tempwordlist = []
        for word in allowedwords:
            tempoary = []
            for position in positions:
                tempoary.append(word[position])
            if tempoary.count(y.lower()) >= num:
                tempwordlist.append(word)
        allowedwords = tempwordlist

def possibleanswers():
    global possiblewords
    global allowedwords
    print('Possible Answers Include:')
    print(' '.join(possiblewords).upper())

def hard():
    global possiblewords
    global allowedwords
    reset()
    query()
    seperate()
    remove(True)
    possibleanswers()
    guess_bot.main(possiblewords, allowedwords)

def normal():
    pass

def main():
    global turn
    prelaunch()
    while turn < 6:
        reset()
        hard()


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
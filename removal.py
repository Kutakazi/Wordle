dictg = {}
dicty = {}
resultg = []
resulty = []
resultx = set({})
sety = set({})
hard = False

def reset():
    global dictg
    global dicty
    global resultx
    global resulty
    global resultg
    global sety
    dictg = {}
    dicty = {}
    resultg = []
    resulty = []
    resultx = set({})
    sety = set({})

def main(g, r, a, p, h=False):
    global guess
    global results
    global allowedwords
    global possiblewords
    global hard
    hard = h
    allowedwords = a
    possiblewords = p
    guess = g
    results = r
    reset()
    seperate()
    remove(hard)
    return allowedwords, possiblewords

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
    for pos, value in dicty.items():
        tempoarypositions = list(positions)
        numy = resulty.count(value)
        tempoarypositions.remove(pos)
        removey(value, tempoarypositions, numy, pos, hard)

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

def removey(y, temppositions, num, pos, hard): # NEED REFINING / NOT EFFICIENT
    global possiblewords
    possiblewords = [word for word in possiblewords if y.lower() != word[pos]]
    tempwordlist = []
    for word in possiblewords:
        tempoary = []
        for position in temppositions:
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
            for position in temppositions:
                tempoary.append(word[position])
            if tempoary.count(y.lower()) >= num:
                tempwordlist.append(word)
        allowedwords = tempwordlist
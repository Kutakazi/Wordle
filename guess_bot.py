from collections import defaultdict
dict = defaultdict(list)
tempdict = dict
totalaverage = defaultdict(float)
guesses = {}
possible = []
allowed = []
temppossible = []
tempallowed = []

def main(possiblewords, allowedwords):
    global possible
    global allowed
    global dict
    global totalaverage
    possible = possiblewords
    allowed = allowedwords
    for allowedword in allowed:
        dict[allowedword] = dict.get(allowedword)
        totalaverage[allowedword] = totalaverage.get(allowedword)
    guessmain()

def guessmain():
    global possible
    for possibleword in possible:
        

def guess1(allowedword, possibleword):

def guess2():
    pass
def guess3():
    pass
def guess4():
    pass


def reset():
    global possible
    global allowed
    global dict
    global temppossible
    global tempallowed
    global tempdict
    temppossible = possible
    tempallowed = allowed
    tempdict = dict

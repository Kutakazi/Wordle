import guess_bot
import removal

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
    if results == ['G','G','G','G','G']:
        print('You Have Found The Answer!')
        turn = 100

def possibleanswers():
    global possiblewords
    global allowedwords
    global turn
    if len(possiblewords) <= 0:
        print('Answer Either Not In Word List Or Entered Options Are Wrong.')
        turn = 100
    elif len(possiblewords) == 1:
        print(f'The Answer Is {"".join(possiblewords).upper()}')
        turn = 100
    else:
        print('Possible Answers Include:')
        print(' '.join(possiblewords).upper())
    return turn

def hard():
    global possiblewords
    global allowedwords
    global turn
    query()
    allowedwords, possiblewords = removal.main(guess, results, allowedwords, possiblewords, True)
    if turn != 100:
        turn = possibleanswers()
    if turn != 100:
        turn = guess_bot.main(possiblewords, allowedwords, turn)

def normal():
    global possiblewords
    global allowedwords
    global turn
    query()
    allowedwords, possiblewords = removal.main(guess, results, allowedwords, possiblewords)
    if turn != 100:
        turn = possibleanswers()
    if turn != 100:
        turn = guess_bot.main(possiblewords, allowedwords, turn)

def main():
    global turn
    prelaunch()
    print('What Difficulty? (N, H)')
    diff = input().lower()
    while turn != 100:
        if diff == 'h':
            hard()
        else:
            normal()
    reset()

def reset():
    global turn
    print('Would You Like To Play Again? (Y/N)')
    ans = input().lower()
    if ans == 'y':
        turn = 0
        main()


allowedwords = []
possiblewords = []
turn = 0
guess = []
results = []
main()

# sortedy = sorted(resulty.keys())
#     for i in sortedy:
#         print(resulty[i])
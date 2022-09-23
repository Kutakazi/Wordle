def prelaunch():
    allowedwords = []
    with open('allowed_words.txt') as f:
        for line in f:
            allowedwords.append(line.strip())
def main():
    with open('wordList.txt') as f:
        words = f.readlines()
        words = list(map(lambda x:x[:-1], words))

    return words
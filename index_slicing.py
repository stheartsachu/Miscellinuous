def mixed_word(word):
    even_word = word[::2]
    odd_word = word[1::2]
    return'{0} {1}'.format(even_word, odd_word)

def main():
    for i in range(int(input())):
        print(mixed_word(input()))




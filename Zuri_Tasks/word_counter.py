def word_counter(word):
    count = 0
    for i in word:
        count += 1
    print(count)


if __name__ == '__main__':
    word_counter('Hello World')

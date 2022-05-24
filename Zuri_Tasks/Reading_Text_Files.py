# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

file = 'C:/Users/DELL/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt'


def read_file_content(filename):
    # [assignment] Add your code here
    list = []
    with open(filename, "r") as f:
        contents = f.read()
        return contents


def count_words():
    from collections import Counter

    # [assignment] Add your code here
    text = read_file_content(file)

    counter = Counter(text.split())

    for word, count in sorted(counter.items()):
        print(f'{word:<12}{count}')


if __name__ == '__main__':
    print(read_file_content(file))
    print()
    print(count_words())

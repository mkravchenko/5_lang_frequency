import os
import sys
import re


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def get_most_frequent_words(text):
    wordcount = {}
    text_without_punctuation = re.sub('[^\w]+', ' ', text.lower())
    list_of_words = [word for word in text_without_punctuation.split()]
    for word in list_of_words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


def print_most_frequent_words(map_of_words):
    number_of_words = 10
    sorted_names = list(reversed(sorted(map_of_words, key=lambda x: map_of_words[x])))[:number_of_words]
    print("\nThe most used words in the text are:\n")
    for name in sorted_names:
        print("'{}' - number of repetitions is: {}".format(name, map_of_words[name]))


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    data_text = load_data(path_to_file)
    most_frequent_words = get_most_frequent_words(data_text)
    print_most_frequent_words(most_frequent_words)

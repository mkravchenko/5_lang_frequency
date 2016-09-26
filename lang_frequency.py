import os
import string
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def get_most_frequent_words(text):
    map_of_words = {}
    map_most_frequent_words = {}

    list_of_words = [word.strip(string.punctuation).lower() for word in text.split()]
    list_of_words.sort()

    for word in list_of_words:
        if word and word not in map_of_words:
            num_of_words = list_of_words.count(word)
            map_of_words[word] = num_of_words
            list_of_words.remove(word)
        else:
            list_of_words.remove(word)
    if len(map_of_words) >= 10:
        sorted_names = list(reversed(sorted(map_of_words, key=lambda x: map_of_words[x])))[:10]
        for word in sorted_names:
            map_most_frequent_words[word] = map_of_words[word]
    else:
        sorted_names = list(reversed(sorted(map_of_words, key=lambda x: map_of_words[x])))
        for word in sorted_names:
            map_most_frequent_words[word] = map_of_words[word]

    return map_most_frequent_words


def print_most_frequent_words(map_of_words):
    sorted_names = list(reversed(sorted(map_of_words, key=lambda x: map_of_words[x])))
    for name in sorted_names:
        print("Word is: '{}', number of number of repetitions is: {}".format(name, map_of_words[name]))


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    data_text = load_data(path_to_file)
    most_frequent_words = get_most_frequent_words(data_text)
    print_most_frequent_words(most_frequent_words)

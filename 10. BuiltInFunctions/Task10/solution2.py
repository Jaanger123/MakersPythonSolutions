from functools import reduce

list_ = ['Paul', 'George', 'Ringo', 'John']

def get_longest_string(word1, word2):
    if len(word1) > len(word2):
        return word1
    return word2

result = reduce(get_longest_string, list_)

print(result)
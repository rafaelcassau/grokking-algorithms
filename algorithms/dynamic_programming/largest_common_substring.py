"""
How similar two strings are?

This method consist in evaluate the largest common substring

fi(sh) X fo(sh)
f(ish) X h(ish)
m(ouse) X h(ouse)
(o)range X lem(o)n
b(lue) X c(lue)s
"""


def fill_table(first_word, second_word):
    matrix = []
    for l in range(len(first_word) + 1):
        matrix.append([0 for c in range(len(second_word) + 1)])
    return matrix


def measure_similarity_between_two_words(first_word, second_word):
    matrix = fill_table(first_word, second_word)
    for line in range(1, len(matrix)):
        for column in range(1, len(matrix[line])):
            if first_word[line-1] == second_word[column-1]:
                matrix[line][column] = matrix[line-1][column-1] + 1
            else:
                matrix[line][column] = 0

    return max([item for sublist in matrix for item in sublist])


assert measure_similarity_between_two_words("fish", "fosh") == 2
assert measure_similarity_between_two_words("fish", "hish") == 3
assert measure_similarity_between_two_words("mouse", "house") == 4
assert measure_similarity_between_two_words("orange", "lemon") == 1
assert measure_similarity_between_two_words("blue", "clues") == 3 

"""
How similar two strings are?

fish X hish
"""


def fill_table(first_word, second_word):
    matrix = []
    for l in range(len(first_word) + 1):
        matrix.append([0 for c in range(len(second_word) + 1)])
    return matrix


def measure_similarity_between_two_strings(first_word, second_word):
    matrix = fill_table(first_word, second_word)
    for line in range(1, len(matrix)):
        for column in range(1, len(matrix[line])):
            if first_word[line-1] == second_word[column-1]:
                matrix[line][column] = matrix[line-1][column-1] + 1
            else:
                matrix[line][column] = 0
    
    largest = 0
    for line in matrix:
        for column in line:
            if column > largest:
                largest = column

    return largest


assert measure_similarity_between_two_strings("fish", "hish") == 3
assert measure_similarity_between_two_strings("fort", "fosh") == 2
assert measure_similarity_between_two_strings("mouse", "house") == 4
assert measure_similarity_between_two_strings("orange", "lemon") == 1

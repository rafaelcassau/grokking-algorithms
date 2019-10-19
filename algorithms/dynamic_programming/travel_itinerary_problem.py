"""
Imagine you are traveling to London to take some vacation,
you have two days to stay there, but you wish to go in a lot
of places, however isn't possible to visit all those places
and you need to organize a list of places to be visited.

These problem is the same bag problem, but instead of a bag
you have limited time and instead of radios and notebooks
there are a list of places you want to visit.
"""


places = [
    {"name": "default", "time_in_days": 0, "ranking": 0},
    {"name": "Abadia de Westminster", "time_in_days": 0.5, "ranking": 7},
    {"name": "Teatro de Globe", "time_in_days": 0.5, "ranking": 6},
    {"name": "Galeria Nacional", "time_in_days": 1, "ranking": 9},
    {"name": "Museu Britanico", "time_in_days": 2, "ranking": 9},
    {"name": "Catedral de Sao Paulo", "time_in_days": 0.5, "ranking":8},
]

times = (0, 0.5, 1, 1.5, 2)


def get_time_index_by_time_in_days(time_in_days, times):
    index = 0
    for time in times:
        if time == time_in_days:
            return index
        index += 1
    return None


def create_matrix(places, times):
    matrix = []
    for i in places:
        matrix.append([0 for i in range(len(times))])
    return matrix


def get_place_can_be_visited_in_time(place, time):
    for key, value in place.items():
        if key == "time_in_days" and value <= time:
            return (place["name"], place["time_in_days"], place["ranking"])
    return ("default", 0, 0)


def make_travel_itinerary(places, times):
    matrix = create_matrix(places, times)
    
    for line_place in range(1, len(places)):
        for column_time in range(1, len(times)):
            current_place, current_time_in_days, current_ranking = get_place_can_be_visited_in_time(places[line_place], times[column_time])

            previous_place_ranking = matrix[line_place - 1][column_time]

            remaining_time_in_days_index = get_time_index_by_time_in_days(current_time_in_days, times)
            remaining_time_index = column_time - remaining_time_in_days_index
            remaining_ranking_for_place = matrix[line_place - 1][remaining_time_index]

            matrix[line_place][column_time] = max(previous_place_ranking, (current_ranking + remaining_ranking_for_place))

    return matrix


matrix = make_travel_itinerary(places, times)

assert matrix[1][1] == 7
assert matrix[1][2] == 7
assert matrix[1][3] == 7
assert matrix[1][4] == 7

assert matrix[2][1] == 7
assert matrix[2][2] == 13
assert matrix[2][3] == 13
assert matrix[2][4] == 13

assert matrix[3][1] == 7
assert matrix[3][2] == 13
assert matrix[3][3] == 16
assert matrix[3][4] == 22

assert matrix[4][1] == 7
assert matrix[4][2] == 13
assert matrix[4][3] == 16
assert matrix[4][4] == 22

assert matrix[5][1] == 8
assert matrix[5][2] == 15
assert matrix[5][3] == 21
assert matrix[5][4] == 24

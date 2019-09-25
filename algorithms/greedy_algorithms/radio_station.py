"""
The problem of set coverage

Suppose that you are starting a new radio program and you want to reach
listeners in all fifty states of United States of America. It's necessary to decide
in which radio stations the program will be transmited to reach all the listeners.
Houver transmit in different radio stations is expensive and you are trying to minimize
the amount of stations to use, it's necessary to avoid to spend much money.

Each station include a region and there are a overlap.

How to find the less set of stations in which you will transmite and reach all the fifty states?
It's sounds easy, isn't?

But it's so hard! look a resolution choice below:

1 - List each possible subset of stations. It's called (set of parts), it's also known as (power set).
2 - Among them choice the set with the less amount of stations that includes all the fifty states.

The problem in this case is the expended time to calculate each possible subset of stations, it's too long.
Once the execution time is Big O(2^N), because there are 2^N subsets.

There is no algorithm that solves this problem faster enough! What you can do?


Approximation Algorithms (Greedy Algorithm)

Below we have a algorithm that give a good solution for this problem:

1 - Get the station that includes the highest amount of states that are not covered yet. There is no problem
    if the station includes some states that are already covered.

2 - Repeat that until all of states has been covered.

This is called approximation algorithm, when is necessary a big amount of time to calculate the exact solution,
a approximation algorithm is a good idea and it works fine!

The approximation algorithms are evaluated for:

1 - By your speed.
2 - By your capacity to reach a ideal solution.


Greedy algorithms are a good choice because they are easy to understanding and because they have a good
execution time. In this case the greedy algorithm has the execution time Big O(N^2), N is the number of
radio stations.
"""

states_to_include = set([
    "MT", "WA", "OR", "ID",
    "NV", "UT", "CA", "AZ"
])
stations = {
    "kone": set(["ID", "NV", "UT"]),
    "ktwo": set(["WA", "ID", "MT"]),
    "kthree": set(["OR", "NV", "CA"]),
    "kfour": set(["NV", "UT"]),
    "kfive": set(["CA", "AZ"]),
}


def calculate_all_inclusion_with_less_station(states_to_include, stations):
    final_stations = set()

    while states_to_include:
        better_station = None
        coverage_states = set()
        for station, states_by_station in stations.items():
            states_temp = states_to_include & states_by_station
            if len(states_temp) > len(coverage_states):
                better_station = station
                coverage_states = states_temp

        final_stations.add(better_station)
        states_to_include -= coverage_states
    
    return sorted(list(final_stations))


final_stations = calculate_all_inclusion_with_less_station(states_to_include, stations)
assert final_stations == ['kfive', 'kone', 'kthree', 'ktwo']

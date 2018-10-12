def reconstruct_trip(tickets):
  pass 

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass

def reconstruct_trip(flights):
    """
    Find departure and arrival airport from chain of flights.

    Effectively the opposite of the itertools recipe pairwise:

    >>> get_departure_arrival([(s0, s1), (s1, s2), (s2, s3)])
    (s0, s3)

    Pairs do not have to be in order:

    >>> get_departure_arrival([(s0, s1), (s2, s3), (s1, s2)])
    (s0, s3)
    """
    sources, destinations = map(set, zip(*flights))

    depart = (sources - destinations).pop()
    arriv = (destinations - sources).pop()

    #return depart, arriv
    flight_dict = dict(flights)
    while depart != arriv:
        yield depart
        depart = flight_dict[depart]
    return depart
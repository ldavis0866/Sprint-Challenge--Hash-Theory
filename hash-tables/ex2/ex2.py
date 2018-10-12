


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass

def reconstruct_trip(flights):
  dictionary = {}

  for flight in flights:
    dictionary[flight[0]] = flight[1]
  present_flight = dictionary[None]
  trip = []

  while present_flight != None:
    trip.append(present_flight)
    if present_flight in dictionary:
      present_flight = dictionary[present_flight]
    else:
      return []

  ##print(trip)
  return trip

    



short_set = [(None, 'PDX'),('PDX', 'DCA'),('DCA', None)]

long_set = [
      ('PIT', 'ORD'),
      ('XNA', 'CID'),
      ('SFO', 'BHM'),
      ('FLG', 'XNA'),
      (None, 'LAX'), 
      ('LAX', 'SFO'),
      ('CID', 'SLC'),
      ('ORD', None),
      ('SLC', 'PIT'),
      ('BHM', 'FLG'),
    ]

incorrect_set = [
      ('LHD', 'DAB'),
      (None, 'HVN'),
      ('MSO', 'SFO'),
      ('RDU', 'ABQ'),
      ('ACY', None),
    ]

#reconstruct_trip(short_set)
#['PDX', 'DCA']

#reconstruct_trip(long_set)
#['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD']

#reconstruct_trip(incorrect_set)
#[]
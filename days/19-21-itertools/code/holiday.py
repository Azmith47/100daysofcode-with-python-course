from itertools import cycle
from time import sleep

locations = "Australia Japan Singapore Italy Greece France".split()

trip = cycle(locations)

while True:
    print(next(trip))
    sleep(1)

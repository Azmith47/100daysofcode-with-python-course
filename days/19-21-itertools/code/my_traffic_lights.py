from itertools import cycle
from random import randint
from time import sleep


colours = "Red Green Amber".split()
traffic_light = cycle(colours)


def sleep_time():
    return randint(3, 8)


def traffic_rotation(traffic_light):
    for colours in traffic_light:
        if colours == "Green":
            print(f"The light is {colours}, Go! Go! Go!")
            sleep(sleep_time())

        elif colours == "Red":
            print(f"The light is {colours}, STOP!")
            sleep(sleep_time())

        else:
            print(
                f"The light is {colours}, Get ready to stop or speed up to get through"
            )
            sleep(3)


if __name__ == "__main__":
    traffic_rotation(traffic_light)

from typing import Dict, List

cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    jeeps = cars["Jeep"][::]
    car = ", ".join(jeeps)

    return car


def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    lst = []
    for keys, values in cars.items():
        lst.append(values[0])
    return lst


def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
    lst = []

    for keys, values in cars.items():
        cnt = 0

        while cnt != len(values):

            if grep.lower() in values[cnt].lower():
                lst.append(values[cnt])

            cnt += 1

    lst.sort()
    return lst


def sort_car_models(cars: CarsType = cars) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
    sortedcars = dict(cars)

    for keys, values in sortedcars.items():
        values.sort()

    sortedcars = list(sortedcars.items())
    sortedcars.sort()
    sortedcars = dict(sortedcars)

    return sortedcars


print(get_all_jeeps())

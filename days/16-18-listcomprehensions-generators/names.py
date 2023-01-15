NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names) -> list:
    """Should return a list of title cased names,
    each name appears only once"""
    lst = [name.title() for name in names]
    lst = list(dict.fromkeys(lst))
    return lst


def get_surname(name) -> str:
    return name.split()[1]


def sort_by_surname_desc(names) -> list:
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(reverse=True, key=get_surname)
    return names


def shortest_first_name(names) -> str:
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    names = [name.split()[0] for name in names]
    shortest = min(names, key=len)
    return shortest

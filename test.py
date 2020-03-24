import random

number = random.randint(1, 8)


def switch_demo(value):
    switcher = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }
    print("Hello planet " + switcher.get(value))


switch_demo(number)

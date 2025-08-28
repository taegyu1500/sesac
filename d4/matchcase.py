from enum import Enum, auto

color = input("Enter color: ")

class Colors(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()

match Colors[color]:
    case Colors.RED:
        print("stop", Colors.RED.value)
    case Colors.YELLOW:
        print("caution", Colors.YELLOW.value)
    case Colors.GREEN:
        print("Go")
    case _:
        print("Invalid")

class Role(Enum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'


## @file Negate.py
import Vector


# Negates input
def execute(input):
    if type(input) == tuple:
        return Vector.componentTo(-input[0], -input[1])
    else:
        return -input
"""
Find the depth of a fall using the time measured between the release of an object and the sound of impact.

Parameters:
mt: measured time in seconds
iterations: maximum number of iterations that the code should execute
precision: number of decimal places in the result

Constants:
v: speed of sound (330.0 m/s)
g: gravitational acceleration (9.8 m/s²)

Returns:
Tuple with the rounded depth and difference between the calculated and measured time
"""

from math import sqrt

def depth(mt: float, iterations: int = 1000, precision: int = 3):

    # Constants of nature
    v = 330.0 # Speed of sound
    g = 9.8 # Gravitational acceleration

    h = (g * mt**2) / 2 # Initially estimated height assuming the sound as instantaneous

    # Loop to find the root of the function f(h) = ct(h) - mt
    for i in range(iterations):

        ct = (h/v) + sqrt(2*h/g) # Calculated time given h
        dct = (1/v) + 1/sqrt(2*g*h) # Derivative dct/dh
        h = h - (ct - mt)/dct # New estimative of h using Newton-Raphson method

    return round(h, precision), round(abs(ct - mt), precision)

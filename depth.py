"""
Find the depth of a fall using the time measured between the release of an object and the sound of impact.

Parameters:
measured_time: measured time in seconds
iterations: maximum number of iterations that the code should execute
precision: number of decimal places in the result

Constants:
speed_of_sound: speed of sound (330.0 m/s)
g: gravitational acceleration (9.8 m/s²)

Returns:
Tuple with the rounded depth and difference between the calculated and measured time
"""

from math import sqrt

def depth(measured_time: float, iterations: int = 1000, precision: int = 3):

    # Constants
    speed_of_sound = 330.0
    g = 9.8

    height= (g * measured_time**2)/2 # Initially estimated height assuming the sound as instantaneous

    # Loop to find the root of the function f(height) = calculated_time(height) - measured_time
    for i in range(iterations):

        calculated_time = (height/speed_of_sound) + sqrt(2*height/g) # Calculated time given height
        dcalculated_time = (1/speed_of_sound) + 1/sqrt(2*g*height) # Derivative dcalculated_time/dheight
        height = height- (calculated_time - measured_time)/dcalculated_time # New estimative of height using Newton-Raphson method

    return round(height, precision), round(abs(calculated_time - measured_time), precision)

#Joe Melia EET-107

from adafruit_circuitplayground import cp
import random
import time

def main():
    pattern = [1, 4, 7, 0, 3, 6, 9, 2, 5, 8]
    while True:
        for pixel in pattern:
            cp.pixels[pixel] = pixel_color()
            time.sleep(0.25)
            cp.pixels[pixel] = (0, 0, 0)

def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return(red, green, blue)
                      
main()

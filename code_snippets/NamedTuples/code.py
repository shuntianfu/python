from collections import namedtuple

color = (55, 155, 255)

color = {'red': 55, 'green': 155, 'blue': 255}

zhang = namedtuple('Color', ['red', 'green', 'blue'])

white = zhang(red=55, green=155, blue=255)

yellow = zhang(red=10, green=234, blue=133)

print(zhang)
print(white)
print(yellow.blue)
print(white.blue)

print(type(zhang))
print(type(white))

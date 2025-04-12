gravity_constants = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Get user input
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Get planet's gravity multiplier
if planet in gravity_constants:
    planet_weight = round(earth_weight * gravity_constants[planet], 2)
    print(f"The equivalent weight on {planet}: {planet_weight}")
else:
    print("Sorry, that planet is not in the list.")
# http://www.python-course.eu/python3_generators.php
# What is really happening, when you use an iterable like a string, a list, or a tuple, inside of a for loop is the
# following: The function "iter" is called on the iterable. The return value of iter is an iterable. We can iterate over
# this iterable with the next function until the iterable is exhausted and returns a StopIteration exception:

cities = ["Paris", "Berlin", "Hamburg", "Frankfurt", "London", "Vienna", "Amsterdam", "Den Haag"]
for location in cities:
    print("location: " + location)


# A brute force iterator example

expertises = ["Novice", "Beginner", "Intermediate", "Proficient", "Experienced", "Advanced"]
expertise_iterator = iter(expertises)
next(expertise_iterator)
next(expertise_iterator)
next(expertise_iterator)
next(expertise_iterator)
next(expertise_iterator)
next(expertise_iterator)
next(expertise_iterator)
next(expertise_iterator)


# Refined iterator

other_cities = ["Strasbourg", "Freiburg", "Stuttgart", "Vienna / Wien", "Hannover", "Berlin", "Zurich"]
city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break


# Basic Generator

def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

city = city_generator()
print(next(city))


import random

class Random (random.Random):
    random = random.Random().random


    def random(Random, random = random ):
        return lambda random=random: random

## This line cane be made as long as desired by adding more calls with '(random=Random().random)' and then making more calls until it returns.
## Should terminate when a '(random=Random().random)' call is followed by two more calls, followed by one last call with no arguments.
## The output will be whatever is passed in the second-to-last call. Since here the library random function is called, the last call just calls that and returns the random number.

random = Random().random(random=Random().random)(random=Random().random)(random=random.random)(random=Random().random)(random=random.random)(random=random.random)()

print(f"random: {random}")



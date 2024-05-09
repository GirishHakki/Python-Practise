import random
def generate_random_number(start, end):
    return random.randint(start, end)

start = 1
end = 100
print("Random number between", start, "and", end, "is:", generate_random_number(start, end))
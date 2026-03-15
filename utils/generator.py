import random

def generate_array(size=30):
    return [random.randint(10, 100) for _ in range(size)]
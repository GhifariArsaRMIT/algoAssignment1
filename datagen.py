import random

# Generate a file with random numbers and their line numbers
with open('randomData.txt', 'w') as file:
    for i in range(0, 100):
        for j in range(0, 100):
            # Generate a random integer
            random_integer = round(random.uniform(1.0, 1000.0), 2)
            # Write the line number and random integer to the file
            file.write(f'{i} {j} {random_integer}\n')
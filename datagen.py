import random

# Generate a file with random numbers and their line numbers

def createFile(size: str):
    filename = "randomData"
    ranges = 0
    if size == "Small":
        ranges = 15
    elif size == "Medium":
        ranges = 40
    elif size == "Large":
        ranges = 100
        
    for i in range(2):
        filename += size
        filename += str(i + 1)
        filename += ".txt"
        with open(filename, 'w') as file:
            for j in range(0, ranges * 2 if i == 1 else ranges):
                for k in range(0, ranges * 2 if i == 1 else ranges):
                    # Generate a random integer
                    random_integer = round(random.uniform(1.0, 1000.0), 2)
                    # Write the line number and random integer to the file
                    file.write(f'{j} {k} {random_integer}\n')
        filename = "randomData"

createFile("Small")
createFile("Medium")
createFile("Large")
                
        
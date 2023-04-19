import random

# Generate a file with random numbers and their line numbers

def createFile(sizes: int, probability: float):
    if sizes > 100:
        print("size too big")
        return
    
    filename = "randomData"
    sizeName = ""
    if sizes < 31:
        sizeName = "Small"
    elif sizes < 100:
        sizeName = "Medium"
    elif sizes >= 100:
        sizeName = "Large"
        
    secondSize = (sizes // 2) + sizes

    for i in range(2):
        filename += sizeName
        filename += str(i + 1)
        filename += ".txt"
        with open(filename, 'w') as file:
            for j in range(0, secondSize if i == 1 else sizes):
                for k in range(0, secondSize if i == 1 else sizes):
                    # Generate a random integer
                    random_integer = round(random.uniform(1.0, 1000.0), 2)
                    # Write the line number and random integer to the file
                    
                    random_float = random.random()
                    if random_float <= probability:
                        file.write(f'{j} {k} {random_integer}\n')
        filename = "randomData"

createFile(15, 0.8)
createFile(40, 0.8)
createFile(100, 0.8)
                
        
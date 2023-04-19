import random

# Generate a file with random numbers and their row and col numbers
globalCount = 1

def createFile(sizes: int, probability: float, num):
    global globalCount
    if sizes > 200:
        print("size too big")
        return
    
    filename = "randomData"
    sizeName = ""
    
    if sizes < 31:
        sizeName = "Small"
        
    elif 31 < sizes <= 60:
        sizeName = "Medium"
        
    elif 60 < sizes < 91:
        sizeName = "MediumLarge"
        
    elif sizes >= 100:
        sizeName = "Large"
    

    filename += sizeName
    filename += str(num)
    filename += ".txt"
    with open(filename, 'w') as file:
        for j in range(0, sizes):
            for k in range(0, sizes):
                # Generate a random number
                random_number = round(random.uniform(1.0, 1000.0), 2)
                # Write the cell row and number and random integer to the file
                
                random_float = random.random()
                if random_float <= probability:
                    file.write(f'{j} {k} {random_number}\n')
    globalCount += 1

createFile(15, 0.8, 1)
createFile(22, 0.8, 2)
createFile(40, 0.8, 1)
createFile(60, 0.8, 2)
createFile(78, 0.8, 1)
createFile(90, 0.8, 2)
createFile(120, 0.8, 1)
createFile(150, 0.8, 2)
                
        
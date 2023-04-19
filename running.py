import subprocess

# Define the command to run
implementation = "array"
cmd = "python3 spreadsheetFilebased.py " + implementation + " randomDataSmall1.txt  sampleCommands.in sample.out"

print("Small1:")
for i in range(3):
    subprocess.run(cmd, shell=True)

cmd = "python3 spreadsheetFilebased.py " + implementation + " randomDataSmall2.txt  sampleCommands.in sample.out"

print("Small2:")
for i in range(3):
    subprocess.run(cmd, shell=True)

cmd = "python3 spreadsheetFilebased.py " + implementation + " randomDataMedium1.txt  sampleCommands.in sample.out"

print("Medium1:")
for i in range(3):
    subprocess.run(cmd, shell=True)
    
cmd = "python3 spreadsheetFilebased.py " + implementation + " randomDataMedium2.txt  sampleCommands.in sample.out"

print("Medium2:")
for i in range(3):
    subprocess.run(cmd, shell=True)
    
cmd = "python3 spreadsheetFilebased.py " + implementation + " randomDataMediumLarge1.txt  sampleCommands.in sample.out"

print("MediumLarge1:")
for i in range(3):
    subprocess.run(cmd, shell=True)
    
cmd = "python3 spreadsheetFilebased.py " + implementation + " randomDataMediumLarge2.txt  sampleCommands.in sample.out"

print("MediumLarge2:")
for i in range(3):
    subprocess.run(cmd, shell=True)

cmd = "python3 spreadsheetFilebased.py " + implementation + " randomDataLarge1.txt  sampleCommands.in sample.out"


print("Large1:")
for i in range(3):
    subprocess.run(cmd, shell=True)

cmd = "python3 spreadsheetFilebased.py " + implementation + " randomDataLarge2.txt  sampleCommands.in sample.out"

print("Large2:")
for i in range(3):
    subprocess.run(cmd, shell=True)
    
# Run the comman
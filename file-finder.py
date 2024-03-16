import os

if os.path.exists('test.txt'):
    print("Found the test.txt")
else:
    print("Couldn't find test.txt")
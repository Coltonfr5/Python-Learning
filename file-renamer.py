import os


if os.path.exists('testfile.txt'):
    os.rename('testfile.txt', 'testingworked.txt')
else:
    if os.path.exists('testingworked.txt'):
        os.rename('testingworked.txt', 'testfile.txt')
    else:
        print("I give up finding it")
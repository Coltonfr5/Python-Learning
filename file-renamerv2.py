import os


if os.path.exists('testfile.txt'):
    os.rename('testfile.txt', 'testingworked.txt')
    file = open('changes.txt', 'a')
    file.write('\n Changed "testfile.exe" to "testingworked.txt"')
    file.close()
else:
    if os.path.exists('testingworked.txt'):
        os.rename('testingworked.txt', 'testfile.txt')
        file = open('changes.txt', 'a')
        file.write('\n Changed "testingworked.txt" to "testfile.exe"')
        file.close()
    else:
        print("I give up finding it")
        file = open('changes.txt', 'a')
        file.write('\n Could not find the file(s) testfile.txt and/or testingworked.txt')
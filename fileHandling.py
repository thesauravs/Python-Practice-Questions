import os

lines = []
#ap = open('sample.txt', 'w')

#ap.write('Hi, this is a special file to check the python code. The special symbols are ~ ! @ # $ % ^ & * ( ) _ - = + , . / < > ? ; ’ : ” [ ] \ { } |.\nThis starts and ends a new line.\nThe numbers are 0 1 2 3 4 5 6 7 8 9\nthis line is all in small letters.\nTHIS LINE IS ALL IN CAPITAL LETTERS.')
#ap.close()

f = open('sample.txt', 'rt')
print(f.read())
#print(f.read())
#print(f.read(10))
#print(f.readline())
#print(f.readline())
#print(f.readlines())
f.close()
print(os.name)
os.remove('test.txt')
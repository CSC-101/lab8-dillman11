import sys
from ast import Index

try:
    text_file = open(sys.argv[1],"r")
    for line in text_file:
        sum = 0
        floats = line.split()
        try:
            for num in floats:
                sum += float(num)
            print("sum =", sum)
        except ValueError as e:
            print("Error -", e)
    text_file.close()
except IOError as e:
    print("Error -", e)
    exit()
except IndexError as e:
    print("Error -", e)
    exit()


#!/usr/bin/env python

import sys

def main(argv):
    if(len(argv)!=2):
        print("Incorrect number of arguments given, 1 expected,", len(argv), "given.")
        print("Usage: python day1.py [filename] [numElves]")
        sys.exit()

    try:
        file = open(argv[0],'r')
    except Exception:
        print("Could not open/read file:",argv[0])
        sys.exit()
    
    numElves = int(argv[1])
    maxCal = []
    for i in range(0,numElves):
        maxCal.append(0)
    currCal = 0

    for lineNum, line in enumerate(file):
        line = line.strip()
        if not line:
            if currCal > maxCal[0]:
                maxCal[0] = currCal
                maxCal.sort()
            currCal = 0
        else:
            try:
                currCal += int(line)
            except ValueError:
                print("Invalid characters in file. Line #",lineNum)
                sys.exit()

    if currCal > maxCal[0]:
        maxCal[0] = currCal

    sum = 0
    for i in maxCal:
        sum += i

    print("Calories carried by top", numElves ,"elves:", maxCal)
    print("Sum of Calories carried by top", numElves ,"elves:", sum)

    file.close()

if __name__ == '__main__':
    main(sys.argv[1:])
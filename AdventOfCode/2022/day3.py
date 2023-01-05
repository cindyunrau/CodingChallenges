#!/usr/bin/env python

import sys

def getValue(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38

def main(argv):
    if(len(argv)!=1):
        print("Incorrect number of arguments given, 1 expected,", len(argv), "given.")
        print("Usage: python day3.py [filename]")
        sys.exit()

    try:
        file = open(argv[0],'r')
    except Exception:
        print("Could not open/read file:",argv[0])
        sys.exit()

    sumPriority = 0
    fileList = file.readlines()

    ### PART 1
    for lineNum, line in enumerate(fileList):
        line = line.strip()
        numItems = len(line) 
        common = ""

        if numItems % 2 != 0:
            print("Odd number of characters in file. Line #", lineNum +1)
            sys.exit()

        comp1 = line[0:int(numItems/2)]
        comp2 = line[int(numItems/2):numItems]
        for x in comp1:
            if x in comp2 and x not in common:
                common += x
                sumPriority += getValue(x)
    
    print("PART 1:")
    print("   Sum of priorities of items common to both parts of each backpack:", sumPriority)

    ### PART 2
    sumPriority = 0
    numGroups = len(fileList)/3
    if not numGroups.is_integer():
        print("Number of lines in file must be divisible by 3. Number of Lines:", len(fileList))
        sys.exit()

    for i in range(int(numGroups)):
        for x in fileList[3*i]:
            if x in fileList[3*i+1] and x in fileList[3*i+2]:
                sumPriority += getValue(x)
                break
    
    print("PART 2:")
    print("   Sum of priorities of items common to all 3 backpacks:", sumPriority)


    file.close()

if __name__ == '__main__':
    main(sys.argv[1:])
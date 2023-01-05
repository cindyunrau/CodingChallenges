#!/usr/bin/env python

import sys

def main(argv):
    if(len(argv)!=1):
        print("Incorrect number of arguments given, 1 expected,", len(argv), "given.")
        print("Usage: python day4.py [filename]")
        sys.exit()

    try:
        file = open(argv[0],'r')
    except Exception:
        print("Could not open/read file:",argv[0])
        sys.exit()

    
    sumFullOverlap = 0
    sumOverlap = 0

    for lineNum, line in enumerate(file):
        line = (re.sub("-", ",", line.strip())).split(",")
        sec = [ int(x) for x in line ]

        if (sec[1] - sec[0]) < (sec[3] - sec[2]):
            sec = [sec[2],sec[3],sec[0],sec[1]]

        if (sec[0] <= sec[2]) and (sec[1] >= sec[3]):
            sumFullOverlap += 1
        elif (sec[2] <= sec[0]) and (sec[3] >= sec[0]):
            sumOverlap += 1
        elif (sec[2] <= sec[1]) and (sec[3] >= sec[1]):
            sumOverlap += 1

    sumOverlap += sumFullOverlap
    
    print("PART 1:")
    print("   Sum of pairs in which one elf's assignment fully overlaps the other's:", sumFullOverlap)

    print("PART 2:")
    print("   Sum of pairs in which one elf's assignment fully or partially overlaps the other's:", sumOverlap)

    file.close()

if __name__ == '__main__':
    main(sys.argv[1:])
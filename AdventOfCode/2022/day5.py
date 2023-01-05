#!/usr/bin/env python

import sys
import re

def main(argv):
    if(len(argv)!=1):
        print("Incorrect number of arguments given, 1 expected,", len(argv), "given.")
        print("Usage: python day5.py [filename]")
        sys.exit()

    try:
        file = open(argv[0],'r')
    except Exception:
        print("Could not open/read file:",argv[0])
        sys.exit()

    numStacks = 0
    maxHeight = 0

    crateData = []

    for lineNum, line in enumerate(file):
        line = re.sub("\n","",line)
        if '[' not in line:
            stackIndices = []
            for i, char in enumerate(line):
                if char.isnumeric():
                    stackIndices.append(i)
            numStacks = len(stackIndices)
            maxHeight = lineNum
            break
        crateData.append(line)

    if numStacks == 0 or maxHeight == 0:
        print("Input File Format Error")
        sys.exit()

    stacks = []
    stacks2 = []
    for i in range(numStacks):
        stacks.append([])
        stacks2.append([])
    
    for row in crateData:
        for i in range(numStacks):
            if(row[stackIndices[i]]!=' '):
                stacks[i].insert(0,row[stackIndices[i]])
                stacks2[i].insert(0,row[stackIndices[i]])


    
    for lineNum, line in enumerate(file):
        if(lineNum != 0):
            line = re.sub("move|from|to","",line.strip()).split()
            cmd = [ int(x) for x in line ]
        
            # PART 1: 9000
            for i in range(cmd[0]):
                stacks[cmd[2]-1].append(stacks[cmd[1]-1].pop())
            
            # PART 2: 9001
            insertIndex = len(stacks2[cmd[2]-1])
            for i in range(cmd[0]):
                stacks2[cmd[2]-1].insert(insertIndex,stacks2[cmd[1]-1].pop())

    topCrates1 = ""
    for stack in stacks:
        topCrates1 += stack[len(stack)-1]

    topCrates2 = ""
    for stack in stacks2:
        topCrates2 += stack[len(stack)-1]
    
    print("PART 1:")
    print("   Crates on the top of each stack using CraneMover9000:", topCrates1)

    print("PART 2:")
    print("   Crates on the top of each stack using CraneMover9001:", topCrates2)

    file.close()

if __name__ == '__main__':
    main(sys.argv[1:])
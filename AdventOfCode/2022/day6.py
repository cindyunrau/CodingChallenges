#!/usr/bin/env python

import sys

def uniqueString(stream,length):
    charRead = 0
    found = False
    marker = []
    for i in range(length):
        marker.append('')

    char = stream.read(1)
    while char and not found:
        charRead += 1
        marker = marker[1:]
        if char not in marker and len(marker) == len(set(marker)) and charRead > length:
            found = True
        marker.append(char)
        char = stream.read(1)

    return charRead


def main(argv):
    if(len(argv)!=1):
        print("Incorrect number of arguments given, 1 expected,", len(argv), "given.")
        print("Usage: python day6.py [filename]")
        sys.exit()

    try:
        file = open(argv[0],'r')
    except Exception:
        print("Could not open/read file:",argv[0])
        sys.exit()

    charRead = uniqueString(file,4)

    print("PART 1:")
    print("   Number of characters processed before start of packet marker found:", charRead)

    file.seek(0)
    charRead = uniqueString(file,14)

    file.close()

    print("PART 2:")
    print("   Number of characters processed before start of packet marker found:", charRead)


if __name__ == '__main__':
    main(sys.argv[1:])
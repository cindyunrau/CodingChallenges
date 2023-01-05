#!/usr/bin/env python

import sys

validPlayerMoves = ["X","Y","Z"]
validOpponentMoves = ["A","B","C"]
rock = ["X","A"]        # also win
paper = ["Y","B"]       # also draw
scissors = ["Z","C"]    # also lose
lose = "X"
draw = "Y"
win = "Z"

def calcRoundScore(player, opponent):
    score = 0
    if player in rock:
        score += 1
        if(opponent in rock):
            score += 3
        elif(opponent in scissors):
            score += 6
    elif player in paper:
        score += 2
        if(opponent in paper):
            score += 3
        elif(opponent in rock):
            score += 6
    elif player in scissors:
        score += 3
        if(opponent in scissors):
            score += 3
        elif(opponent in paper):
            score += 6

    return score

def calcRoundMove(outcome, opponent):
    move = "A"
    if outcome is win:
        if opponent in rock:
            move = "B"
        elif opponent in paper:
            move = "C"
    elif outcome is draw:
        if opponent in paper:
            move = "B"
        elif opponent in scissors:
            move = "C"  
    elif outcome is lose:
        if opponent in scissors:
            move = "B"
        elif opponent in rock:
            move = "C"     
        
    return move
        

def main(argv):
    if(len(argv)!=2):
        print("Incorrect number of arguments given, 1 expected,", len(argv), "given.")
        print("Usage: python day2.py [filename] [partNum]")
        sys.exit()

    try:
        file = open(argv[0],'r')
    except Exception:
        print("Could not open/read file:",argv[0])
        sys.exit()
    
    partNum = int(argv[1])
    totalScore = 0

    for lineNum, line in enumerate(file):
        moves = line.strip().split(' ',1)

        if moves[0] not in validOpponentMoves or moves[1] not in validPlayerMoves:
            print("Invalid characters in file. Line #",lineNum)
            sys.exit()

        if(partNum == 1):
            totalScore += calcRoundScore(moves[1],moves[0])
        else:
            playerMove = calcRoundMove(moves[1],moves[0])
            totalScore += calcRoundScore(playerMove,moves[0])

        

    print("Total Player Score:", totalScore)

    file.close()

if __name__ == '__main__':
    main(sys.argv[1:])
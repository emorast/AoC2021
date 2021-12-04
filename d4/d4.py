from os import remove
import numpy as np

def isComplete(m):

    col = np.sum(m, axis = 0)
    row = np.sum(m, axis = 1)

    if 500 in col:

        return True

    elif 500 in row:

        return True

    else:

        return False

def readInput(file, div):

    with open(file) as f:
        
        # Read drawn numbers
        content = f.readline()
        num = content.strip().split(',')

        matrix = np.loadtxt(file, skiprows = 2)
        matrices = np.vsplit(matrix, div)

        return num, matrices

def part1(num, matrices):

    
    noWinner = True
    for n in num:

        for m in matrices:
            
            if int(n) in m:

                m[m == int(n)] = 100

                if isComplete(m):
                    
                    winner = m
                    noWinner = False

                    break
        if not noWinner:

            break

    winner[winner == 100] = 0
    sum = int(winner.sum())
    print(sum*int(n))
        
    return

def part2(num, matrices):
   
    d = {}
    i = 0
    
    for m in matrices:

        d[i] = m

        i += 1
    for n in num:
        
        todelete = []
        for key in d:

            if int(n) in d[key]:
                
                m = d[key]
                
                m[m == int(n)] = 100

                if isComplete(m):

                    todelete.append(key)
        
        for key in todelete:
            del d[key]

        if not d:

            m[m == 100] = 0
            sum = int(m.sum())
            print(sum*int(n))

            break

def main():

    num, matrices = readInput('input.txt', 100)

    part1(num, matrices)

    num, matrices = readInput('input.txt', 100)

    part2(num, matrices)

if __name__ == "__main__":
    main()
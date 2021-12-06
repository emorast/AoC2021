import numpy as np
import re

from numpy.core.defchararray import isdecimal

class Line:

    def __init__(self, x0, y0, x1, y1):

        self.xstart = int(x0)
        self.xend = int(x1)
        self.ystart = int(y0)
        self.yend = int(y1)

def readInput(file):

    with open(file) as f:
        
        lines = f.readlines()
    
    seg = []
    for line in lines:
        regex = re.compile(r'[0-9][0-9]?[0-9]?')
        x = regex.findall(line)
        l = Line(x[0],x[1],x[2],x[3])

        if l != None:
            
            seg.append(l)

    return seg

def notDiagonal(line):

    if line.xstart == line.xend or line.ystart == line.yend:

        return True

    else:

        return False

def findDim(lines):
    
    xmax = 0
    ymax = 0
    
    for line in lines:

        if line.xstart > xmax:

            xmax = line.xstart
        
        elif line.xend > xmax:

            xmax = line.xend

        if line.ystart > ymax:

            ymax = line.ystart
        
        elif line.yend > ymax:

            ymax = line.yend

    return xmax, ymax

def main():

    seg = readInput("input.txt")
    
    xmax, ymax = findDim(seg)
    
    m = np.zeros((ymax+1, xmax+1), dtype = int)

    for line in seg:

        if notDiagonal(line):

            if line.xstart > line.xend:
                xs = line.xend
                xe = line.xstart
            else:
                xs = line.xstart
                xe = line.xend
            if line.ystart > line.yend:
                ys = line.yend
                ye = line.ystart
            else:
                ys = line.ystart
                ye = line.yend

            for i in range(ys,ye+1):
                for j in range(xs, xe+1):

                    m[i][j] += 1
        else:
            print(line.xstart, line.ystart, line.xend, line.yend)
            r = abs(line.xend - line.xstart)

            if line.ystart < line.yend and line.xstart < line.xend: #ok

                for i in range(0,r+1):
                    m[line.ystart+i][line.xstart+i] += 1
                
            elif line.ystart > line.yend and line.xstart < line.xend: #ok

                for i in range(0,r+1):
                    m[line.ystart-i][line.xstart+i] += 1

            elif line.ystart < line.yend and line.xstart > line.xend:

                for i in range(0,r+1):
                    m[line.ystart+i][line.xstart-i] += 1

            elif line.ystart > line.yend and line.xstart > line.xend:

                for i in range(0,r+1):
                    m[line.ystart-i][line.xstart-i] += 1
            
    print(m)

    n = 0
    for row in m:
        for col in row:

            if col > 1:

                n += 1

    print(n)

if __name__ == "__main__":
    main()
class Basin:

    def __init__(self):

        self.size = 0

def findBasin(i, j, hmap, visited, basin):

    visited[i][j] = visited[i][j] + 1
    basin.size +=1

    if hmap[i+1][j] < 9 and visited[i+1][j] != 1:

        findBasin(i+1,j,hmap, visited, basin)
    
    if hmap[i-1][j] < 9 and visited[i-1][j] != 1:

        findBasin(i-1,j,hmap, visited, basin)

    if hmap[i][j+1] < 9 and visited[i][j+1] != 1:

        findBasin(i,j+1,hmap, visited, basin)
    
    if hmap[i][j-1] < 9 and visited[i][j-1] != 1:

        findBasin(i,j-1,hmap, visited, basin)

def readInput(file):

    with open(file) as f:

        content = f.readlines()
        nRow = len(content)
        nCol = len(content[0].strip())
        hmap = []
        hmap.append([10]*(nCol+2))

        for line in content:

            temp = line.strip()
            x = list(temp)
            num = [int(i) for i in x]
            num.insert(0, 10)
            num.append(10)
            hmap.append(num)
        
        hmap.append([10]*(nCol+2))

        return hmap, nRow, nCol

def main():
    
    #hmap, nRow, nCol= readInput('test.txt')
    hmap, nRow, nCol = readInput('input.txt')

    visited = []
    visited.append([0]*(nCol+2))
    for i in range(0, nRow+1):
        visited.append([0]*(nCol+2))
    
    basins = []
    minArr = []
    for row in range(1, nRow+1):
        for col in range(1,nCol+1):

            if hmap[row][col] >= hmap[row-1][col]:

                continue

            elif hmap[row][col] >= hmap[row+1][col]:

                continue

            elif hmap[row][col] >= hmap[row][col-1]:

                continue

            elif hmap[row][col] >= hmap[row][col+1]:

                continue
            
            else:

                minArr.append(hmap[row][col])

                basin = Basin()
                findBasin(row, col, hmap, visited, basin)
                basins.append(basin)

  # Print result part 1
    risk = 0
    for point in minArr:
        risk += (1+point)
    
    print(risk)

    # Print result part 2
    arr = []
    for basin in basins:
        arr.append(basin.size)
    
    arr.sort(reverse=True)

    print(arr[0]*arr[1]*arr[2])

if __name__ == "__main__":
    main()
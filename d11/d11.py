def readInput(file):
    with open(file) as f:
        content = f.readlines()
        nCol = len(content[0].strip())
        mat = []
        mat.append([10]*(nCol+2))

        for line in content:

            temp = line.strip()
            x = list(temp)
            num = [int(i) for i in x]
            num.insert(0, 10)
            num.append(10)
            mat.append(num)
        
        mat.append([10]*(nCol+2))

        return mat

def chain(mat, heap, count):
        
    if len(heap) != 0:

        for item in heap:

            i, j = heap.pop()
            count += 1
            
            for m in range(-1,2):
                for n in range(-1,2):

                    if mat[i+m][j+n] == 9:

                        mat[i+m][j+n] = 0
                        heap.append([i+m,n+j])

                    if mat[i+m][j+n] != 0:
                        
                        mat[i+m][j+n] += 1

                    elif mat[i+m][j+n] == 10:

                        continue

        mat, count = chain(mat, heap, count)

    return mat, count

def main():

    count = 0
    #mat = readInput('mini.txt')
    #mat = readInput('test.txt')
    mat = readInput('input.txt')

    for step in range(1,1000):
 
        heap = []
        for i in range(1,11):
            for j in range(1, 11):
                
                if mat[i][j] == 9:

                    index = [i, j]
                    
                    mat[i][j] = 0

                    heap.append(index)
                else:
                    mat[i][j] += 1

        mat, count = chain(mat,heap,count)

        print("Step: " + str(step))
        sum = 0
        for i in range(1,11):
            for j in range(1, 11):

                sum += mat[i][j]

        if sum == 0:

            break

    print(count)

if __name__ == "__main__":
    main()
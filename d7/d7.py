class Crab:

    def __init__(self, pos, cost = 0):

        self.pos = int(pos)
        self.cost = cost

def readInput(file):

    with open(file) as f:
        
        content = f.readline()
        input = content.strip().split(',')

    return input

def f(d):
    
    cost = 0
    for i in range(1, d+1):
        cost += i
    

    return(cost)

def main():

    #input = readInput('test.txt')
    input = readInput('input.txt')
    
    list = []
    max_pos = 0
    for x in input:
        list.append(Crab(x))

        if int(x) > max_pos:
            max_pos = int(x)

    min = float('inf')
    for i in range(0, max_pos+1):

        d = 0
        for j in list:

            d += f(abs(i - j.pos))
        
        if d < min:
            min = d

    print(min)

if __name__ == "__main__":
    main()


class Lanternfish:

    def __init__(self, init_time):

        self.time = init_time

def readInput(file):

    with open(file) as f:
        
        content = f.readline()
        input = content.strip().split(',')

    return input

def part1():
    days = 80
    n = 0

    input  = readInput('input.txt')

    pop = []
    for fish in input:

        x = Lanternfish(int(fish))
        pop.append(x)
        n += 1
    
    for day in range(0, days):

        toAdd = []
        for fish in pop:

            fish.time -= 1

            if fish.time < 0:

                fish.time = 6

                x = Lanternfish(8)
                toAdd.append(x)
        
        for x in toAdd:
            pop.append(x)
            n += 1
    
    print(n)

def part2():

    pass

def main():

    part1()

    part2()

if __name__=="__main__":
    main()
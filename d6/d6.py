
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

    input  = readInput('input.txt')
    days = 256

    tank = (dict((int(l), input.count(l)) for l in set(input)))
    tank.update({6: 0, 7: 0, 8: 0, 0: 0})
    
    n = 0
    for key in tank:
        n += tank[key]
    
    tank.update({'n': n})

    for i in range(days):

        temp = {0: tank[1], 1: tank[2], 2: tank[3], 3: tank[4], 4: tank[5], 5: tank[6], 6: tank[7] + tank[0], 7: tank[8], 8: tank[0], 'n': tank['n'] + tank[0]}
        tank = temp

    print(tank)

def main():

    part1()

    part2()

if __name__=="__main__":
    main()
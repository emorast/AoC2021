def readInput(file):

    with open(file) as f:
        
        lines = f.readlines()
    
    list = []
    for line in lines:
    
        list.append(line.strip())

    return list

def part1():

    list = readInput('input.txt')
    #list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    prev_scan = None;
    count = 0
    for scan in list:

        if prev_scan != None:

            if int(prev_scan) <= int(scan):

                count = count + 1

        prev_scan = scan

    print(count)

    return


def part2():
    
    list = readInput('input.txt')
    #list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    prev_sum = None
    count = 0
    
    for i in range(0, len(list)-2):

        sum = int(list[i]) + int(list[i+1]) + int(list[i+2])

        if prev_sum != None:

            if prev_sum < sum:
                count = count + 1
        
        prev_sum = sum
    
    print(count)

    return

def main():

    part1()

    part2()

    return


if __name__ == "__main__":
    main()
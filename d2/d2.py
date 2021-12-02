def readInput(file):

    with open(file) as f:
        
        lines = f.readlines()
    
    list = []
    for line in lines:
    
        list.append(line.strip())

    return list
def main():

    list = readInput('input.txt')

    x = 0
    depth = 0
    aim = 0

    for command in list:

        s = command.split()
        
        if s[0] == 'up':

            aim = aim - int(s[1])

        elif s[0] == 'down':

            aim = aim + int(s[1])

        elif s[0] == 'forward':

            x = x + int(s[1])
            depth = depth + aim*int(s[1])

    print(depth*x)

    return

if __name__ == "__main__":
    
    main()
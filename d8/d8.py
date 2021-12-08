import re

def readInput(file):

    with open(file) as f:
        
        lines = f.readlines()

        inp = []
        out = []
        for line in lines:

            temp = line.strip().split('|')
            regex = re.compile(r'[a-g]+')
            x = regex.findall(temp[1])
            y = regex.findall(temp[0])
            out.append(x)
            inp.append(y)

    return inp, out


def findall(seq, sub):
    
    for i in sub:
        
        found = False
        for char in seq:

            if char == i:

                found = True
        
        if found == False:
            
            break

    if found == True:
        
        return True
    else:

        return False

def main():

    # inp, out = readInput('test.txt')
    inp, out = readInput('input.txt')
    # Pick the easy ones
    output = []
    sum = 0
    for i, o in zip(inp,out):

        d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        rest = []
        for j in i:

            if len(j) == 7:
                d[8] = j

            elif len(j) == 4:
                d[4] = j
            
            elif len(j) == 3:
                d[7] = j

            elif len(j) == 2:
                d[1] = j

            else:
                rest.append(j)
        
        # Divide into subgroups
        for j in rest:

            # 9, 0 ,3
            if findall(j, d[1]):

                if len(j) == 5:
                    d[3] = j

                else:

                    if findall(j, d[4]):
                        d[9] = j
                    
                    else:
                        d[0] = j

            # 5, 6, 2
            else:

                if len(j) == 6:
                    d[6] = j
                
                else:

                    count = 0
                    for m in d[4]:
                        for n in j:

                            if m == n:
                                count += 1

                    if count == 3:
                        d[5] = j

                    else:
                        d[2] = j
        print(d)
        
        nr = ''
        for x in o:
            

            for key in d:

                if findall(x, d[key]) and len(x) == len(d[key]):

                    nr += str(key)

        sum += int(nr)
    
    print(sum)

if __name__ == "__main__":
    main()
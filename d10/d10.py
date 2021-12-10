import re
start = {'(': ')', '[': ']', '{': '}', '<': '>'}
scoring1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scoring2 = {'(': 1, '[': 2, '{': 3, '<': 4}

def readInput(file):

    with open(file) as f:
        
        lines = f.readlines()
        
        data = []
        for line in lines:

            arr = list(line.strip())

            data.append(arr)

    return data

def middle(lst):
  half_len = int((len(lst) / 2))
  
  if len(lst) % 2 == 0:
   return (lst[half_len -1] + lst[half_len]) / 2
  
  else:
   return lst[half_len]

def main():

    #data = readInput('test.txt')
    data = readInput('input.txt')

    sum = 0
    points = []
    for line in data:

        prev = []
        for i in range(0, len(line)):
            
            x = line[i]

            if x in start:
                
                prev.append(x)
            
            else:
                

                if x == start[prev[len(prev)-1]]:

                    prev.pop()

                else:

                    sum += scoring1[x]
                    
                    break
                
            if i == len(line)-1:
                
                prev.reverse()

                score = 0
                for s in prev:

                    score = score*5 + scoring2[s]
                
                points.append(score)

    points.sort()

    print(middle(points))

    #print(sum)

if __name__ == "__main__":
    main()
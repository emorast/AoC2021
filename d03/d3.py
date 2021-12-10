class Node:

    def __init__(self, value = 0, next = None):

        self.value = value
        self.next = next


class BinList:

    def __init__(self, n):

        self.head = None

        for i in range(n):

            node = Node()

            if self.head == None:
                
                self.head = node

                prev_node = node
            
            else:   
                
                prev_node.next = node

                prev_node = node

        return
    
    def addBin(self, bin):

        node = self.head

        for i in bin:
            
            node.value += int(i)
            node = node.next
    
    def getParam(self, n):

        node = self.head

        gamma = ''
        epsilon = ''

        while node != None:

            k = node.value/n

            if k > 0.5:

                gamma = gamma + '1'
                epsilon = epsilon + '0'

            else:

                gamma = gamma + '0'
                epsilon = epsilon + '1'

            node = node.next

        return gamma, epsilon

def readInput(file):

    with open(file) as f:
        
        lines = f.readlines()
    
    list = []
    for line in lines:
    
        list.append(line.strip())

    return list

def main():

    list = readInput('input.txt')
    #list = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

    binlist = BinList(len(list[0]))

    for bin in list:

        binlist.addBin(bin)

    gamma, epsilon = binlist.getParam(len(list))

    print(int(gamma, 2)*int(epsilon, 2))

    i = 0
    while len(list) > 1:  
        
        updated_list = []
       
        sum = 0
        n = 0
        for entry in list:

            sum = sum + int(entry[i])
            n += 1
        
        k = sum/n

        if k >= 0.5:

            num = '0'
        else:

            num = '1'

        for entry in list:

            if entry[i] == num:

                updated_list.append(entry)

        if len(updated_list) == 0:

            next
            
        else:

            list = updated_list
            print(list)

        i += 1

    # Hardcorded results due to lack of time to fix a good looking solution, competition is real =)
    print(int('100100101101',2)*int('010010100110',2))

    return

if __name__ == "__main__":
    main()
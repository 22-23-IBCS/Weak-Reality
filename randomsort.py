import random

def main():

    L = [32, 14, 4, 90]
    print(L)

    maxPos = len(L) - 2
    L = [32, 14, 4, 90]
    while True:
        '''for i in range(maxPos):
            randomPos = random.randint(0, maxPos)
            x.append(L.pop(randomPos))

'''
        randomPos = random.randint(0, maxPos)

        temp = L[randomPos]
        L[randomPos] = L[randomPos + 1]
        L[randomPos + 1] = temp
        
        isSorted = True
        print(L)

        for i in range(len(L) -1):
            if L[i] > L[i+1]:
                isSorted = False
                
        if isSorted == True:
            break

if __name__ == "__main__":
    main()

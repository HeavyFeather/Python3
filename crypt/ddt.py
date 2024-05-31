import random
import string

def createDDT():
    DDT = [ [0]*8 for i in range(8) ]

    for i in range(len(DDT)):
        for j in range(len(DDT[i])):
            tmp = i ^ j
            c = sbox.get(i)
            c1 = sbox.get(j)
            dc = c ^ c1
            DDT[tmp][dc] += 1


    for row in DDT:            # делаем перебор всех строк матрицы A
        for elem in row:     # перебираем все элементы в строке row
            print(elem, end = ' ')
        print()

def createRandX():
    for i in range(5):
        for j in range (3):
            print(bin(random.randint(1,7)))
        print()

def xorK(a, k):
    for i in range(len(a)):
        a[i] = a[i] ^ k[i]
    return a

def sub(a, sbox):
    for i in range(len(a)):
        a[i] = sbox.get(a[i])
    return a

def per(a):
    b = [0] * 3 
    b[0] = (a[0] & 4) | ((a[1] & 4) >> 1) | ((a[2] & 4) >> 2)
    b[1] = ((a[0] & 2) << 1) | (a[1] & 2) | ((a[2] & 2) >> 1)
    b[2] = ((a[0] & 1) << 2) | ((a[1] & 1) << 1) | (a[2] & 1)
    return b

def firstR(a, k):
    a = xorK(a,k)
    a = sub(a, sbox)
    a = per(a)
    return a

def lastR(a,k):
    a = xorK(a, k)
    a = sub(a, sbox)
    a = xorK(a, k)
    return a

def encr(a, k):
    a = firstR(a,k)
    a = firstR(a,k)
    a = lastR(a,k)
    printBin(a)
    return a


def printBin(li):
    print(li)
    for elem in li:
        print(bin(elem))
    print()

def xor(a, D):
    b = [0] * 3
    for i in range(len(a)):
        b[i] = a[i] ^ D[i]
    return b

if __name__ == '__main__':
    key = [6,2,1]
    a = [0] * 3
    sbox = {0:4,1:5,2:2,3:0,4:7,5:6,6:1,7:3}
    #createRandX()
    #createDDT()
    D = [4,0,0]


    for i in range(1,6):
        # Здесь посчитали X
        print(f"X{i}: ")
        for j in range(len(a)):
            a[j] = random.randint(1,7)

        b = xor(a,D) # D - дифференциал
        printBin(a)
        print()

        # Зашифровали X
        print(f"Y{i}:")
        encr(a,key)
        print()
        
        print(f"X'{i}:")
        printBin(b)
        print()

        print(f"Y'{i}:")
        b = encr(b,key)

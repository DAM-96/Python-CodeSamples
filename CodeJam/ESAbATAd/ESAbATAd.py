from sys import *
T = input().split()
for i in range(len(T)):
  T[i] = int(T[i])

def identify_bitmov(bitinit, bitend, bitnew):
    comp = []
    if bitinit == bitnew:
        return 0
    else:
        for i in range(len(bitnew)):
            if bitnew[i] == '0':
                comp.append('1')
            else:
                comp.append('0')
        for j in range(len(comp)):
            if comp[j] != bitinit[j]:
                break
            if j == (len(comp)-1):
                return 1
        del comp
        comp = []
        for k in range(len(bitend)):
            comp.append(bitend[len(bitend)-k-1])
        if comp == bitnew:
            return 2
        else:
            return 3



def bit_predict(bitmov, bitstring,bitref):
    comp = []
    if bitmov == 1:
        for i in range(len(bitstring)):
            if bitstring[i] == '0':
                comp.append('1')
            else:
                comp.append('1')
        for j in range(len(comp)):
            bitstring[j] = comp[j]
    elif bitmov == 2:
        for k in range(len(bitref)):
            comp.append(bitref[len(bitref)-k-1])
    return bitstring




for cases in range(T[0]):
    B = []
    Bcur = []
    Btemp = []
    Binit = []
    Bend = []
    iteration = 0
    knownbits = 0
    while True:
        if T[1] == 10:
            for i in range(1,11):
                print(i)
                stdout.flush()
                B.append(input())
        else:
            while True:
                iteration += 1
                if iteration == 1:
                    for i in range(1,11):
                        if i <= 5:
                            print(i)
                            stdout.flush()
                            Binit.append(input())
                        else:
                            print(T[1] - 10 + i)
                            stdout.flush()
                            Bend.append(input())
                        knownbits = 10

                elif iteration%2 == 0:
                    for i in range(1,6):
                        print(i + ((iteration/2)-1) * 5)
                        stdout.flush()
                        Bcur.append(input())
                    for j in range(6,11):
                        knownbits += 1>
                        print(i + ((iteration/2)-1) * 5)
                        stdout.flush()
                        Btemp.append(input())

                else:
                    None
                bitmov = identify_bitmov(Binit, Bend, Bcur)





        B = ''.join(B)
        print(B)
        stdout.flush()
        if(input()!= 'N'):
            break
        else:
            del B, Bcur, Bend, Binit, Btemp, knownbits, iteration
    del B, Bcur, Btemp, Binit, Bend
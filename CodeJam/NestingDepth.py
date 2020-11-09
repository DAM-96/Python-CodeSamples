T = int(input())

for cases in range(T):
    openP = '('
    closeP = ')'
    pendCloseP = 0
    S = list(input())
    outputS = []
    for i in S:
        if pendCloseP > 0:
            if (pendCloseP < int(i)):
                for j in range(int(i) - pendCloseP):
                    outputS.append(openP)
                    pendCloseP += 1
                outputS.append(i)
            else:
                for k in range(pendCloseP - int(i)):
                    outputS.append(closeP)
                    pendCloseP -= 1
                outputS.append(i)
        else:
            for j in range(int(i)):
                outputS.append(openP)
                pendCloseP += 1
            outputS.append(i)

    for l in range(pendCloseP):
        outputS.append(closeP)
    outputS = ''.join(outputS)
    print("Case #{}: {}".format(cases + 1, outputS))
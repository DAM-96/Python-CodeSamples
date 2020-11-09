T = int(input())
Words = []
wordInit = []
wordEnd = []
wordMiddle = []
output = '*'

def containsString(stringA, stringB, pos):
    if len(stringA) < len(stringB) or pos == None:
        return False
    if pos == 0: ##EndsWithAsterisk
        for i in range(len(stringB)-1):
            if stringA[len(stringA) - len(stringB) + i + 1 ] is not stringB[i + 1]:
                return False
    if pos == 1: ##StartsWithAsterisk
        for i in range(len(stringB)-1):
            if stringA[i] is not stringB[i]:
                return False
    return True

for cases in range(T):
    N = int(input())
    for ipt in range(N):
        Words.append(input())
    for ipt in range(N):
        if Words[ipt][0] == '*':
            if wordInit == []:
                wordInit.append(Words[ipt])
            else:
                if not containsString(wordInit[0], Words[ipt], 0):
                    break
                else:
                    if not containsString(Words[ipt], wordInit[0], 0):
                        break
                    else:
                        wordInit[0] = Words[ipt]
        elif Words[ipt][len(Words[ipt])-1] == '*':
            if wordEnd == []:
                wordEnd.append(Words[ipt])
            else:
                if not containsString(wordEnd[0], Words[ipt], 1):
                    break
                else:
                    if not containsString(Words[ipt], wordEnd[0], 1):
                        break
                    else:
                        wordEnd[0] = Words[ipt]
        else:
            tempInit = []
            tempEnd = []
            asteriskPos = 0
            for i in range(len(Words[ipt])):
                if Words[ipt][i] == '*':
                    asteriskPos = i
                if asteriskPos == 0:
                    tempEnd.append(Words[ipt][i])
                    if i == len(Words[ipt]) - 1:
                        tempInit = tempEnd
                        tempInit.insert(0, '*')
                        tempEnd.append('*')
                elif asteriskPos == i:
                    tempEnd.append(Words[ipt][i])
                    tempInit.append(Words[ipt][i])
                else:
                    tempInit.append(Words[ipt][i])
            if wordInit == []:
                wordInit.append(tempInit)
            else:
                if not containsString(wordInit[0], tempInit, 0):
                    break
                else:
                    if not containsString(tempInit, wordInit[0], 0):
                        break
                    else:
                        wordInit[0] = Words[ipt]
            if wordEnd == []:
                wordEnd.append(tempEnd)
            else:
                if not containsString(wordEnd[0], tempEnd, 1):
                    break
                else:
                    if not containsString(tempEnd, wordEnd[0], 1):
                        break
                    else:
                        wordEnd[0] = tempEnd
    if cases == T-1:
        for i in range(len(wordEnd)-1):
            output.append(wordEnd[i])
        for i in range(len(wordInit)-1):
            output.append(wordInit[i+1])

    print("Case #{}: {}".format(cases + 1, output))



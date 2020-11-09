T = int(input())

for cases in range(T):
    trace = 0
    rowrepeated = 0
    colrepeated = 0

    N = int(input())
    M = []
    for i in range(N):
        row = input().split()
        for j in range(len(row)):
            row[j] = int(row[j])
        M.append(row)

    for i in range(N):
        tempcol = []
        trace += M[i][i]
        for k in range(N):
            tempcol.append(M[k][i])
        for j in range(N - 1):
            if M[i].count(M[i][j]) > 1:
                rowrepeated += 1
                break
        for l in tempcol:
            if tempcol.count(l) > 1:
                colrepeated += 1
                break
        del tempcol


    print("Case #{}: {} {} {}".format(cases + 1, trace, rowrepeated, colrepeated))
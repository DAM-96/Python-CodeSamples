T = int(input())

for cases in range(T):
    N = int(input())
    S = []
    taskStatus = []
    for ipt in range(N):
        tasks = input().split()
        tasks.append(ipt)
        for j in range(len(tasks)):
            tasks[j] = int(tasks[j])
        S.append(tasks)

    S.sort()

    def is_available(partner, task):
        if partner == []:
            None
        else:
            for T in partner:
                if ((task[0] <= T[0]) and (task[1] > T[0])) or ((task[1] >= T[1]) and (task[0] < T[1])) or ((task[0] >= T[0]) and (task[1] <= T[1])):
                    return False
        partner.append(task)
        return True

    C = []
    J = []
    :
    for i in range(len(S)):
        if is_available(C, S[i])
            S[i].append("C")
        elif is_available(J, S[i]):
            S[i].append("J")
        else:
            taskStatus = "IMPOSSIBLE"
            break
        if i == (len(S) - 1):
            S.sort(key=lambda x: x[2])
            for j in range(len(S)):
                taskStatus.append(S[j][3])
            taskStatus = ''.join(taskStatus)

    print("Case #{}: {}".format(cases + 1, taskStatus))

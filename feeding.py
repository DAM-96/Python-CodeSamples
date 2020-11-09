bucketNum, weightCap = input().split()
bucketNum = int(bucketNum)
weightCap = int(weightCap)

buckets = input().split()
for i in range(len(buckets)):
    buckets[i] = int(buckets[i])
buckets.sort()

bucketPairs = []

for i in range(len(buckets)):
    for j in range(len(buckets)-1):
        if buckets[-1] + buckets[(j*-1)-1] > weightCap:
            if buckets[(j*-1)-1] == buckets[-1]:
                bucketPairs.append(buckets[-1])
                buckets.pop(-1)
                break
            else:
                continue
        else:
            bucketPairs.append([buckets[-1], buckets[(j*-1)-1]])
            buckets.pop((j*-1)-1)
            buckets.pop(-1)
            break
    if len(buckets) == 1:
        bucketPairs.append(buckets[-1])
        break

print(len(bucketPairs))

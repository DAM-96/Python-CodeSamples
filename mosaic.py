# Problem M. Mosaic Mansion
# Source file name: mosaic.c, mosaic.cpp, mosaic.java, mosaic.py
# Input: Standard
# Output: Standard
# A mosaic is a picture made from square tiles arranged in a grid, at least for today’s purposes.
# We would like to make a mosaic with exactly the same number of tiles of each colour. We will do this by
# taking an existing design and removing some of the rows from it.
# 1 2 1 2 3 1 2 3 4 3
# 5 2 5 3 5 5 5 5 1 4
# 2 3 2 1 4 3 3 2 1 4
# 1 2 3 4 4 4 4 1 2 3
# Figure M.1: Illustration of a solution to Example Input 1. The three rows annotated with white can be
# kept, giving 6 of each colour of tile.
# What is the greatest number of rows we can keep?

rowNum, columnNum, colors = map(int,input().split())
rowMap = []

for i in range(rowNum):
    rowMap.append([int(j) for j in input().split()])

colorCount = rowMap
colorCountTot = []
for i in rowMap:
    for j in range(colors):
        if len(colorCountTot) != colors:
            colorCountTot.append(i.count(j+1))
            print(colorCountTot)
        else:
            colorCountTot[j] += i.count(j+1)
        

print(rowMap)
print(colorCountTot)
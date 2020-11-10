#Count the amount ofelements out of order in an array.

def countOutOfPlace(height):
    initialHeight = [0 for i in range(len(height))]
    for i in range(len(height)):
        initialHeight[i] = height[i]
    height.sort()
    outOfPlace = 0
    for i in range(len(height)):
        if height[i] != initialHeight[i]:
            outOfPlace += 1
    return outOfPlace

matrix = [1,2,3,4,5,8,7,6,9,10]
print(countOutOfPlace(matrix))
#This script will read 3 numbers "n", "x" and "y" and print a validation for each number in the range 1:n of whether the number is divisible by x, divisible by y or divisible by both.
def xyMultiple(n,x,y):
    for i in range(1,n+1):
        isDivX = False
        isDivY = False
        res = "Div by "
        if i % x == 0:
            isDivX = True
            res += str(x)
        if i % y == 0:
            isDivY = True
            res += str(y)
        if isDivX or isDivY:
            if isDivX and isDivY:
                res = "Div by Both"
        else:
            res = i
        print(res)


xyMultiple(2500,7,13)
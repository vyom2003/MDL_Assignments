import numpy as np
import copy
grid = [
    [0, 1, -1],
    [0, 0, 0],
    [0, 2, 0],
    [0, 0, 0]
]


def FuncUp(i, j):
    sum = 0
    if(i == 0 or grid[i-1][j] == 2):
        return -10000000
    sum += grid[i-1][j]*0.7
    if(j == 0 or grid[i][j-1] == 2):
        sum += 0.15*grid[i][j]
    else:
        sum += 0.15*grid[i][j-1]
    if(j == 2 or grid[i][j+1] == 2):
        sum += 0.15*grid[i][j]
    else:
        sum += 0.15*grid[i][j+1]
    return sum


def FuncDown(i, j):
    sum = 0
    if(i == 3 or grid[i+1][j] == 2):
        return -10000000
    sum += grid[i+1][j]*0.7
    if(j == 0 or grid[i][j-1] == 2):
        sum += 0.15*grid[i][j]
    else:
        sum += 0.15*grid[i][j-1]
    if(j == 2 or grid[i][j+1] == 2):
        sum += 0.15*grid[i][j]
    else:
        sum += 0.15*grid[i][j+1]
    return sum


def FuncLeft(i, j):
    sum = 0
    if(j == 0 or grid[i][j-1] == 2):
        return -10000000
    sum += grid[i][j-1]*0.7
    if(i == 0 or grid[i-1][j] == 2):
        sum += 0.15*grid[i][j]
    else:
        sum += 0.15*grid[i-1][j]
    if(i == 3 or grid[i+1][j] == 2):
        sum += 0.15*grid[i][j]
    else:
        sum += 0.15*grid[i+1][j]
    return sum


def FuncRight(i, j):
    sum = 0
    if(j == 2 or grid[i][j+1] == 2):
        return -10000000
    sum += grid[i][j+1]*0.7
    if(i == 0 or grid[i-1][j] == 2):
        sum += 0.15*grid[i][j]
    else:
        sum += 0.15*grid[i-1][j]
    if(i == 3 or grid[i+1][j] == 2):
        sum += 0.15*grid[i][j]
    else:
        sum += 0.15*grid[i+1][j]
    return sum


change = 1
action = [
    ['u', '-', '-'],
    ['u', 'u', 'u'],
    ['u', '-', 'u'],
    ['u', 'u', 'u']
]
iter = 0
while(change > 0.0001):
    iter+=1
    utility = np.zeros([4, 3])
    change = 0
    for i in range(0, 4):
        for j in range(0, 3):
            if(grid[i][j] == 2 or (i == 0 and j == 1) or (i == 0 and j == 2)):
                utility[i][j] = grid[i][j]
            else:
                maxim = -10000000
                if(-0.04+0.95*FuncUp(i, j) > maxim):
                    maxim = -0.04+0.95*FuncUp(i, j)
                    action[i][j] = 'u'
                if(-0.04+0.95*FuncDown(i, j) > maxim):
                    maxim = -0.04+0.95*FuncDown(i, j)
                    action[i][j] = 'd'
                if(-0.04+0.95*FuncLeft(i, j) > maxim):
                    maxim = -0.04+0.95*FuncLeft(i, j)
                    action[i][j] = 'l'
                if(-0.04+0.95*FuncRight(i, j) > maxim):
                    maxim = -0.04+0.95*FuncRight(i, j)
                    action[i][j] = 'r'
                utility[i][j] = copy.deepcopy(maxim)
                change = abs(grid[i][j]-utility[i][j])
    grid = copy.deepcopy(utility)
    print("Iteration Number ",iter," : ")
    for i in range(4):
        for j in range(3):
            if(grid[i][j] == 2):
                print('wall', end="\t")
            else:
                print(grid[i][j], end="\t")
        print()

print()
print("Policy = \n", action)

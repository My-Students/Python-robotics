grid = [[True, True, True, True, True, False],
    [False, False, True, True, True, False],
    [True, True, True, False, True, True],
    [True, False, False, True, True, False],
    [True, False, True, True, False, True],
    [True, False, True, True, True, False]]

def bool2int(mat):
    n = 1
    defM = []

    for i in grid:
        matrix = []
        for x in i:
            if (x == True):
                matrix.append(n)
                n=n+1
            else: 
                matrix.append(-1) 
        defM.append(matrix)

    print (defM)
    return defM

def adj2Dict(m):
    
    dictionary = {}
    matNeigh = []
    matDef = []
    for i in m:
        matNeigh = []
        for c in i:
            if (m[i][c] > 0):
                if (m[i][c+1] > 0):
                    matNeigh.append(m[i][c+1])
                if (m[i-1][c] > 0):
                    matNeigh.append(m[i-1][c])
                if (m[i][c-1] > 0):
                    matNeigh.append(m[i][c-1])
                if (m[i+1][c] > 0):
                    matNeigh.append(m[i+1][c])
        dictionary[i] = matNeigh

def main():
    m = bool2int(grid)
    adj2Dict(m)

if __name__ == "main":
    main()
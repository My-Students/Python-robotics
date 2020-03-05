grid = [[True, True, True, True, True, False],
        [False, False, True, True, True, False],
        [True, True, True, False, True, True],
        [True, False, False, True, True, False],
        [True, False, True, True, False, True],
        [True, False, True, True, True, False]]

def Bool2Numb(grid):
    n=1
    matrix=[]
    defM=[]
    for r in grid:
        matrix = []
        for c in r:
            if(c==True):
                matrix.append(n)
                n=n+1
            else:
                matrix.append(-1)
        defM.append(matrix)
    return defM
            
def adj2dict(mat):
    dictionary = {}
    matNeigh = []
    for i in mat:
        matNeigh = []
        for c in i:
            if (mat[i][c] > 0):
                if (mat[i][c+1] > 0):
                    matNeigh.append(mat[i][c+1])
                if (mat[i-1][c] > 0):
                    matNeigh.append(mat[i-1][c])
                if (mat[i][c-1] > 0):
                    matNeigh.append(mat[i][c-1])
                if (mat[i+1][c] > 0):
                    matNeigh.append(mat[i+1][c])
        dictionary[i] = matNeigh
    return dictionary


def main():
    m = Bool2Numb(grid)
    print(m)
    dic= adj2dict(m)
    print(dic)

if __name__ == "main":
    main()




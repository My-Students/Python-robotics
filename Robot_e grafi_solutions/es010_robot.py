def matrix2dict(matrix):
    number_of_nodes = 1
    for i in range(0,len(matrix)):
        for e in range(0,len(matrix)):
            if matrix[i][e]:
                matrix[i][e] = number_of_nodes
                number_of_nodes = number_of_nodes + 1

    print(matrix)

    d = {}
    offset = 1
    number_of_nodes= 1
    links =[]

    for r in range(0,len(matrix)):
        print(f"r ={r}")
        for e in range(0,len(matrix)):
            links= []
            #print(f" i = {i} e = {e} len = {len(matrix)}")
            if matrix[r][e]!= False:
                #print(f"[{i}][{e}] libero")
                if r-offset >= 0:
                    if(matrix[r-offset][e]!=False):
                        links.append(matrix[r-offset][e])

                if e-offset >= 0:
                    if(matrix[r][e-offset]!=False):
                        links.append(matrix[r][e-offset])

                if e+offset < len(matrix):
                    if(matrix[r][e+offset]!=False):
                        links.append(matrix[r][e+offset])

                if r+offset < len(matrix):
                    if(matrix[r+offset][e]!=False):
                        links.append(matrix[r+offset][e])

                d[number_of_nodes] = links
                number_of_nodes =number_of_nodes+1
                print(links)
    
    return d

    
    

grid = [[True, True, True, True, True, False],
        [False, False, True, True, True, False],
        [True, True, True, False, True, True],
        [True, False, False, True, True, False],
        [True, True, True, True, False, True],
        [True, False, True, True, True, False]]

print(matrix2dict(grid))

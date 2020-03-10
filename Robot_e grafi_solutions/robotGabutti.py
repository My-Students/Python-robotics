def matrix2dict(matrix):
    number_of_nodes = 0
    for i in range(0,len(matrix)):
        for e in range(0,len(matrix)):
            if matrix[i][e]:
                matrix[i][e] = number_of_nodes
                number_of_nodes = number_of_nodes + 1

    print(matrix)

    d = {}
    offset = 1
    number_of_nodes= 0
    links =[]

    for i in range(0,len(matrix)):
        links.clear()
        for e in range(0,len(matrix)):
            #print(f" i = {i} e = {e} len = {len(matrix)}")
            if matrix[i][e]!= False or matrix[i][e]==0:
                #print(f"[{i}][{e}] libero")
                if i-offset >= 0:
                    if(matrix[i-offset][e]!=False or matrix[i][e]==0):
                        links.append(matrix[i-offset][e])

                if e-offset >= 0:
                    if(matrix[i][e-offset]!=False or matrix[i][e]==0):
                        links.append(matrix[i][e-offset])

                if e+offset < len(matrix)-2:
                    if(matrix[i][e+offset]!=False or matrix[i][e]==0):
                        links.append(matrix[i][e+offset])

                if i+offset < len(matrix)-2:
                    if(matrix[i+offset][e]!=False or matrix[i][e]==0):
                        links.append(matrix[i+offset][e])

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

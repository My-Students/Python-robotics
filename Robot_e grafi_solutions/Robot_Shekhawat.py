#Shekhawat Karni 
#03/04/2020
def matrixBorn():  #Creo matrice inizializzata a -1
    l = int(input("What's the lenth of the matrix ? \n"))

    matrix = []

    for i in range(0, l):
       line = []

        for j in range(0, l):
            line.append(-1)
      
       matrix.append(line) 
    
    return matrix

def fillTabel(m): #Faccio caricare la matrice liberando blocchi indiati dei nodi 

    nNodes = int(input("Insert the numeber of nodes  : \n"))

    for i in range(0, nNodes):
        cordx = int(input(f"Insert the x cordinates of the {i}  node : \n"))
        cordy = int(input(f"Insert the y cordinates of the {i}  node : \n"))

        m[cordx][cordy] = i #False
    
    return m



def trovoVicini(m):
    vicini = []
    for i in range(len(m)):
        for k in range(len(m)):
            near = []
            if(m[i][k] > 0 ):
                if(m[i][k-1] > 0):
                    near.append(m[i][k-1])
                if(m[i][k+1] > 0 ):
                    near.append[m[i][k+1]]
                if(m[i+1][k] > 0):
                    near.append(m[i+1][k])
                if(m[i-1][k] > 0):
                    near.append(m[i-1][k])
            
            vicini.append(near)
    
    return vicini
    

            
            
                    
            
        


if __name__ == "__main__":
    matrix=matrixBorn()
    print(trovoVicini(fillTabel(matrix)))
    


"""
grid = [[True, True, True, True, True, False],
        [False, False, True, True, True, False],
        [True, True, True, False, True, True],
        [True, False, False, True, True, False],
        [True, True, True, True, False, True],
        [True, False, True, True, True, False]]

        """



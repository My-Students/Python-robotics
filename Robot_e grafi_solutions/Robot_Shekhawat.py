#Shekhawat Karni 
#03/04/2020
def matrixBorn():  #Creo matrice boolena inizializzata a True
    l = int(input("What's the lenth of the matrix ? \n"))

    matrix = []

    for i in range(0, len(l)):
        line = []
        for j in range(0, len(v)):
            line.append(True)
      
       matrix.append(line) 
    
    return matrix

def fillTabel(m): #Faccio caricare la matrice liberando blocchi indiati dei nodi 

    nNodes = int(input("Insert the numeber of nodes  : \n"))

    for i in range(0, nNodes):
        cordx = int(input(f"Insert the x cordinates of the {i}  node : \n"))
        cordy = int(input(f"Insert the y cordinates of the {i}  node : \n"))

        m[cordx][cordy] = False
    
    return m

"""
def contVicini(m):
    d = {}
    cont = 0
    for i in range(len(m)):
        for k in range(len(m)):
            
            if(m[i][k] == False & m[i][k+1] == False| m[i+1][k] == False):
                d{cont} = 


"""

if __name__ == "__main__":
    matrix=matrixBorn()
    fillTabel(matrix)

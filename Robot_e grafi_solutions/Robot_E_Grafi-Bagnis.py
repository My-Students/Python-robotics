"""
Robot e Grafi completo
"""

def DizionarioDaMatrice(matrice):

    #funzione che numera le caselle esistenti della matrice a partire da 1
    n_nodi = 1
    for r in range(0,len(matrice)):
        for c in range(0,len(matrice)):
            if matrice[r][c]:
                matrice[r][c] = n_nodi
                n_nodi = n_nodi + 1

    d = {}
    n_nodi = 1
    ponti =[]

    for r in range(0,len(matrice)):
        for c in range(0,len(matrice)):
            ponti= []
            if matrice[r][c]!= False:
                if r-1 >= 0:
                    if(matrice[r-1][c]!=False):
                        ponti.append(matrice[r-1][c])
                if c-1 >= 0:
                    if(matrice[r][c-1]!=False):
                        ponti.append(matrice[r][c-1])
                if c+1 < len(matrice):
                    if(matrice[r][c+1]!=False):
                        ponti.append(matrice[r][c+1])
                if r+1 < len(matrice):
                    if(matrice[r+1][c]!=False):
                        ponti.append(matrice[r+1][c])

                d[n_nodi] = ponti
                n_nodi =n_nodi+1
                print(ponti)
    
    return d

def main():
    scacchiera = []
    dim = int(input("Inserisci la dimensione della scacchiera: "))
    for i in range(0, dim):
        riga = []
        for j in range(0, dim):
            riga.append(1)
        scacchiera.append(riga)
    ancora = 1
    while ancora != 0:
        ostacolo = input("Inserisci le cordinate della cella con ostacolo (x.y) ")
        cordinate = ostacolo.split(".")
        scacchiera[int(cordinate[0])][int(cordinate[1])] = 0
        ancora= int(input("c'è n'è ancora? (0 per terminare)"))
    
    scacchiera_bool=[]
    for n,r in enumerate(scacchiera):
        riga=[]
        for c,_ in enumerate(r):
            if scacchiera[n][c]==1:
                riga.append(True)
            else:
                riga.append(False)
        scacchiera_bool.append(riga)
    
    print(DizionarioDaMatrice(scacchiera_bool))
    

if __name__ == "__main__":
    main()
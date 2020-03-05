"""
Robot e grafi
"""
def main():
    scacchiera = []
    dimMatrice = 0
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
        dimMatrice = dimMatrice + 1
        ancora= int(input("c'è n'è ancora? (0 per terminare)"))
    
    scacchiera_bool=[]
    for n,r in enumerate(scacchiera):
        riga=[]
        for c,_ in enumerate(r):
            if scacchiera[n][c]==1:
                riga.append("True")
            else:
                riga.append("False")
        scacchiera_bool.append(riga)
    
    for r in scacchiera_bool:
        print(r)

if __name__ == "__main__":
    main()
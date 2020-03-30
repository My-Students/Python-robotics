def main():
    piastrelle = dimPavimento()
    mat = formazionePavimento(piastrelle)
    dict = costruiscoMatrice(piastrelle, mat)

def dimPavimento():
    nodo = int(input("inserisci la dimensione del pavimento"))
    return nodo


def formazionePavimento(piastrelle):
    mat = []
    for a in range(0, piastrelle):
        riga=[]
        for b in range(0, piastrelle):
            num = int(input(f"inserisci se la cella {a} {b} è libera o occupata :\n 0 --> cella libera \n 1 --> cella occupata \n "))
            if num == 0:
                riga.append(True)
            else:
                riga.append(False)
        mat.append(riga)
    creaNodi(mat)
    print(mat)
    return mat

def creaNodi(pav):
    nNodi = 1
    for r in range(0, len(pav)):
        for c in range(0, len(pav)):
            if pav[r][c]:
                pav[r][c] = nNodi
                nNodi += 1




def costruiscoMatrice (piastrelle , matBool):
    dict = {}
    numNodi = 1
    offset=1
    for a in range(0, piastrelle):
        for b in range(0, piastrelle):
            collegamenti = []
            if matBool[a][b] != False :
                if a-offset >= 0:
                    if matBool[a-offset][b] != False:
                        collegamenti.append(matBool[a-1][b])
                if b-offset >= 0:
                    if matBool[a][b-offset]!=False:
                        collegamenti.append(matBool[a][b-1])
                if a+offset < len(matBool) :
                    if matBool[a+offset][b] != False:
                        collegamenti.append(matBool[a+1][b])
                if b+offset < len(matBool) :
                    if matBool[a][b+offset]!=False:
                        collegamenti.append(matBool[a][b+1])
            dict[numNodi] = collegamenti
            numNodi += 1
    print(dict)
    return dict

if __name__ == '__main__':
    main()

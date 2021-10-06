matrice = [[1,2,3,4,5],
           [1,2,3,4,5],
           [1,2,3,4,5],
           [1,2,3,4,5],
           [1,2,3,4,5]]
for linie in matrice:
    print(linie)
for rand in range(len(matrice)):
    print(f'Suma elementelor din randul {rand + 1} este {sum(matrice[rand])}')
suma = [sum(x) for x in zip(*matrice)]
diag_prin = []
diag_sec = []
for i in range(len(matrice)):
    print(f'Suma elementelor din coloana {i + 1} este {suma[i]}')
    for j in range(len(matrice[0])):
        if i == j:
            diag_prin.append(matrice[i][j])
        if i + j == len(matrice) - 1:
            diag_sec.append(matrice[i][j])
print(f'Diagonala principala {diag_prin}')
print(f'Diagonala secundara {diag_sec}')
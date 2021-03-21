M2 = [[-1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
a = []
for i in range(len(M2)):
    for j in range(len(M2[i])):
         if i == j:
            a.append(M2[i][j])
ab = {
    'sd':23
}
print(ab['sd'],'test')
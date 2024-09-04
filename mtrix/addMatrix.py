#  matrix addtion


def matrix_addtion(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    res = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(mat1[i][j] + mat2[i][j])
        res.append(row)
    return res


mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_addtion(mat1, mat2))

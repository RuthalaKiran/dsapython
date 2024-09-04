# rotate the matrix by 90 deg


# brute force
def rotate_mat_brute(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    newmat = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            newmat[j][cols - 1 - i] = matrix[i][j]
    return newmat


# tc - O(n^2)
# sc - O(n^2)



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_mat_brute(matrix))

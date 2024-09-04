# print the matrix elements in  spiral order


def spiral_order(matrix):
    n = len(matrix)
    m = len(matrix[0])
    left, right = 0, m - 1
    top, bottom = 0, n - 1
    res = []

    while left <= right and top <= bottom:

        #  right => left --> right with top as constant
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        #  bottom => top --> bottom with right as constant
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        #  left => right --> left with bottom as constant
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        # top => bottom --> top with left as constant
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiral_order(matrix))

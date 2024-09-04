rows = int(input("enter no. of rows : "))
cols = int(input("enter no. of cols : "))

matrix = []
print("enter the elements : ")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"enter element [{i}][{j}] :"))
        row.append(value)
    matrix.append(row)

for row in matrix:
    print(" ".join(map(str, row)))


# join only takes the iterable strings
arr = [1, 2, 3]
print("A".join(map(str, arr)))


# print the matrix with all elements zero
rows = 3
cols = 3
mat = [[0 for _ in range(cols)] for _ in range(rows)]
print(mat)

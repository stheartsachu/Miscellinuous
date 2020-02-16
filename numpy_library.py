import numpy
n = int(input())
matrix = []
for i in range(n):
    matrix.append(input().split())
n_l = []
for i in range(n):
    n_l.append([])

for i in range(len(matrix)):
    for j in matrix[i] :
        n_l[i].append(float(j))
value = numpy.linalg.det(n_l)
print ("{:.2f}".format(value))

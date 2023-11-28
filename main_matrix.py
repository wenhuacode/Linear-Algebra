from playLA.Matrix import Matrix
from playLA.Vector import Vector


if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print(matrix.shape())
    print(matrix.col_num())
    print(matrix.row_num())
    print(matrix.size())
    print(len(matrix))
    print(matrix[1, 0])

    matrix2 = Matrix([[5, 6], [7, 8]])

    print("add: {}".format(matrix + matrix2))
    print("sub: {}".format(matrix - matrix2))
    print("scalar-mul: {}".format(matrix * 2))
    print("scalar-mul: {}".format(2 * matrix))

    print(matrix.zero(22, 1))

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print("T.dot(p) = {}".format(T.dot(p)))

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print("T.dot(P) = {}".format(T.dot(P)))
    print(P.T())

    I = Matrix.identity(2)
    print(I)
    print("A.dot(T) = {}".format(matrix.dot(I)))
    print("I.dot(A) = {}".format(I.dot(matrix)))

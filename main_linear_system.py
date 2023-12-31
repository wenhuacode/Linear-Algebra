from playLA.Matrix import Matrix
from playLA.Vector import Vector
from playLA.LinearSystem import LinearSystem, inv, rank

if __name__ == "__main__":
    # A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    # b = Vector([7, -11, 1])
    # ls = LinearSystem(A, b)
    # ls.gauss_jordan_elimination()
    # ls.fancy_print()
    # print()

    A7 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]])
    b7 = Vector([1, 5, 13, -1])
    ls7 = LinearSystem(A7, b7)
    ls7.gauss_jordan_elimination()
    ls7.fancy_print()
    print()

    A8 = Matrix([[2, 2],
                 [2, 1],
                 [1, 2]])
    b8 = Vector([3, 2.5, 7])
    ls8 = LinearSystem(A8, b8)
    if not ls8.gauss_jordan_elimination():
        print("No Solution!")
    ls8.fancy_print()
    print()

    A = Matrix([[1, 2], [3, 4]])
    invA = inv(A)
    print(invA)
    print(A.dot(invA))
    print(invA.dot(A))
    print()

    print(rank(A8))
    print(rank(A7))

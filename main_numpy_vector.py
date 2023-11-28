import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    vec = np.array([1, 2, 3])
    print(vec)

    # np.array的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 666))

    # np.array的基本属性
    print(vec)
    print("size=", vec.size)
    print("size=", len(vec))
    print(vec[0])
    print(vec[-1])
    print(type(vec[0: 2]))

    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec))
    print("{} * {} = {}".format(vec, 2, vec * 2))
    print("{} * {} = {}".format(vec, vec2, vec * vec2))  # 不准确
    print("{}.doc({}) = {}".format(vec, vec2, vec.dot(vec2)))  # 点乘

    print(np.linalg.norm(vec))  # 取模
    print(vec / np.linalg.norm(vec))  # 单位向量
    print(np.linalg.norm(vec / np.linalg.norm(vec)))

    zero3 = np.zeros(3)
    zero3 / np.linalg.norm(zero3)
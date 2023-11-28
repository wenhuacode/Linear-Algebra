from playLA.Vector import Vector

if __name__ == "__main__":
    vec = Vector([5, 2])

    print(vec[0])

    vec2 = Vector([2, 5])

    zero2 = Vector([0, 0])

    print(vec.norm())
    print(vec.normalize())

    vec3 = Vector([0, 0])
    print(vec2 == vec3)
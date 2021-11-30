import numpy as np

def main():
    F = np.array([1, 0, 1, 1])
    print("F:", F)

    T = np.vstack((np.hstack((np.zeros((len(F)-1, 1)), np.identity(len(F)-1))),
                   F))
    print("T:\n", T)

    X = [T[:, 0]]
    while True:
        tmp = T.dot(X[-1]) % 2

        if np.array_equal(tmp, X[0]):
            stop = True
            break

        X.append(tmp)

    print("X:")
    for i in range(len(X)):
        print("\tx{} = {}".format(i, X[i].dot(2**np.arange(X[i].size)[::-1])))

    A = np.vstack(X).T
    print("A:\n", A)

if __name__ == "__main__":
    main()
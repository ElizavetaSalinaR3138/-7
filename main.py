import time
import random
import numpy as np

range1 = 1000000
count = 1000000


def generateArray():
    array = []
    for i in range(count):
        array.append(random.randint(-range1, range1))
    return array


if __name__ == '__main__':
    np1 = np.random.randint(-range1, range1, count)
    np2 = np.random.randint(-range1, range1, count)

    startTime = time.perf_counter()
    npResult = np.multiply(np1, np2)
    npTime = time.perf_counter() - startTime
    print(npTime)

    array1 = generateArray()
    array2 = generateArray()
    array = []

    startTime = time.perf_counter()
    for i in range(len(array1)):
        array.append(array1[i] * array2[i])
    arrayTime = time.perf_counter() - startTime
    print(arrayTime)

    print(arrayTime / npTime)

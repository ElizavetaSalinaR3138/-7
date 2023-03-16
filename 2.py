import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    table = np.genfromtxt('data1.csv', delimiter=';')

    array1 = table[1:, 0]
    array4 = table[1:, 3]
    array5 = table[1:, 4]

    correlation = np.subtract(array5, array4)

    plt.plot(array1, array4, "pink")
    plt.plot(array1, array5, 'red')
    plt.plot(array1, correlation, 'black')

    plt.xlabel('Время')
    plt.ylabel('Положение дроссельной заслонки (%)\nОбороты двигателя (об/мин)')

    plt.show()

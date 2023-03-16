import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(-np.pi, np.pi, 100)
    y = x
    z = np.tan(x)

    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='blue')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()

import matplotlib.pyplot as plot
import numpy as np
import sys

radius = 8
eps = 0.000001
x0 = np.array([-10, -10])
way = list()


def object_function(xk):
    return 10 * xk[0] ** 2 + xk[1] ** 2


def gradient_function(xk):
    return np.array([20 * xk[0], 2 * xk[1]])


def arg_min(xk, sk):
    alpha = 1.0
    a = 0.0
    b = -sys.maxsize
    c_1 = 0.1
    c_2 = 0.5
    k = 0
    while k < 100:
        k += 1
        if object_function(xk) - object_function(xk + alpha * sk) >= -c_1 * alpha * np.dot(gradient_function(xk), sk):
            if np.dot(gradient_function(xk + alpha * sk), sk) >= c_2 * np.dot(gradient_function(xk), sk):
                return alpha
            else:
                a = alpha
                alpha = arg_min(2 * alpha, (alpha + b) / 2)

        else:
            b = alpha
            alpha = 0.5 * (alpha + a)
    return alpha


def conjugate_gradient(x0, eps):
    xk = x0
    gk = gradient_function(xk)
    point = [xk[0], xk[1], object_function(xk)]
    way.append(point)

    sigma = np.linalg.norm(gk)
    sk = -gk
    step = 0

    while sigma > eps and step < 1000:

        step += 1
        alpha = arg_min(xk, sk)
        xk = xk + alpha * sk
        g0 = gk
        gk = gradient_function(xk)

        point = [xk[0], xk[1], object_function(xk)]
        way.append(point)

        miu = (np.linalg.norm(gk) / np.linalg.norm(g0)) ** 2
        sk = -1 * gk + miu * sk
        sigma = np.linalg.norm(gk)
        print(' {} итерация, результат {}, значение функции {}'.format(step, np.array(xk), object_function(xk)))
    return xk


def get_grid(grid_step):
    samples = np.arange(-radius, radius, grid_step)
    x, y = np.meshgrid(samples, samples)
    xk = [x, y]
    return x, y, object_function(xk)


def draw_chart(point, grid):
    point_x, point_y, point_z = point
    grid_x, grid_y, grid_z = grid
    plot.rcParams.update({
        'figure.figsize': (4, 4),
        'figure.dpi': 250,
        'xtick.labelsize': 4,
        'ytick.labelsize': 4
    })

    ax = plot.figure().add_subplot(111, projection='3d')
    for way_point in way:
        way_point_x, way_point_y, way_point_z = way_point
        ax.scatter(way_point_x, way_point_y, way_point_z, color='red')
    ax.scatter(point_x, point_y, point_z, color='red')
    ax.plot_surface(grid_x, grid_y, grid_z, rstride=5, cstride=5, alpha=0.7)
    plot.show()


if __name__ == '__main__':

    xk = conjugate_gradient(x0, eps)
    print(xk)
    minimum = [xk[0], xk[1], object_function(xk)]
    draw_chart(minimum, get_grid(0.05))

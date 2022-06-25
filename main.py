import numpy as np
import matplotlib.pyplot as plot


radius = 8
global_epsilon = 0.000001
step = 0.01
way = list()


def differentiable_function(x, y):
    return 10 * x ** 2 + y ** 2


def derivative_x(epsilon):
    return 20*epsilon


def derivative_y(epsilon):
    return 2*epsilon


def gradient_descent(best_estimates):

    best_x, best_y = best_estimates
    descent_step = step
    point = [best_x, best_y, differentiable_function(best_x, best_y)]
    way.append(point)
    old_z = differentiable_function(best_x, best_y)
    best_y = best_y - descent_step * derivative_y(best_y)

    best_x = best_x - descent_step * derivative_x(best_x)

    z = differentiable_function(best_x, best_y)
    point = [best_x, best_y, z]
    way.append(point)

    while abs(z - old_z) > global_epsilon:
        old_z = differentiable_function(best_x, best_y)
        best_y = best_y - descent_step * derivative_y(best_y)

        best_x = best_x - descent_step * derivative_x(best_x)

        z = differentiable_function(best_x, best_y)
        point = [best_x, best_y, z]
        way.append(point)

    return best_y, best_x


def find_minimum():
    points = [-1.0, -1.0]
    return gradient_descent(points)


def get_grid(grid_step):
    samples = np.arange(-radius, radius, grid_step)
    x, y = np.meshgrid(samples, samples)
    return x, y, differentiable_function(x, y)


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
    min_x, min_y = find_minimum()
    minimum = (min_x, min_y, differentiable_function(min_x, min_y))
    print(minimum)
    print(len(way))
    draw_chart(minimum, get_grid(0.05))

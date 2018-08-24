import numpy as np
from scipy import optimize

def rosenbrock(x):
    """
    This function is to return a Rosenbrock function when n = 3
    x: a list representing the variable of the function
    return: value of function
    """
    return 100 * (x[2] - x[1] ** 2) ** 2 + (1 - x[1]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2

def gradient(x):
    """
    This function is to calculate the gradient of rosenbrock(x) when n = 3
    x: a list representing the variable of the function rosenbrock(x)
    return: the gradient vector
    """
    return np.array([-400 * x[0] * (x[1] - x[0] ** 2) - 2 * x[0],
                     -400 * x[1] * (x[2] - x[1] ** 2) - 2 * x[1] + 200 * (x[1] - x[0] ** 2),
                     200 * (x[2] - x[1] ** 2)])

if __name__ == "__main__":
    x0_1 = [100, 200, 300]
    x0_2 = [10, 20, 30]
    x0_3 = [-1, 0, 1]

    opt = []
    opt.append(optimize.minimize(rosenbrock, x0_1, method = 'BFGS', jac = gradient).fun)
    opt.append(optimize.minimize(rosenbrock, x0_2, method = 'BFGS', jac = gradient).fun)
    opt.append(optimize.minimize(rosenbrock, x0_3, method = 'BFGS', jac = gradient).fun)

    print(min(opt))

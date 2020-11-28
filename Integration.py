import matplotlib.pyplot as plt
from collections import deque
from math import cos


def plot_function(function, t_0=0.0, x_0=1.0, min_t=-2.0, max_t=2.0, d_t=0.01, label=""):
    t = deque([t_0])
    x = deque([x_0])
    while t[0] >= min_t:
        x.appendleft(x[0] - function(x[0], t[0]) * d_t)
        t.appendleft(t[0] - d_t)
    while t[-1] <= max_t:
        x.append(x[-1] + function(x[-1], t[-1]) * d_t)
        t.append(t[-1] + d_t)
    plt.plot(t, x, label=label)
    plt.ylabel('x')
    plt.xlabel('t')
    plt.legend()
    plt.show()


def log_der(x, t):
    return 1/t


def sqrt_der(x, t):
    return 1/(2*x)


def sin_der(x, t):
    return cos(t)


def sigmoid_der(x, t):
    return x * (1 - x)


delta_t = 0.01

# log_der = 1/t
plot_function(log_der,
              t_0=1, x_0=0,
              min_t=0, max_t=10,
              d_t=delta_t,
              label="log_der = 1/t")

# sqrt_der = 1/(2x)
plot_function(sqrt_der,
              t_0=1, x_0=1,
              min_t=0, max_t=100,
              d_t=delta_t,
              label="sqrt_der = 1/(2x)")

# sin_der = cos(t)
plot_function(sin_der,
              t_0=0, x_0=0,
              min_t=-10, max_t=10,
              d_t=delta_t,
              label="sin_der = cos(t)")

# sigmoid_der = x * (1 - x)
plot_function(sigmoid_der,
              t_0=0, x_0=0.5,
              min_t=-10, max_t=10,
              d_t=delta_t,
              label="sigmoid_der = x * (1 - x)")

import math

from sympy import Symbol, lambdify, symbols, sin, log, sqrt
import sympy as sp
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)


def function(x):
    y = 22 * x ** 5 + 121 * x ** 4 + 4 * (1 - 11) * x ** 3 + 22 * (1 - 11) * x ** 2 - 8 * x - 44
    return y


def function_diff(x):
    y_diff = 110 * x ** 4 + 484 * x ** 3 - 120 * x ** 2 - 440 * x - 8
    return y_diff


# METODA STYCZNYCH
def met_stycznych():
    e = 0.00001
    x1 = -5
    loops = 100000
    root_numbers = []
    while loops > 0:
        x1 += 0.0001
        xk1 = x1 - (function(x1) / function_diff(x1))
        abs_v = abs(function(xk1))
        if abs_v < e:
            if root_numbers.__len__() != 0:
                root_already = False
                for root_number in root_numbers:
                    value = round(root_number, 2)
                    round_xk1 = round(xk1, 2)
                    if value == round_xk1:
                        root_already = True

                if not root_already:
                    root_numbers.append(round(xk1, 2))

            else:
                root_numbers.append(round(xk1, 2))
        loops -= 1

    for root_number in root_numbers:
        print(f"Root number: {root_number}")


# def bisection_method():
#     x = symbols('x')
#     # func = x ** 3 - 2 * x ** 2 + 7 * x - 9
#     # func = x ** 3 - 4 * x ** 2 + 1  # works!
#     func = x ** 3 - 2 * x ** 2 + 7 * x - 9  # works!
#     # func = 2 * sin(x) - log(x) # works!
#     # func = log(x) - sqrt(x)  # works!
#     f = lambdify(x, func)
#     a1 = -5
#     b1 = 10
#     x1 = (a1 + b1) / 2
#     e = 0.01
#     iterations = 1000
#     while abs(f(x1)) >= e and iterations != 0:
#         if f(x1) * f(a1) < 0:
#             b1 = x1
#         else:
#             a1 = x1
#
#         x1 = (a1 + b1) / 2
#         iterations = iterations - 1
#
#     if iterations != 0:
#         print(x1)


# METODA SIECZNYCH
def met_siecznych():
    x0 = -0.3
    x1 = 1.5
    x2 = 0

    e = 0.000000001

    iterations = 10000
    roots = []
    while iterations != 0:  # abs(f(x1)) > e:
        if function(x0) * function(x1) < 0:
            try:
                x2 = (function(x1) * x0 - function(x0) * x1) / (function(x1) - function(x0))
            except Exception as ex:
                # print(ex)
                pass
            if iterations == 1:
                pass
            x0 = x1
            x1 = x2

            if abs(function(x1)) < e and not roots.__contains__(round(x1, 2)):
                roots.append(round(x1, 2))
                x0 = x1 + 0.3

        else:
            x1 += 1
        iterations = iterations - 1
        # print(x1)
    for root in roots:
        print(f"Root number: {root}")


if __name__ == "__main__":
    # met_siecznych()
    met_stycznych()

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Point:
    def __init__(self, e1, e2, e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3


def function(x1, x2, x3):
    return (((1 - x1) ** 2) + 11 * (x2 - x1 ** 2) ** 2) + (1 - x2) ** 2 + 11 * (x3 - x2 ** 2) ** 2


epsilon = 0.000001
delta = 0.1
lower = 0.8

point0 = Point(0, 0, 0)
initial_point0 = point0
value_x0 = function(point0.e1, point0.e2, point0.e3)
initial_value = value_x0

point1 = Point(1, 0, 0)
point2 = Point(0, 1, 0)
point3 = Point(0, 0, 1)
point_base = point0

j = 1
# i = 1


def test(point_move):
    global value_x0, point0
    point_z1 = Point((point0.e1 + point_move.e1 * delta), (point0.e2 + point_move.e2 * delta),
                     (point0.e3 + point_move.e3 * delta))
    value_z1 = function(point_z1.e1, point_z1.e2, point_z1.e3)

    if value_z1 < value_x0:
        value_x0 = value_z1
        point0 = point_z1
        return True

    point_z1 = Point((point0.e1 - point_move.e1 * 2 * delta), (point0.e2 -
                                                               point_move.e2 * 2 * delta),
                     (point0.e3 - point_move.e3 * 2 * delta))
    value_z1 = function(point_z1.e1, point_z1.e2, point_z1.e3)

    if value_z1 < value_x0:
        value_x0 = value_z1
        point0 = point_z1
        return True

    return False


main_cond = True
while main_cond:

    condition = True
    while condition:
        test(point1)
        test(point2)
        test(point3)
        # global point_base
        point_base = point0
        print(f'Delta {delta}')
        print(f'Epsilon {epsilon}')
        if (value_x0 < initial_value):
            print("Był pomyślny krok")
            print(f"Punkt minimalny pomyślnego kroktu to {point_base.e1}, {point_base.e2}, {point_base.e3}")
            print(value_x0)
            condition = False
        else:
            print("Nie był pomyślny")
            print(initial_value)
            print(value_x0)

            if delta < epsilon:
                print(f"Punkt minimalny to {point_base.e1}, {point_base.e2}, {point_base.e3}")
                print(value_x0)
                condition = False
                main_cond = False
            else:
                if j == 1:
                    point0 = Point(10, 50, 10)
                    # break
                else:
                    # zmiana punktu startowego jezeli j = 1
                    delta = lower * delta
                j = j + 1

    print(f"Ostatni punkt Xb {point_base.e1}, {point_base.e2}. {point_base.e3}, wartość: {value_x0}")
    # value_x0 = function(point_base.e1, point_base.e2)
    j = j + 1
    print(f"Iteracje: {j}")
    point0 = Point((2 * point_base.e1 - initial_point0.e1), (2 * point_base.e2 - initial_point0.e2), (2 * point_base.e3 - initial_point0.e3))
    # value_x0 = function(point0.e1, point0.e2)
    initial_value = value_x0
    initial_point0 = point_base
    print(f"Punkt nowy Xj {point0.e1}, {point0.e2}, {point0.e3}")

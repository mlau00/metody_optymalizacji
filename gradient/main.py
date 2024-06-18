import math


class Point:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def show_point(self):
        return {
            "x1": self.x1,
            "x2": self.x2,
            "value": function(self)
        }


def function(point):
    z = (12 - point.x1) ** 2 + 2 * (point.x2 - point.x1 ** 2) ** 2
    return z


def deriv_x1(point):
    term1 = -2 * (12 - point.x1)
    term2 = -8 * point.x1 * (point.x2 - point.x1 ** 2)
    return term1 + term2


def deriv_x2(point):
    return 4 * (point.x2 - point.x1 ** 2)


def gradient_prosty():
    e = 0.0000001
    learning_rate = 0.1
    point_0 = Point(0, 0)
    # point_final = None
    print('Point x0:')
    print(point_0.show_point())

    condition = True
    while condition:
        point_next = Point(point_0.x1 - (learning_rate * deriv_x1(point_0)),
                           point_0.x2 - (learning_rate * deriv_x2(point_0)))

        w = math.sqrt(deriv_x1(point_next) ** 2 + deriv_x2(point_next) ** 2)
        print(w)
        if w < e:
            print('This is last result:')
            print(point_next.show_point())
            # point_final = point_next
            condition = False
        if function(point_next) >= function(point_0):
            learning_rate = learning_rate * 0.25

        point_0 = point_next


if __name__ == '__main__':
    gradient_prosty()

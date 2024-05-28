from math import sqrt


class Point:
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2


class Map:
    def __init__(self, point, value):
        self.point = point
        self.value = value


def function(point):
    return (2 - point.e1) ** 2 + 13 * (point.e2 - point.e1 ** 2) ** 2


# Simplex R2
point1 = Point(3, 3)
point2 = Point(2, 2)
point3 = Point(0, 0)
epsilon = 0.001

map_points = []
last_map_points = []

for point in [point1, point2, point3]:
    map_points.append(Map(point, function(point)))

map_points.sort(key=lambda x: x.value, reverse=False)


def print_points():
    sort_points()
    for point in map_points:
        print(point.point.e1, point.point.e2
              # , function(point.point)
              )


cond = True
i = 0
while cond:
    last_check = False


    def sort_points():
        for point in map_points:
            point.value = function(point.point)
        map_points.sort(key=lambda x: x.value, reverse=False)


    i = i + 1
    sort_points()
    # Centroid
    x1_centroid = 0
    x2_centroid = 0
    z = 0
    for point in map_points:
        x1_centroid += point.point.e1
        x2_centroid += point.point.e2
        z += 1
    x1_centroid = x1_centroid / z
    x2_centroid = x2_centroid / z

    point_centroid = Point(x1_centroid, x2_centroid)
    print(point_centroid.e1, point_centroid.e2)


    def move_to_end():
        global last_check
        # last_check = True
        if last_check is False:
            global cond
            last_check = True
            print(f'Iteration {i}')
            value = 0
            for point in map_points:
                value = value + (function(point.point) - function(point_centroid)) ** 2
            value = sqrt(value * (1 / len(map_points)))
            if value < epsilon:
                last_map_points = map_points
                cond = False
                print_points()
            # else:
            # sort_points()

            print(f"Value is: {value}")


    # Reflection
    biggest_point_value = map_points[len(map_points) - 1]

    point_reflection = Point((2 * point_centroid.e1 - biggest_point_value.point.e1),
                             (2 * point_centroid.e2 - biggest_point_value.point.e2))
    print(point_reflection.e1, point_reflection.e2)

    point_expansion: Point = Point(None, None)


    def find_expansion():
        global point_expansion
        point_expansion = Point((2 * point_reflection.e1 - point_centroid.e1),
                                (2 * point_reflection.e2 - point_centroid.e2))


    if function(point_reflection) < function(map_points[0].point):
        find_expansion()
        if function(point_expansion) < function(map_points[0].point):
            if last_check is False:
                map_points[len(map_points) - 1].point = point_expansion
                move_to_end()

        elif function(point_expansion) >= function(map_points[0].point):
            if last_check is False:
                map_points[len(map_points) - 1].point = point_reflection
                move_to_end()

    if function(map_points[0].point) <= function(point_reflection) <= function(
            map_points[len(map_points) - 2].point):
        if last_check is False:
            map_points[len(map_points) - 1].point = point_reflection
            move_to_end()

    point_contraction: Point = Point(None, None)


    def find_contraction():
        global point_contraction
        point_contraction = Point((point_centroid.e1 + map_points[len(map_points) - 1].point.e1) / 2,
                                  (point_centroid.e2 + map_points[len(map_points) - 1].point.e2) / 2)


    def reduction():
        for point in map_points:
            point.point.e1 = (point.point.e1 + map_points[0].point.e1) / 2
            point.point.e2 = (point.point.e2 + map_points[0].point.e2) / 2


    if function(point_reflection) > function(map_points[len(map_points) - 2].point) and function(
            point_reflection) < function(map_points[len(map_points) - 1].point):
        map_points[len(map_points) - 1].point = point_reflection
        find_contraction()

        if function(point_contraction) < function(map_points[len(map_points) - 1].point):
            if last_check is False:
                map_points[len(map_points) - 1].point = point_contraction
                move_to_end()
        elif function(point_contraction) >= function(map_points[len(map_points) - 1].point):
            if last_check is False:
                reduction()
                move_to_end()

    if function(point_reflection) >= function(map_points[len(map_points) - 1].point):
        find_contraction()
        if function(point_contraction) < function(map_points[len(map_points) - 1].point):
            if last_check is False:
                map_points[len(map_points) - 1].point = point_contraction
                move_to_end()
        elif function(point_contraction) >= function(map_points[len(map_points) - 1].point):
            if last_check is False:
                reduction()
                move_to_end()

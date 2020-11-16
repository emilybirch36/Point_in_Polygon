import os
import sys
from collections import OrderedDict
import plotter
import matplotlib.pyplot as plt


def main():
    # Call the read file function to get the x list by passing in index 1 and the y list by passing in index 2
    x_list = read_file(1, "/polygon.csv")
    y_list = read_file(2, "/polygon.csv")
    x_list_input = read_file(1, "/input.csv")
    y_list_input = read_file(2, "/input.csv")

    x_float = conv_float(x_list)
    y_float = conv_float(y_list)
    point = Point(x_float, y_float)
    polygon_init = Polygon(point)
    polygon_lines = polygon_init.lines()

    x_input_float = conv_float(x_list_input)
    y_input_float = conv_float(y_list_input)
    input_points = Point(x_input_float, y_input_float)
    ray_casting = RayCasting(input_points, point, polygon_lines)
    contains = ray_casting.contains()
    unclassified_list = ray_casting.unclassified_list()
    ray_casting = ray_casting.ray_casting()

    # Write classification results to a csv file
    id_list_input = read_file(0, "/input.csv")
    file_creation = write_file(id_list_input, contains)

    # Plot the figure showing the polygon outline and the
    # points that have been clasified and plotted
    plt.figure()
    plot_polygon = plotter.Plotter()
    plot_polygon.add_polygon(x_float, y_float)
    plot_polygon.add_point(x_input_float, y_input_float, ray_casting)
    plot_polygon.show()


def read_file(index, csv):
    # read in the absolute file path
    abs_path = os.path.dirname(os.path.abspath(__file__))
    file_path = abs_path + csv
    with open(file_path, 'r') as f:
        my_list = f.read().splitlines()
        coord_data = []
        for line in my_list[1:]:
            point = line.rstrip().split(",")[index]
            coord_data.append(point)
        return coord_data


def write_file(id, classification):
    with open("Output.csv", "w") as ffile:
        for i, j in zip(id, classification):
            ffile.write("{}, {}\n".format(i, j))
        ffile.close()


def conv_float(coord_list):
    float_list = []
    for i in coord_list:
        i = float(i)
        float_list.append(i)
    return float_list


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "Point(%s, %s)" % (self.__x, self.__y)

    # gain access to x and y private attributes
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Line(Point):

    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2

    def __str__(self):
        return "Line(%s, %s)" % (self.__point_1, self.__point_2)

    def get_point_1(self):
        return self.__point_1

    def get_point_2(self):
        return self.__point_2

    def slope(self):
        a = self.__point_1
        b = self.__point_2
        slope = (b.get_y() - a.get_y()) / (b.get_x90 - a.get_x())
        return slope


class Polygon(Point):
    # Constructing a polygon, a list is able to use data structure that supports sequences

    def __init__(self, points):
        self.__points = points

    # a list of points in clockwise order
    def get_points(self):
        return self.__points

    def __str__(self):
        return "Point(%s)" % (self.__points)

    # iterate across pairs of points to make lines which form the polygon
    # will loop around the points to generate a list of lines that are then returned by the method line
    def lines(self):
        res = []
        points = self.get_points()
        x_coord = self.__points.get_x()
        y_coord = self.__points.get_y()

        points = [str(x) + "," + str(y) for x, y in zip(x_coord, y_coord)]
        for i, p in enumerate(points):
            p1 = p
            p2 = points[(i + 1) % len(points)]
            res.append((p1, p2))
        return res


class RayCasting(Point):
    def __init__(self, points, polygon_points, lines):
        self.__points = points
        self.__polygon_points = polygon_points
        self.__lines = lines

    # a list of points in clockwise order
    def get_points(self):
        return self.__points

    def __str__(self):
        return "Point(%s)" % (self.__points)

    def pointOnVector(self, polygon_point_a_x, polygon_point_b_x, polygon_point_a_y, polygon_point_b_y,
                      list_of_points_to_check_x, list_of_points_to_check_y, eps, mbr_category, n_of_points_to_check):
        # This method takes two polygon points a and b
        # plots a vector and checks to see if list of coordinates lies on that vector
        for i in range(n_of_points_to_check):
            q = "on boundary"
            crossproduct = (list_of_points_to_check_y[i] - polygon_point_a_y) * (polygon_point_b_x - polygon_point_a_x)\
                           - (list_of_points_to_check_x[i] - polygon_point_a_x) * (polygon_point_b_y - polygon_point_a_y)
            dotproduct = (list_of_points_to_check_x[i] - polygon_point_a_x) * (polygon_point_b_x - polygon_point_a_x)\
                         + (list_of_points_to_check_y[i] - polygon_point_a_y) * (polygon_point_b_y - polygon_point_a_y)
            squaredlengthba = (polygon_point_b_x - polygon_point_a_x) * (polygon_point_b_x - polygon_point_a_x) + \
                              (polygon_point_b_y - polygon_point_a_y) * (polygon_point_b_y - polygon_point_a_y)
            if abs(crossproduct) > eps:
                q = "not on boundary"

            if dotproduct < 0:
                q = "not on boundary"

            if dotproduct > squaredlengthba:
                q = "not on boundary"

            if q == "on boundary":
                mbr_category[i] = "boundary"

    mbr_category = []

    def contains(self):
        _infinity = sys.float_info.max
        _eps = 0.00001
        lines = self.__lines

        category = Category(self.__polygon_points.get_x(), self.__polygon_points.get_y(), self.__points.get_x(),
                            self.__points.get_y())
        mbr_category = category.inside_mbr()

        for i in range(len(lines)-1):
            # In the loop, extract each line one by one
            line = lines[i]
            a = line[0]
            b = line[1]
            # X and Y coords of the first point
            a_y = float(a.split(",")[1])
            a_x = float(a.split(",")[0])
            # X and Y coords of the second point
            b_y = float(b.split(",")[1])
            b_x = float(b.split(",")[0])
            # Need to ensure point A (the first point) is set to the lowest point
            # if A is higher than B (greater Y value), swap labels on points (i.e. point A becomes point B)
            # This would therefore make point A lower than B.
            if a_y > b_y:
                a, b = b, a
            n_of_points = len(mbr_category)
            # Get x and y values for the point to check against polygon
            y = self.__points.get_y()
            x = self.__points.get_x()
            self.pointOnVector(a_x, b_x, a_y, b_y, x, y, _eps, mbr_category, n_of_points)
        return mbr_category

    def unclassified_list(self):
        mbr_category = self.contains()
        unclassified_list_indexes = []
        for i in range(len(mbr_category)):
            if mbr_category[i] == "inside":
                unclassified_list_indexes.append(i)
        return unclassified_list_indexes

    def ray_casting(self):
        mbr_category = self.contains()
        unclassified_list_indexes = self.unclassified_list()
        if unclassified_list_indexes is not None:
            _infinity = sys.float_info.max
            _eps = 0.00001
            lines = self.__lines

            inside = False
            for i in range(len(lines) - 1):
                # In the loop, extract each line one by one
                line = lines[i]
                # Take the first point of the extracted line
                a = line[0]
                # Take the second point of the extracted line
                b = line[1]
                # X and Y coords of the first point
                a_y = float(a.split(",")[1])
                a_x = float(a.split(",")[0])
                # X and Y coords of the second point
                b_y = float(b.split(",")[1])
                b_x = float(b.split(",")[0])
                # Need to ensure point A (the first point) is set to the lowest point
                # if A is higher than B (greater Y value), swap labels on points (i.e. point A becomes point B)
                # This would therefore make point A lower than B.
                if a_y > b_y:
                    a, b = b, a
                # Get x and y values for your point to check against polygon
                y = self.__points.get_y()
                x = self.__points.get_x()
                count = 0
                for j in unclassified_list_indexes:

                    # Make sure point is not at the same height as vertex
                    if y[j] == a_y or y[j] == b_y:
                        y[j] += _eps

                    # The horizontal ray does not intersect with the edge
                    if (y[j] > b_y or y[j] < a_y) or (x[j] >= max(a_x, b_x)):
                        continue

                    if x[j] < min(a_x, b_x):
                        inside = not inside
                        continue

                    try:
                        m_edge = (b_y - a_y) / (b_x - a_x)
                    except ZeroDivisionError:
                        m_edge = _infinity

                    try:
                        m_point = (y[i] - a_y) / (x[i] - a_x)
                    except ZeroDivisionError:
                        m_point = _infinity

                    # The ray intersects with the edge
                    if m_point >= float(m_edge):
                        inside = not inside
                        continue
                if inside == True:
                    count = count + 1
                    if count % 2:
                        mbr_category[j] = "outside"
                    mbr_category[j] = "outside"
            return mbr_category
        return mbr_category

class Mbr(Point):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.point = Point(x, y)

    def min(self, coord_list):
        coord_min = coord_list[0]
        for min in coord_list[1:]:
            if min < coord_min:
                coord_min = min
        return coord_min

    def max(self, coord_list):
        coord_max = coord_list[0]
        for max in coord_list[1:]:
            if max > coord_max:
                coord_max = max
        return coord_max


class Category(Mbr):
    def __init__(self, x, y, x_input, y_input):
        super().__init__(x_input, y_input)
        self.point = Point(x, y)
        self.mbr = Mbr(x, y)
        self.x_input = x_input
        self.y_input = y_input

    def inside_mbr(self):
        result = []
        x_min = float(self.mbr.min(self.point.get_x()))
        x_max = float(self.mbr.max(self.point.get_x()))
        y_min = float(self.mbr.min(self.point.get_y()))
        y_max = float(self.mbr.max(self.point.get_y()))
        for i in range(len(self.x_input)):
            if float(self.x_input[i]) > x_min and float(self.x_input[i]) < x_max and float(
                    self.y_input[i]) < y_max and float(self.y_input[i]) > y_min:
                result.append("inside")
            else:
                result.append("outside")
                # result.append(self.x_input[i] + "," + self.y_input[i])
        return result


if __name__ == "__main__":
    main()
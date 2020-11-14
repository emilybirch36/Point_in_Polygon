import os
import sys
from collections import OrderedDict
"""
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
"""

def main():
    # Call the read file function to get the x list by passing in index 1
    # Call the read file function to get the y list by passing in index 2
    # Giving it the index and then parsing in the file name
    x_list = read_file(1, "/polygon.csv")
    y_list = read_file(2, "/polygon.csv")

    point = Point(x_list, y_list)
    mbr = Mbr(x_list, y_list)

    x_list_input = read_file(1, "/input.csv")
    y_list_input = read_file(2, "/input.csv")

    print("inputcsv_x", x_list_input)
    print("inputcsv_y", y_list_input)

    cat = Category(x_list, y_list, x_list_input, y_list_input)
    cate = cat.inside_mbr(point)
    print("catee", cate)
    x_min = mbr.min(x_list)
    x_max = mbr.max(x_list)
    y_min = mbr.min(y_list)
    y_max = mbr.max(y_list)

    # Initialise class to use functions in class
    getx = point.get_x()
    print("GETTING X", getx)
    gety = point.get_y()
    print("GETTING Y", gety)
    polygon = Polygon(point)
    print("polygon", polygon)
    polygon_points = polygon.get_points()
    polygon_lines = polygon.lines()
    print("polygonpoints", polygon_points)
    print("polygonlines", polygon_lines)

    # Reading in input csv
    # Calling read file function
    x_list_input = read_file(1, "/input.csv")
    y_list_input = read_file(2, "/input.csv")

    print("inputcsv_x", x_list_input)
    print("inputcsv_y", y_list_input)

    # Call the MBR in the main and pass in the x and y lists
    # Minimum bounding rectangle
    # initialise
    point = Point(x_list, y_list)


 # to test the RCA algorithm

   # q = Polygon(Point(get_x, get_y))
   # categ = Category()
   # lis_ans = categ.categorise(.....)



  #  for i in inside_mbr_list?
    ##    contains
   # print "inside", "outside"




"""
     # Test 1: Point inside of polygon
    p1 = Point(75, 50);
    print
    "P1 inside polygon: " + str(q.contains(p1))

    # Test 2: Point outside of polygon
    p2 = Point(200, 50)
    print
    "P2 inside polygon: " + str(q.contains(p2))

    # Test 3: Point at same height as vertex
    p3 = Point(35, 90)
    print
    "P3 inside polygon: " + str(q.contains(p3))

    # Test 4: Point on bottom line of polygon
    p4 = Point(50, 10)
    print
    "P4 inside polygon: " + str(q.contains(p4))
"""

def read_file(index, csv):
    # read in the absolute file path
    abs_path = os.path.dirname(os.path.abspath(__file__))
    file_path = abs_path + csv
    with open(file_path, 'r') as f:
        my_list = f.read().splitlines()
        print(my_list)
        coord_data = []
        for line in my_list[1:]:
            point = line.rstrip().split(",")[index]
            coord_data.append(point)
        print(coord_data)
        return coord_data


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


class Line:

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
    """ Constructing a polygon, a list is able to use data structure that supports sequences """

    def __init__(self, points):
        self.__points = points

    # a list of points in clockwise order
    def get_points(self):
        return self.__points

    def __str__(self):
        return "Point(%s)" % (self.__points)

    # iterate across pairs of points to make lines which form the polygon, will loop around the points to generate a list of lines that are then returned by the method line
    def lines(self):
        res = []
        points = self.get_points()
        x_coord = self.__points.get_x()
        y_coord = self.__points.get_y()
        print("xcoordPOLY", x_coord)
        print("ycoord", y_coord)

        points = [x + "," + y for x, y in zip(x_coord, y_coord)]
        print("polygonpoints", points)
        point_a = points[0]
        print("POINT A ", point_a)
        for point_b in points[1:]:
            res.append(Line(point_a, point_b))
            point_a = point_b
            res.append(Line(point_a, points[0]))
            return res

    # _infinity represents infinity if we divide by 0
    # _eps is used to make sure points are not on the same line as vertexes
    def contains(self, point):
        _infinity = sys.float_info.max
        _eps = 0.00001

        # starting on outside of polygon
        # initialise boolean variable "inside" which will be toggled each time we find an edge the ray intersects
        # initialise inside to false so that the final value of "inside" will be true if P (point) is inside Q (polygon) and vice versa
        # Make sure A is the lower point of the edge
        inside = False
        for edge in self.lines():
            a = edge.get_point_1()
            b = edge.get_point_2()
            if a.get_y() > b.get_y():
                a, b = b, a

        # Make sure point is not at the same height as vertex
            if point.get_y() == a.get_y() or point.get_y() == b.get_y():
                point.y(_eps)

        # The horizontal ray does not intersect with the edge
            if (point.get_y() > b.get_y or point.get_y() < a.get_y() or point.get_x() > max(a.get_x(), a.get_x())):
                continue

        # the ray intersects the edge
            if point.get_x() <= min(a.get_x(), b.get_get_x()):
                inside = not inside
                continue

            try:
                m_edge = (b.get_y() - a.get_y()) / (b.get_x() - a.get_x())
            except ZeroDivisionError:
                m_edge = _infinity

            try:
                m_point = (point.get_y() - a.get_y()) / (point.get_x() - a.get_x())
            except ZeroDivisionError:
                m_point = _infinity

            # The ray intersects with the edge
            if m_point >= m_edge:
                inside = not inside
                continue

        return inside


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

    # just need to make it a point object then use the getters

    def inside_mbr(self, point):

        result = []
        x_min = float(self.mbr.min(self.point.get_x()))
        print("XMIN", x_min)

        x_max = float(self.mbr.max(self.point.get_x()))
        y_min = float(self.mbr.min(self.point.get_y()))
        y_max = float(self.mbr.max(self.point.get_y()))
        print("y_max", y_max)
        for i in range(len(self.x_input)):
            if float(self.x_input[i]) >= x_min and float(self.x_input[i]) <= x_max and float(
                    self.y_input[i]) <= y_max and float(self.y_input[i]) >= y_min:
                result.append(self.x_input[i] + "," + self.y_input[i])
        print("RESULT", result)
        return result


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == "outside":
            plt.plot(x, y, "ro", label='Outside')
        elif kind == "boundary":
            plt.plot(x, y, "bo", label='Boundary')
        elif kind == "inside":
            plt.plot(x, y, "go", label='Inside')
        else:
            plt.plot(x, y, "ko", label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()



if __name__ == "__main__":
    main()

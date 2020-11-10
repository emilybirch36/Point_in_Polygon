import os


def main():
    # call the read file function to get the x list by passing in index 1
    # call the read file function to get the y list by passing in index 2
    # giving it the index and then parsing in the file name
    x_list = read_file(1, "/polygon.csv")
    y_list = read_file(2, "/polygon.csv")
    point = Point(x_list, y_list)
    # initialise class to use functions in class
    getx = point.get_x()
    print("GETTING X", getx)
    polygon = Polygon(point)
    print("polygon", polygon)
    polygon_points = polygon.get_points()
    polygon_lines = polygon.lines()
    print("polygonpoints", polygon_points)
    print("polygonlines", polygon_lines)

    # reading in input csv
    # calling read file function
    x_list_input = read_file(1, "/input.csv")
    y_list_input = read_file(2, "/input.csv")
    print("inputcsv_x", x_list_input)
    print("inputcsv_y", y_list_input)

def read_file(index, csv):
    current_directory = os.getcwd()
    print("current directory", current_directory)
    csv = current_directory + csv
    print("csv", csv)
    with open(csv, 'r') as f:
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

    # gain access to x and y private attributes
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Line:

    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2

    def get_point_1(self):
        return self.__point_1

    def get_point_2(self):
        return self.__point_2

    def slope(self):
        a = self.__point_1
        b = self.__point_2
        slope = (b.get_y() - a.get_y()) / (b.get_x90 - a.get_x())
        return slope


class Polygon:
    """ Constructing a polygon, a list is able to use data structure that supports sequences """
    def __init__(self, points):
        self.__points = points

    # a list of points in clockwise order
    def get_points(self):
        return self.__points

    # iterate across pairs of points to make lines which form the polygon, will loop around the points to generate a list of lines that are then returned by the method line
    def lines(self):
        res = []
        points = self.get_points()
        print("pointspoly", points)
        x_point = self.__points.get_x()
        y_point = self.__points.get_y()
        print("xpoint", x_point)
        print("ypoint", y_point)

        point_a = points[0]
        for point_b in points[1:]:
            res.append(Line(point_a, point_b))
            point_a = point_b
            res.append(Line(point_a, points[0]))
            return res
"""
class Mbr(Points):
    def __init__(self):
        self.__points = Points()


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

    def area(self, x_list, y_list):
        x_min = self.min(x_list)
        x_max = self.max(x_list)
        y_min = self.min(y_list)
        y_max = self.max(y_list)
        res = ((x_max - x_min) * (y_min - y_max))
        return res
"""

if __name__ == "__main__":
    main()


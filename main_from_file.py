import os


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
    cate = cat.categorise(point)
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
        super().__init__(x, y)
        self.point = Point(x, y)
        self.mbr = Mbr(x, y)
        self.x_input = x_input
        self.y_input = y_input

    # just need to make it a point object then use the getters

    def categorise(self, point):

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
                result.append("inside_mbr")
            else:
                result.append("outside_mbr")
        print("RESULT", result)
        return result


if __name__ == "__main__":
    main()

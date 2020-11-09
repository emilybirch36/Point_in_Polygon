""" with open("csv, 'r' as f:
    my list = f.read().splitlines()
    print(mylist)
    x_data = []
    y_data = []
    for line in mylist:
    x = line.rstrip().split(",")[1]
    print("testingx", x)
    y = line.rstrip().split(",")[2]
    print("testingy", y)
    x_data.append(x)
    y_data.append(y)
    print(x_data)
    print(y_data)"""

def coordinate_reader(csv):
    with open(csv, 'r') as f:
        coordinates = []
        for line in f.readlines():
            format_line = line.rstrip().split(",")
            print("line", format_line)
            point = Point(float(format_line[1])),float(format_line[2])
            getx = point.get_x()
            print("x", getx)
            gety = point.get_y()
            print("y", gety)


class Geometry:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Point(Geometry):
    def __init__(self, name, x, y):
        # call super to construct the parent
        super().__init__(name)
        self.__x = x
        self.__y = y
    # gain access to x and y private attributes
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    """def set_x(self, value):
        self.__x += value
    
    def set_y(self, value):
        self.__y(self, value):"""


class Line(Geometry):
    """so to make the polygon, join the lines from p1-p2, p2-p3 etc. clockwise"""
    """making a polygon of 3+ numbers in order, therefore, create a list to use data structures that support sequences"""
    def __init__(self, name, point_1, point_2):
        super().__init__(name)
        self.__point_1 = point_1
        self.__point_2 = point_2

def get_point_1(self):
    return self.__point_1

def get_point_2(self):
    return self__point_2

"""def slope(self):
    a = self.__point_1
    b = self.__point_2
    slope = (b.get_y() - a.get_y())/ (b.get_x90 - a.get_x())
    return slope"""


class Polygon(Geometry):
    
    def __init__(self, name, points):
            super().__init__(name)
            self.__points = points
    
    def get_points(self):
        return self.__points
    # iterate across pairs of points to make lines which form the polygon, will loop around the points to generate a list of lines that are then returned by the method line
    def lines(self):
        res = []
        points = self.get_points()
        point_a = points[0]
        for point_b in points[1:]:
            res.append(Line(point_a.get_name() + '-' + point_b.get_name(), point_a, point_b))
            point_a = point_b
            res.append(Line(point_a.get_name() + '-' + points[0].get_name(), point_a, points[0]))
            return res


class Mbr(Polygon):

    def __init__(self, name):
        super().__init__(name)

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



class CategoryMbr(Mbr):
    
    



def main():
    import os
    import matplotlib

    test = coordinate_reader("/Users/emilybirch/Documents/UCL/Programming/point_in_polygon_test/polygon.csv")
    print(test)

    test = coordinate_reader(input.csv)



if __name__ == "__main__":
    main()










"""class MBR(Polygon):
    # initialise the class polygon, parse name and list of points
    def__init__(self, name, point_1, point_2)
        super().__init__(name, [point_1, point_2])
# defining rectangle by bottom left point, top right point, side 1 and side 2
# to get MBR coords- need to get min and max of coords list
    # area of rectangle is
    # be able to code formula for working our MBR here. do this in the method area
# construct polygon as its the parent,
    def area(self):
        res = 0
        ps = self.get_points()
        # MBR formula
        res = res + ps
        return res


# x_data and y_data is the list of each to find min and max from
    def min(vs):
        res = vs[0]
        for v in vs[1:]:
            if v < res:
                res = v
                return res

    def max(vs):
        res = vs[0]
        for v in vs[1:]:
            if v > res:
                res = v
                return res


class Categorisation(MBR)"""



# allow access to directory
# import csv file
# READ list of x y coordinates from csv file
# then put them into a list representing each value for each column
# then iterate with for loop, read directly the points/ values stored in this list

# define and initialise geometry parent class
# define point child class as x y
# define a line child class as two points

# create a polygon object from the coordinates- construct in clockwise order down list
# get the minimum and maximum x and y coordinate points of polygon
# calculate the minimum bounding rectangle for the polygon

# categorise points as "in" "out" or "boundary" - implementing Minimum bounding rectangle MBR
# if coordinate "out" of MBR, then it is definitely outside of polygon
# else if points are "in" or "boundary" of MBR, then implement RCA
# implement RCA (ray casting algorithm)
# categorise points again
# plot the polygon and point
# READ data from file into list
# fr each item in list (use for because we know how many times we need to iterate)
# split each item string and assign parts to


# Point in Polygon Test

import os

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
 # return coordinates


class Point():
    def __init__(self, x, y):
        # call super to construct the parent
        # super().__init__(name)
        self.__x = x
        self.__y = y
    # gain access to x and y private attributes
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y



def main():
    test = coordinate_reader("/Users/emilybirch/Documents/UCL/Programming/point_in_polygon_test/polygon.csv")
    print(test)


if __name__ == "__main__":
    main()


"""

class Geometry:

def __init__(self, name):
    self.__name = name

def get_name(self):
    return self.__name


class Line(Geometry):
# so to make the polygon, join the lines from p1-p2, p2-p3 etc. clockwise
# making a polygon of 3+ numbers in order, therefore, create a list to use data structures that support sequences
def __init__(self, name, point_1, point_2):
    super().__init__(name)
    self.__point_1 = point_1
    self.__point_2 = point_2


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


class MBR(Polygon):
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




class Categorisation(MBR)

"""



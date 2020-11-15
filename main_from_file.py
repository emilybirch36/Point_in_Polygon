import os
import sys
import plotter




def main():
    # Call the read file function to get the x list by passing in index 1
    # Call the read file function to get the y list by passing in index 2
    # Giving it the index and then parsing in the file name
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
    print("contains", contains)

    # Write classification results to a csv file
    id_list_input = read_file(0, "/input.csv")
    file_creation = write_file(id_list_input, contains)

    # Plot the figure showing the polygon outline and the
    # points that have been clasified and plotted
    plot_polygon = plotter.Plotter()
    plot_polygon.add_polygon(x_float, y_float)
    plot_polygon.add_point(x_input_float, y_input_float, contains)
    plot_polygon.show()


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


def write_file(id, classification):
    with open("classification.csv", "w") as ffile:
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
        print("GET POINT", points)
        x_coord = self.__points.get_x()
        y_coord = self.__points.get_y()
        print("xcoordPOLY", x_coord)
        print("ycoord", y_coord)

        points = [str(x) + "," + str(y) for x, y in zip(x_coord, y_coord)]
        print("polygonpoints", points)
        for i, p in enumerate(points):
            p1 = p
            print("P1", p1)
            p2 = points[(i + 1) % len(points)]
            print("p2", p2)
            res.append((p1, p2))
        print("RES", res)
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

    # _infinity represents infinity if we divide by 0
    # _eps is used to make sure points are not on the same line as vertexes
    def vertex(self):
        vertex_list = []
        x_list = self.__polygon_points.get_x()
        print("xlist", x_list)
        for pol_point in self.__polygon_points():
            if pol_point.get_x() == self.__points.get_x() and pol_point.get_y() == self.__points.get_y():
                vertex_list.append("True")
            else:
                vertex_list.append("False")
        return vertex_list

    def contains(self):
        _infinity = sys.float_info.max
        _eps = 0.00001

        # starting on outside of polygon
        # initialise boolean variable "inside" which will be toggled each time we find an edge the ray intersects
        # initialise inside to false so that the final value of "inside" will be true if P (point) is inside Q (polygon) and vice versa
        # Make sure A is the lower point of the edge
        lines = self.__lines
        # Intialise point classification list
        in_out_list = []
        # Populate the list with all points "inside" to begin with
        for i in range(len(self.__points.get_y())):
            in_out_list.append("inside")
        # Initialise a second list for storing the indexes of the "outside" points
        outside_indexes = []
        # Loop over each line that builds the polygon
        for i in range(len(lines)):
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

            # Start algorithm, create a temp list for storage within our "points" loop
            temp_list = []
            # For each polygon line (x20) Begin looping over points (x100)
            category = Category(self.__polygon_points.get_x(), self.__polygon_points.get_y(), self.__points.get_x(),
                                self.__points.get_y())
            mbr_category = category.inside_mbr()
            print("MBR CAT", mbr_category)
            for i in range(len(self.__points.get_y())):

                # Get x and y values for your point to check against polygon
                y = self.__points.get_y()
                x = self.__points.get_x()

                ## The algorithm given is for simple polygons, it doesn't work in this case.
                ## To determine if a point is inside a complicated polygon
                ## you need to 'ray cast' (or draw a line) in the x or y direction. if you intersect the polygon
                ## an odd amount of times, you're likely to be inside it, if not, outside.
                ## There are further complications when you are touching the edge of the polygon.

                ## You can also quickly determine your max/min X/Y of your polygon and do a set of rules:
                ## If your point's Y > polygon MaxY == outside
                ## If your point's Y < polygon MinY == outside
                ## If your point's X > polygon MaxX == outside
                ## If your point's X < polygon MinX == outside
                ## This would automatically give you a 'box' perimeter of your polygon - anything outside
                ## The box can be labelled "outside" automatically.

                if mbr_category[i] == "inside":

                    # Make sure point is not at the same height as vertex
                    if y[i] == a_y or y[i] == b_y:
                        y[i] += _eps

                    # The horizontal ray does not intersect with the edge
                    if (y[i] > b_y or y[i] < a_y) or (x[i] >= max(a_x, b_x)):
                        # If it doesn't point is good and is inside.
                        temp_list.append("inside")
                        continue

                    if x[i] < min(a_x, b_x):
                        # Point is outside, append to temporary storage
                        temp_list.append("outside")
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
                        # Point is outside, append to temporary storage
                        temp_list.append("outside")
                        continue
                    temp_list.append("inside")
                else:
                    temp_list.append("outside")
            return temp_list

        ## Code below is using algorithm given, you can see in the plot that it is incorrect though.
        '''
                    # Make sure point is not at the same height as vertex
                    if y[i] == a_y or y[i] == b_y:
                        y[i] += _eps

                    # The horizontal ray does not intersect with the edge
                    if (y[i] > b_y or y[i] < a_y or x[i] > max(a_x, b_x)):
                        # If it doesn't point is good and is inside.
                        temp_list.append("inside")
                        continue


                # By this line, all 2000 iterations will be done. Tab backwards out of loop
                # Create a "Final ordered list" of the 'indexes' of the "outside" points. 
                # ('set' removes duplicates from a list, 'list' then re-converts back into a list)
                final_outside_indexes = list(set(outside_indexes))
                #print("getting outsides index", final_outside_indexes) 

                # Earlier, the 'in_out_list' was populated completely with "inside" - we will now replace "inside"
                # with "outside" at the indexes specified by "outside_indexes"
        for i in range (len(final_outside_indexes)):
            in_out_list[final_outside_indexes[i]] = "outside"
            print("I", i)

            #if inside == True:
            #    in_out_list.append("inside")
            #elif inside == False:
            #    in_out_list.append("outside")

        #print("IN OUT LIST", in_out_list)
        return in_out_list
        '''


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
        print("XMIN", x_min)

        x_max = float(self.mbr.max(self.point.get_x()))
        y_min = float(self.mbr.min(self.point.get_y()))
        y_max = float(self.mbr.max(self.point.get_y()))
        print("y_max", y_max)
        for i in range(len(self.x_input)):
            if float(self.x_input[i]) >= x_min and float(self.x_input[i]) <= x_max and float(
                    self.y_input[i]) <= y_max and float(self.y_input[i]) >= y_min:
                result.append("inside")
            else:
                result.append("outside")
                # result.append(self.x_input[i] + "," + self.y_input[i])
        print("RESULT", result)
        return result


if __name__ == "__main__":
    main()
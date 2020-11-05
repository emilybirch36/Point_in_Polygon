# import csv file
# read the list of x y coordinates
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
print(os.getcwd())



def main():

     # READ list of x y coordinates from csv file

    with open("/Users/emilybirch/Documents/UCL/Programming/point_in_polygon_test/polygon.csv") as f:
        formatting_line = f.read().splitlines()
        print(formatting_line)
        x_data = []
        y_data = []
        for line in formatting_line:
            print(line)
            x = line.split(",")[1]
            print("testingx",x)
            y = line.split(",")[2]
            print("testingy", x)
            x_data.append(x)
            y_data.append(y)
            print(x_data)
            print(y_data)


if __name__ == "__main__":
    main()

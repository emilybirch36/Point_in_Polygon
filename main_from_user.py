import plotter
import main_from_file as usermain
from main_from_file import Point, Polygon, RayCasting


def main():
    x_value = user_input("X coordinate")
    y_value = user_input("Y coordinate")

    # Call the read file function to get the x list by passing in index 1 and the y list by passing in index 2
    x_list = usermain.read_file(1, "/polygon.csv")
    y_list = usermain.read_file(2, "/polygon.csv")

    x_float = usermain.conv_float(x_list)
    y_float = usermain.conv_float(y_list)
    point = Point(x_float, y_float)
    polygon_init = Polygon(point)
    polygon_lines = polygon_init.lines()

    x_input_float = usermain.conv_float(x_value)
    y_input_float = usermain.conv_float(y_value)
    input_points = Point(x_input_float, y_input_float)
    ray_casting = RayCasting(input_points, point, polygon_lines)
    contains = ray_casting.contains()
    unclassified_list = ray_casting.unclassified_list()
    ray_casting = ray_casting.ray_casting()
    print("your point is:", ray_casting)


    # Plot the figure showing the polygon outline and the classified points
    plot_polygon = plotter.Plotter()
    plot_polygon.add_polygon(x_float, y_float)
    plot_polygon.add_point(x_input_float, y_input_float, ray_casting)
    plot_polygon.show()


def user_input(input_str):
    input_str = "Please enter your {}".format(input_str)
    user_value = input(input_str)
    user_value = float(user_value)
    print(user_value)
    user_value_list = []
    user_value_list.append(user_value)
    return user_value_list


if __name__ == "__main__":
        main()













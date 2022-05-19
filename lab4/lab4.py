from quadrangles import Parallelogram, Rectangle, Square
from input_operations import input_points

if __name__ == '__main__':
    n = int(input("Enter the number of quadrangles to be created: "))
    sum_squares_rectangles = 0
    sum_p_parallelograms = 0

    for i in range(n):
        choice = int(input("Enter 1 for parallelogram, 2 for rectangle, 3 for square: "))
        print(f"Enter the coordinates for the figure in such format (x, y): ")
        coordinates = input_points()

        if choice == 1:
            figure = Parallelogram(coordinates)
            p = figure.get_perimeter()
            sum_p_parallelograms += p
            print(f"The perimeter of the parallelogram is {p}")
        elif choice == 2:
            figure = Rectangle(coordinates)
            area = figure.get_area()
            sum_squares_rectangles += area
            print(f"The area of the rectangle is {area}")
        else:
            figure = Square(coordinates)
            area = figure.get_area()
            sum_squares_rectangles += area
            print(f"The area of the square is {area}")

    print(f"The sum of the areas of all the squares and rectangles is {sum_squares_rectangles}")
    print(f"The sum of the perimeters of all the parallelograms is {sum_p_parallelograms}")

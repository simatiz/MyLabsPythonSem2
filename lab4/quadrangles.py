from abc import ABC, abstractmethod
from point import Point, get_distance

class TQuadrangle(ABC):
    def __init__(self, coordinates):
        self.point_1 = Point(coordinates[0], coordinates[1])
        self.point_2 = Point(coordinates[2], coordinates[3])
        self.point_3 = Point(coordinates[4], coordinates[5])
        self.point_4 = Point(coordinates[6], coordinates[7])
        self.side_1 = get_distance(self.point_1, self.point_2)
        self.side_2 = get_distance(self.point_2, self.point_3)
        self.side_3 = get_distance(self.point_3, self.point_4)
        self.side_4 = get_distance(self.point_1, self.point_4)

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Parallelogram(TQuadrangle):
    def get_perimeter(self):
        return (self.side_1 + self.side_2) * 2

    def get_area(self):
        vector_1 = Point(self.point_2.x - self.point_1.x, self.point_2.y - self.point_1.y)
        vector_2 = Point(self.point_4.x - self.point_1.x, self.point_4.y - self.point_1.y)
        return abs(vector_1.x * vector_2.y - vector_1.y * vector_2.x)

class Rectangle(Parallelogram):
    def get_area(self):
        return self.side_1 * self.side_2

class Square(Rectangle):
    def get_perimeter(self):
        return self.side_1 * 4

    def get_area(self):
        return self.side_1 ** 2

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_distance(point_1, point_2):
    return math.sqrt((point_2.x - point_1.x) ** 2 + (point_2.y - point_1.y) ** 2)

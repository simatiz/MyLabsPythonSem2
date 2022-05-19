def input_points():
    coordinates = []
    for i in range(1, 5):
        point_str = input(f"Point {i}: ").split(',')
        x, y = int(point_str[0]), int(point_str[1])
        coordinates.append(x)
        coordinates.append(y)
    return coordinates

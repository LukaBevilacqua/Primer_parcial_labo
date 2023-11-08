def detect_collisions(rect_1, rect_2):
    for r1, r2 in [(rect_1, rect_2), (rect_2, rect_1)]:
        return point_in_rect(r1.topleft, r2) or \
        point_in_rect(r1.topright, r2) or \
        point_in_rect(r1.bottomleft, r2) or \
        point_in_rect(r1.bottomright, r2)


def point_in_rect(point, rect):
    x, y = point
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom


def detect_collisions_circle(rect_1, rect_2):
    distancia = distance_between_centers_rect(rect_1, rect_2)
    r1 = calculate_radius_rect(rect_1)
    r2 = calculate_radius_rect(rect_2)
    return distancia <= (r1 + r2)

def distance_between_points(point_1: tuple, point_2: tuple):
    from math import sqrt
    x1, y1 = point_1
    x2, y2 = point_2
    return sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)

def calculate_radius_rect(rect):
    return rect.width // 2

def distance_between_centers_rect(rect_1, rect_2):
    return distance_between_points(rect_1.center, rect_2.center)






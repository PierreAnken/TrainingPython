import math


class Target:
    points = [16, 8, 4, 2, 1, 0]

    def __init__(self, size, line_amount, distance):
        self.size = size
        self.line_amount = line_amount
        self.distance_m = distance

    def compute_points(self, x_from_center, y_from_center):
        # compute distance between 2 lines
        distance_between_lines = self.size / ((self.line_amount * 2) - 1)
        distance_from_center = math.sqrt(x_from_center ** 2 + y_from_center ** 2)
        arcs_from_center = int(distance_from_center // distance_between_lines)

        if arcs_from_center > self.line_amount:
            return 0
        return Target.points[int(distance_from_center // distance_between_lines)]


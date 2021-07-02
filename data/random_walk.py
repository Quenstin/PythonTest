from random import choice


class RandomWalk:
    def __init__(self, num_position=5000):
        self.num_position = num_position
        self.x_values = [0]
        self.y_value = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_position:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_value[-1] + y_step
            self.x_values.append(x)
            self.y_value.append(y)

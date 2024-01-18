class Wing:
    def __init__(self, x_posn, y_posn):
        self.x = x_posn
        self.y = y_posn
        self.direction = 1

    def turn(self):
        self.direction += 1
        if self.direction >= 3:
            self.direction = 0

    def move(self):
        if self.direction == 0:
        elif self.direction == 1:
        elif self.direction == 2:
        


class Fighter:

class Bullet:


#,b_angle_neighbor_a_angle
class Romb:
    def __init__(self,a_side, a_angle):
        self.a_side = a_side
        self.a_angle = a_angle

    def __setattr__(self, key, value):
        if key == "a_side":
            if value <= 0:
                raise ValueError("Сторона ромба не може бути менше або дорівнювати 0")
        elif key == "a_angle":
            if not (0 < value < 180):
                raise ValueError("Кут ромба не може бути >= 180 або <= 0")
            object.__setattr__(self, "b_angle", 180 - value)
        object.__setattr__(self, key, value)

    def __str__(self):
        return (f"Ромб: сторона a = {self.a_side}, кут a = {self.a_angle},кут b = {self.b_angle}")


romb = Romb(11, 55)
print(romb)
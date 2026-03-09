class Car:
    def __init__(self, max_speed, speed_unit):
        if speed_unit not in ['km/h', 'mph']:
            raise ValueError('Satuan Kecepatan harus "km/h" atau "mph"')

        self.max_speed = max_speed
        self.speed_unit = speed_unit

    def __str__(self):
        return f"{self.max_speed} {self.speed_unit}"

    def __repr__(self):
        return f"Car(max_speed={self.max_speed}, speed_unit='{self.speed_unit}')"


class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.max_speed} knots"

    def __repr__(self):
        return f"Boat(max_speed = {self.max_speed} knots)"

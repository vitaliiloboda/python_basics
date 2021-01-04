class Road:
    mass = 25
    depth = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        return self._length * self._width * self.mass * self.depth / 100


a = Road(500, 20)
print(a.asphalt_mass())

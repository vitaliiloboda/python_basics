class Complex:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        self.complex = complex(number1, number2)

    def __add__(self, other):
        return Complex(self.number1 + other.number1, self.number2 + other.number2)

    def __mul__(self, other):
        return Complex(self.number1 * other.number1 - self.number2 * other.number2,
                       self.number1 * other.number2 + self.number2 * other.number1)

    def __str__(self):
        return str(self.complex)


one = Complex(5, 4)
two = Complex(4, 2)
print(one)
print(two)

print(one + two)
print(one * two)

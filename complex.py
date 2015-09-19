class Complex:
    real = None
    imaginary = None

    def __init__(self, r, i):
        self.real = float(r)
        self.imaginary = float(i)

    def __str__(self):
        r_str = "%.2f" % self.real if self.real != 0 else ""
        i_str = "%.2fi" % abs(self.imaginary) if self.imaginary != 0 else ""
        return "{}{}{}".format(r_str, self.__sign(self.imaginary) if self.imaginary else "", i_str)

    def __sign(self, n):
        if self.real == 0:
            if n < 0: return "-"
            else: return ""
        elif self.real != 0:
            if n < 0: return " - "
            else: return " + "
        else: return ""

    def add(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __add__(self, other):
        return self.add(other)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __sub__(self, other):
        return self.subtract(other)

    def multiply(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real)

    def __mul__(self, other):
        return self.multiply(other)

    def divide(self, other):
        denom = other.real ** 2 + other.imaginary ** 2
        new_real = (self.real * other.real + self.imaginary * other.imaginary) / denom
        new_imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denom
        return Complex(new_real, new_imaginary)

    def __truediv__(self, other):
        return self.divide(other)

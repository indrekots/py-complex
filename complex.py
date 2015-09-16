class Complex:
    real = None
    imaginary = None

    def __init__(self, r, i):
        self.real = float(r)
        self.imaginary = float(i)

    def __str__(self):
        return "%.2f %s %.2fi" % (self.real, "+" if self.imaginary > 0 else "-", abs(self.imaginary))

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

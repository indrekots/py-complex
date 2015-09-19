import unittest
from complex import Complex


class TestComplexNumbers(unittest.TestCase):

    def test_normal(self):
        x = Complex(1, 3)

        self.assertEqual(str(x), "1.00 + 3.00i", "Complex number 1.00 + 3.00i doesn't print the correct value")

    def test_zero_real(self):
        x = Complex(0, 15)

        self.assertEqual(str(x), "15.00i", "Complex number 15.00i doesn't print the correct value")

    def test_negative_imaginary(self):
        x = Complex(1.539, -2.5)

        self.assertEqual(str(x), "1.54 - 2.50i", "Complex number 1.539 - 2.50i doesn't print the correct value")

    def test_negative_imaginary_with_zero_real(self):
        x = Complex(0, -999)

        self.assertEqual(str(x), "-999.00i", "Complex number -999.00i doesn't print the correct value")

    def test_both_negative(self):
        x = Complex(-10, -20)

        self.assertEqual(str(x), "-10.00 - 20.00i", "Complex number -10.00 - 20.00i doesn't print the correct value")

    def test_add(self):
        c1 = Complex(10, 4)
        c2 = Complex(12, -2)

        self.assertEqual(str(c1.add(c2)), "22.00 + 2.00i", "Should equal '22.00 + 2.00i'")

    def test_add_with_operator_overloading(self):
        c1 = Complex(10, 4)
        c2 = Complex(12, -2)

        self.assertEqual(str(c1 + c2), "22.00 + 2.00i", "Should equal '22.00 + 2.00i'")

    def test_subtract(self):
        c1 = Complex(-10, 3)
        c2 = Complex(1, -2)

        self.assertEqual(str(c1.subtract(c2)), "-11.00 + 5.00i", "Should equal '-9.00 + 7.00i'")

    def test_subtract_with_operator_overloading(self):
        c1 = Complex(10, -3)
        c2 = Complex(-5, -2)

        self.assertEqual(str(c1 - c2), "15.00 - 1.00i", "Should equal '15.00 - 1.00i'")

    def test_multiply(self):
        c1 = Complex(13, -2)
        c2 = Complex(-2, -5)

        self.assertEqual(str(c1.multiply(c2)), "-36.00 - 61.00i", "Should equal '-36.00 - 61.00i'")

    def test_multiply_with_operator_overloading(self):
        c1 = Complex(1, -2)
        c2 = Complex(-2, -4)

        self.assertEqual(str(c1 * c2), "-10.00", "Should equal -10.00")

    def test_divide(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)

        self.assertEqual(str(c1.divide(c2)), "0.44 + 0.08i", "Should equal 0.44 + 0.08i")

    def test_divide_with_operator_overloading(self):
        c1 = Complex(3, 13)
        c2 = Complex(7, 17)

        self.assertEqual(str(c1 / c2), "0.72 + 0.12i", "Should equal -200 + 142i")

    def test_absolute_value(self):
        c1 = Complex(6, 8)

        self.assertEqual(c1.abs(), 10, "Should equal 10")

if __name__ == '__main__':
    unittest.main()

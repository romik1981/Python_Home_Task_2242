class ComplexNumbers:

    def __init__(self, real, imagin):
        self.real = real
        self.imagin = imagin

    def __str__(self):
        if self.imagin < 0:
            return f'{self.real} - j{abs(self.imagin)}'
        else:
            return f'{self.real} + j{self.imagin}'

    def __add__(self, other):
        r = self.real + other.real
        i = self.imagin + other.imagin
        return ComplexNumbers(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imagin - other.imagin
        return ComplexNumbers(r, i)

    def __mul__(self, other):
        r = self.real * other.real - self.imagin * other.imagin
        i = self.real * other.imagin + other.real * self.imagin
        return ComplexNumbers(r, i)

    def __truediv__(self, other):
        r = (self.real * other.real + self.imagin * other.imagin) / (pow(other.real, 2) + pow(other.imagin, 2))
        i = (other.real * self.imagin + self.real * other.imagin) / (pow(other.real, 2) + pow(other.imagin, 2))
        return ComplexNumbers(r, i)

z1 = ComplexNumbers(3, 7)
print(z1)

z2 = ComplexNumbers(5, 3)
print(z2)
sum = z1 + z2
print(sum)
sub = z1 - z2
print(sub)
print(z2 - z1)
mul = z1 * z2
print(mul)
print(z2 * z1)
div = z1 / z2
print(div)
div1 = z2 / z1
print(div1)

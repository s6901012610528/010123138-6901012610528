# code run in Thonny Python 3.14.4
# W11 : Create your own
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{self.real}+{self.imag}i"

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def multiply(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return Complex(r, i)


my_complex = [
    Complex(1, 2),
    Complex(3, -1),
    Complex(0, 4)
]

print("My Complex :", my_complex)
print("z1 + z2 : ", my_complex[0].add(my_complex[1]))
print("z1 x z3 : ", my_complex[0].multiply(my_complex[2]))

# ДЗ 15.1. Клас "Прямокутник"

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return math.isclose(self.get_square(), other.get_square(), rel_tol=1e-9)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_area = self.get_square() + other.get_square()
            side = math.sqrt(new_area)
            return Rectangle(side, side)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            if n < 0:
                raise ValueError("Множник повинен бути невід'ємним")
            factor = math.sqrt(n)
            return Rectangle(self.width * factor, self.height * factor)
        return NotImplemented

    __rmul__ = __mul__

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"

if __name__ == "__main__":
    r1 = Rectangle(2, 4)  # площа 8
    r2 = Rectangle(3, 6)  # площа 18

    assert r1.get_square() == 8, "Test1"
    assert r2.get_square() == 18, "Test2"

    r3 = r1 + r2
    assert math.isclose(r3.get_square(), 26, rel_tol=1e-9), "Test3"

    r4 = r1 * 4
    assert math.isclose(r4.get_square(), 32, rel_tol=1e-9), "Test4"

    assert Rectangle(3, 6) == Rectangle(2, 9), "Test5"

    print("Всі випробування пройдені!")
    print(r1, r2, r3, r4, sep="\n")

class Triangle(object):
    def __init__(self, side1, side2, side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
            self.perim = self._perimeter()
            self.sq = self._square()
            self.tr_type = self._triangle_type()

    def __repr__(self):
        return "The triangle with sides a = " + str(self.side1) + ", b = " + str(self.side2) + ", c = " + str(self.side3) + ", has perimeter = " + str(self.perim) + " and square = " + str(self.sq) + ". " + self.tr_type

    @staticmethod
    def _is_exist(self):
        if triangle:
            return True
        else:
            raise ValueError('The triangle is not exist')

    def _perimeter(self):
        p = float((self.side1 + self.side2 + self.side3) / 2)
        return p

    def _square(self):
        p = self._perimeter()
        s = (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5
        return s

    def _triangle_type(self):
        if self.side1 == self.side2 != self.side3 or self.side2 == self.side3 != self.side1 or self.side1 == self.side3 != self.side2:
            return "This is the triangle with two equal sides"
        elif self.side1 == self.side2 == self.side3:
            return "This is the equal triangle"
        else:
            return "This is the scalene triangle"

    @staticmethod
    def is_right(angle1, angle2, angle3):
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("This is the right triangle")
        else:
            print("This is not the right triangle")


#triangle = my_triangle = Triangle(-1, 0, -18)
triangle = my_triangle = Triangle(55, 55, 65)
print(my_triangle)




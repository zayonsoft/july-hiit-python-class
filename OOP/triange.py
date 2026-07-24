class Triangle:
    # this is not necessary
    a = 3
    b = 10
    c = 5

    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3

    def perimeter(self):
        per = self.a + self.b + self.c
        print(f"The Perimeter is: {per}")
        return per


t1 = Triangle(10, 15, 78)
t2 = Triangle(97, 76, 3)

t1.perimeter()
t2.perimeter()

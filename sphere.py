class Circle:

    def __init__(self, r):
        self.r = r

    def volume(self):
        return 4/3*3.14*self.r*self.r*self.r

    def area(self):
        return 4*3.14*self.r*self.r


circle = Circle(2)
circle2 = Circle(3)

print(circle.area());



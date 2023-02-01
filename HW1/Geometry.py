import numpy as np
class Geometry:
    numInstances = 0;
    def __init__(self, name = "Shape", points = None):
        self.name = name
        # name is string that is a name of geometry
        self.points = points
        # points are a list of tuple points = [(x0, y0), (x1, y1), ...]
        Geometry.numInstances += 1;
        def calculate_area(self):
            pass

        def get_name(self):
            return self.name

        @classmethod
        def count_number_of_geometry(cls):
            return Geometry.numInstances;
class Triangle(Geometry):
    def __init__(self, a, b, c):
        super(Triangle, self).__init__("Triangle",[a,b,c]);

    def calculate_area(self):
        # Write a function to take in three tuples and return the area of the triangle
        pass;

class Rectangle(Geometry):
    def __init__(self, a, b):
        super(Rectangle, self).__init__("Rectangle",[a,b]);

    def calculate_area(self):
        x1,y1 = self.points[0];
        x2,y2 = self.points[1];
        length = (x2-x1);
        height = (y2-y1);
        area = length * height;
        return area;
class Square(Rectangle):
    def __init__(self, a, length):
        super(Square, self).__init__(a=a, b=None);
        self.length = length;

    def calculate_area(self):
        area = self.length ** 2;
        return area;
        
class Circle(Geometry):
    def __init__(self, o, r):
        super(Circle, self).__init__("Circle",o);
        self.radius = r;

    def calculate_area(self):
        area = np.pi * (self.radius ** 2);
        return area;
class Polygon(Geometry):
    def __init__(self, points):
        super(Polygon, self).__init__("Polygon",points=points);

    def calculate_area(self):
        pass;

def main():
    a = Square((1,1), 10);
    a.calculate_area();
    b = Circle((1,1), 9);
    b.calculcate_area();
    c = Geometry();
    print(c.numInstances);
    d = Polygon([(1,0), (1,1), (0,2), (-2,1), (-1,0)])
    e = Rectangle((0, 0), (2, 2))

if __name__ == "__main__":
    main();



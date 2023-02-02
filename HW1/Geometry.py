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

    def distance(self, index1, index2):
        x1,y1 = self.points[index1];
        x2,y2 = self.points[index2];
        ds = (x1 - x2) ** 2 + (y1 - y2) ** 2;
        return np.sqrt(ds);

class Triangle(Geometry):
    def __init__(self, a, b, c):
        super(Triangle, self).__init__("Triangle",[a,b,c]);

    def calculate_area(self):
        # Write a function to take in three tuples and return the area of the triangle

        ab = self.distance(0,1);
        ac = self.distance(0,2);
        bc = self.distance(1,2);

        p = (ab + ac + bc) / 2;
        return np.sqrt(p * (p - ab) * (p - ac) * (p - bc));

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
        self.name = "Square";
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
        N = len(self.points)
        S = 0
        for i in range(2, N):
            ab, ac, bc = self.distance(0, i - 1), self.distance(0, i), self.distance(i, i - 1)
            p = (ab + ac + bc) / 2
            S += np.sqrt(p * (p - ab) * (p - ac) * (p - bc))
            return S 
def main():
    pass;

if __name__ == "__main__":
    main();



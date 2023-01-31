import numpy as np
class Geometry:
    def __init__(self, name = "Shape", points = None):
        self.name = name
        # name is string that is a name of geometry
        self.points = points
        # points are a list of tuple points = [(x0, y0), (x1, y1), ...]
        def calculate_area(self):
            pass

        def get_name(self):
            return self.name

        @classmethod
        def count_number_of_geometry(cls):
            pass;

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
        x1, y1 = self.points[0][0];
        x2, y2 = self.points[0][1];
        x3,y3 = self.points[1][0];
        x4,y4 = self.points[1][1];

        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2);
        width = np.sqrt((x4 - x1)**2 +  (y4 - y1)**2);

        area = length * width;
        print(area);

x = Geometry();

y = Rectangle([(0,0), (0,1) ], [(2,1), (2,0)]);
y.calculate_area();
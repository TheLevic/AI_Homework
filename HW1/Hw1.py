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

def matrix_multiplication(A:np.matrix,B:np.matrix):
    rowsA, colsA = A.shape
    rowsB, colsB = B.shape
    # C will be our final matrix
    C = np.zeros((rowsA,colsB))
    #Now need to multiply each item in A's rows by each item in B's cols.
    for row in range(rowsA):
        for col in range(colsB):
            for num in range(colsA):
                C[row,col] += A[row,num] * B[num,col];
    return C;

def pow(A , n):
    if (n == 0):
        return np.eye(A.shape[0])
    else:
        B = pow(A, int(n / 2));
        B = B @ B;
        if (n % 2) == 0:
            return B;
        else:
            return B @ A;


# Getting an array that start with our 1's for our fib sequence
def get_A():
    return np.array([[1., 1.], [1., 0.]])

def fibo(n):
    # Get our array
    A = get_A();
    # Set our f1 variable array to implement the formula
    f1 = np.array([[1.],[1.]]);
    # Implement formula
    fNum = pow(A, n - 1) @ f1;
    # Return fib number
    return int(fNum[0][0]);

def f(n,k):
    # If n < k, the formula says to return 1
    if (n < k):
        return 1;
    else:
        result = 0;
        # We want to loop through all values including k, so we need k + 1 here
        for i in range(1, k + 1):
            result += f(n - i, k);
        return result; 


def recursiveDFS(x, y, matrix, visited, path):
    row,col = np.shape(matrix);
    # Visited is a matrix keeping track of whether we have visited a certain point or not
    visited[x][y] = 1;

    #Now, I need to check my base case
    if (x == row - 1 and y == col - 1 ):
        print(path);
   # Now, I need to check if I can move one way or the other, and if it has been visited
    for dx, dy in [(0,1), (0,-1),(1,0), (-1,0)]:
       u = x + dx;
       v = y + dy; 
       if (u >= 0 and u < row and v >= 0 and v < col and matrix[u][v] != 0 and visited[u][v] == 0):
            # Now I need to append values to the path array
            path.append((u,v))
            recursiveDFS(u, v,matrix,visited,path);
            # If the values are not used when getting to the (row-1,col-1) then they should be popped off the path array.
            path.pop();

def DFS(A:np.matrix):
    # Give a m x n matrix
    # Wanting to find a path from (0,0) to (m-1, n-1 )
    # So I need to treat each spot in the matrix as a node, and (0,0) as the starting node
    recursiveDFS(0,0,A,np.zeros_like(A),[]); 
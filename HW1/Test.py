import random
import numpy as np
from Hw1 import Triangle, Rectangle, Square, Circle, Polygon, matrix_multiplication, pow, fibo, f

##############################
## Test cases for Problem 1 ##
##############################

triangle = Triangle((0, 1), (1, 0), (0, 0))
print("Area of %s: %0.4f" % (triangle.name, triangle.calculate_area()))

rectangle = Rectangle((0, 0), (2, 2))
print("Area of %s: %0.4f" % (rectangle.name, rectangle.calculate_area()))

square = Square((0, 0), 2)
print("Area of %s: %0.4f" % (square.name, square.calculate_area()))

circle = Circle((0, 0), 3)
print("Area of %s: %0.4f" % (circle.name, circle.calculate_area()))

polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print("Area of %s: %0.4f" % (polygon.name, polygon.calculate_area()))

#########################################
## Test cases for matrix multplication ##
#########################################

for test in range(10):
    m, n, k = random.randint(3, 10), random.randint(3, 10), random.randint(3, 10)
    A = np.random.randn(m, n)
    B = np.random.randn(n, k)
    assert np.mean(np.abs(A.dot(B) - matrix_multiplication(A, B))) <= 1e-7, "Your implmentation is wrong!"
    print("[Test Case %d]. Your implementation is correct!" % test)

#####################################
## Test cases for the pow function ##
#####################################

for test in range(10):
    n = random.randint(2, 5)
    A = np.random.randn(n, n)
    print("A^{} = {}".format(n, pow(A, n)))


#####################################################
## Test Cases for Fibonacci and Recursive Sequence ##
#####################################################

a, b = 1, 1
for i in range(2, 10):
    c = a + b
    assert (fibo(i) == c), "You implementation is incorrect"
    print("[Test Case %d]. Your implementation is correct!. fibo(%d) = %d" % (i - 2, i, fibo(i)))
    a = b
    b = c

for n in range(5, 11):
    for k in range(2, 5):
        print("f(%d, %d) = %d" % (n, k, f(n, k)))

########################################### 
## Test Cases for BFS, DFS, Find Minimum ##
###########################################

# As = np.load("test.npy", allow_pickle=True)
# for test in range(len(As)):
#     A = As[test]
#     print("Test Case %d" % test)
#     print(A) 
#     BFS(A) # or DFS(A) or FindMinium(A) 
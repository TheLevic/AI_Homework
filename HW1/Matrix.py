import numpy as np
def matrix_multiplication(A:np.matrix,B:np.matrix):
    # Need to check that there are the same amount of cols in A as rows in B
    rowsA, colsA = A.shape
    rowsB, colsB = B.shape

    C = np.zeros((rowsA,colsB))


    if rowsA > colsB:
        print("Can not do matrix multiplication with these to matricies")
    else:
        for row in range(rowsA):
            for col in range(colsB):
                for num in range(colsA):
                    C[row,col] += A[row,num] * B[num,col];
        return C;


A = np.random.randn(4, 5)
B = np.random.randn(5, 6) 
assert np.mean(np.abs(A.dot(B) - matrix_multiplication(A, B))) <= 1e-7, "Your implmentation is wrong!"
print("Your implementation is correct!")
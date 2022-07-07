def square_matrix_simple(matrix=[]):
    squer = [[(row[i] * row[i])for i in range(3)] for row in matrix]
    return squer

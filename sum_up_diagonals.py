def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    size = len(matrix)
    diagonal_sum_tl_br = 0
    diagonal_sum_tr_bl = 0

    for i in range(size): 
        diagonal_sum_tl_br += matrix[i][i]
        diagonal_sum_tr_bl += matrix[i][size - i - 1]
    return diagonal_sum_tr_bl + diagonal_sum_tl_br
from typing import List
import itertools


def _check_valid(matrix):
    if type(matrix) is list and matrix:
        l = len(matrix[0])
        for item in matrix:
            if type(item) is list and len(item) == l:
                continue
            else:
                return False
    else:
        return False
    return True


class Matrix:

    def __init__(self, matrix: List[List[int]]):
        if _check_valid(matrix):
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')

    def __str__(self):
        return self.__str_m

    def __add__(self, other):
        i = 0
        new_matrix = []
        while i < len(self.matrix):
            element = itertools.zip_longest(self[i], other[i])
            sum_el = []
            for i1, i2 in element:
                sum_el.append(i1 + i2)
            new_matrix.append(sum_el)
            i += 1
        return Matrix(new_matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    @property
    def __str_m(self):
        result_str = ''
        counter = 1
        for i in self.matrix:
            if not counter == 1:
                result_str = result_str + "\n| "
            else:
                counter += 1
                result_str = result_str + "| "
            for _ in i:
                result_str += f'{_}'
            result_str += ' | '
        return result_str


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """

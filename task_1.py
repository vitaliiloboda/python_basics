class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for i in range(len(self.matrix)):
            list_str = ''
            for j in range(len(self.matrix[i])):
                inner_list_str = f'{self.matrix[i][j]}'
                if j == len(self.matrix[i]) - 1:
                    list_str += f'{inner_list_str}'
                else:
                    list_str += f'{inner_list_str}  '

            result += f'{list_str} \n'
        return result

    def __add__(self, other):
        result = []

        for i in range(len(self.matrix)):
            sub_result = []

            for j in range(len(self.matrix[i])):
                sub_result.append(self.matrix[i][j] + other.matrix[i][j])

            result.append(sub_result)

        return Matrix(result)


matrix1 = Matrix([[1, 5, 4], [4, 7, 3], [8, 2, 4], [7, 7, 7]])
matrix2 = Matrix([[5, 7, 2], [1, 6, 7], [3, 8, 2], [6, 4, 3]])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)

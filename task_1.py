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


######################################################2#################################################################

class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(['\t'.join(list(map(str, i))) for i in self.my_list])

    def __add__(self, other):
        result = []

        for m in range(len(self.my_list)):
            b = [self.my_list[m][k] + other.my_list[m][k] for k in range(len(self.my_list[0]))]
            result.append(b)

        return Matrix(result)


matrix = Matrix([[1, 2, 8], [4, 3, 1], [7, 1, 4], [1, 2, 3]])
matrix2 = Matrix([[4, 5, 3], [6, 9, 4], [6, 8, 1], [8, 9, 0]])

print(matrix)
print()
print(matrix2)
print()
print(matrix + matrix2)

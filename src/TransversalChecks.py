class CheckTransversal:

    @staticmethod
    def check_transversal(transversal, n):
        """
        Checks if the transversal is
        :param transversal: A list of cells which represents a rainbow matching.
        :param n: A proper transversal should be at size of n.
        :return: True- if the transversal is properly and legal, False- otherwise.
        """
        if len(transversal) != n:
            print("ERROR: Not full. Size: ", len(transversal))
            return False
        for cell_1 in range(len(transversal)):
            for cell_2 in range(cell_1 + 1, len(transversal)):
                if transversal[cell_1][0] == transversal[cell_2][0]:
                    print("ERROR: Same row.", transversal[cell_1], transversal[cell_2])
                    return False
                if transversal[cell_1][1] == transversal[cell_2][1]:
                    print("ERROR: Same column.", transversal[cell_1], transversal[cell_2])
                    return False
                if transversal[cell_1][2] == transversal[cell_2][2]:
                    print("ERROR: Same color.", transversal[cell_1], transversal[cell_2])
                    return False
        return True

    @staticmethod
    def is_there_transversal(matrix, n, row, column, transversal):
        """
        A back-tracking recursive function which finds if there is a transversal in the given matrix.
        :param matrix: The given nXn matrix which represents a graph.
        :param n: The matrix has n rows and n columns.
        :param row: The row index in the matrix.
        :param column: The column index in the matrix.
        :param transversal: A list of cells which represents a legal transversal.
        :return: True- there is at least one transversal in the matrix, False- otherwise.
        """
        if len(transversal) == n:
            return CheckTransversal.check_transversal(transversal, n)
        if row >= n or row < 0 or column >= n or column < 0:
            return False
        if CheckTransversal.valid_cell(matrix, row, column, transversal):
            transversal.append([row, column, matrix[row][column]])
            return CheckTransversal.is_there_transversal(matrix, n, row + 1, 0, transversal) or \
                CheckTransversal.is_there_transversal(matrix, n, row, column + 1, transversal[:row])
        else:
            return CheckTransversal.is_there_transversal(matrix, n, row, column + 1, transversal)

    @staticmethod
    def valid_cell(matrix, row, column, transversal):
        """
        Help-function for the function is_there_transversal.
        :param matrix: The given nXn matrix which represents a graph.
        :param row: The row index in the matrix.
        :param column: The column index in the matrix.
        :param transversal: A list of cells which represents a legal transversal.
        :return: True- if the cell is legal to be added to the current transversal, False- otherwise.
        """
        if matrix[row][column] == 0:
            return False
        if len(transversal) == 0:
            return True
        for cell in transversal:
            if cell[0] == row or cell[1] == column or cell[2] == matrix[row][column]:
                return False
        return True

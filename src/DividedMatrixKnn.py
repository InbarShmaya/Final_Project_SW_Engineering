import random


class DividedMatrixKnn:
    def __init__(self, n, k):
        """
        Creates a matrix which represents a random coloring Knn.
        :param n: The size of the matrix is nXn.
        :param k: The number of the different symbols (colors) in the matrix.
        """
        self.n = n
        self.k = k
        self.matrix = [[random.randint(1, k) for i in range(n)] for j in range(n)]
        print("Random coloring Knn:")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.matrix]))
        print()

    def algo(self):
        """
        The chosen algorithm we analyzed in the project.
        :return: A full/ partial transversal.
        """
        transversal = []
        if self.n % 2 != 0:
            return transversal
        cols_list = [i for i in range(self.n)]
        colors_list = []

        # Handling the T1
        T1_cells = []
        for row in range(int(self.n / 2)):
            for col in range(int(self.n / 2)):
                if col not in cols_list:    # The column has been chosen already
                    continue
                color = self.matrix[row][col]
                if color not in colors_list:
                    T1_cells.append([row, col, color])
                    colors_list.append(color)
                    cols_list.remove(col)
                    break

        # Handling the T2
        T2_cells = []
        for row in range(int(self.n / 2), self.n):
            for col in range(int(self.n / 2), self.n):
                if col not in cols_list:    # The column has been chosen already
                    continue
                color = self.matrix[row][col]
                if color not in colors_list:
                    T2_cells.append([row, col, color])
                    colors_list.append(color)
                    cols_list.remove(col)
                    break

        C1_cols = []
        C2_cols = []
        R1_rows = []
        R2_rows = []
        for index in range(0, int(self.n / 2)):
            flag_row = False
            flag_col = False
            for cell in T1_cells:
                if cell[0] == index:
                    flag_row = True
                if cell[1] == index:
                    flag_col = True
            if not flag_row:
                R1_rows.append(index)
            if not flag_col:
                C1_cols.append(index)
        for index in range(int(self.n / 2), self.n):
            flag_row = False
            flag_col = False
            for cell in T2_cells:
                if cell[0] == index:
                    flag_row = True
                if cell[1] == index:
                    flag_col = True
            if not flag_row:
                R2_rows.append(index)
            if not flag_col:
                C2_cols.append(index)

        # Handling the H1
        row = 0
        col = 0
        while row < len(R1_rows):
            while col < len(C1_cols):
                for cell in T2_cells:
                    # Check if the inversion is legal
                    if self.matrix[cell[0]][C1_cols[col]] not in colors_list or self.matrix[cell[0]][C1_cols[col]] == cell[2]:
                        if self.matrix[R1_rows[row]][cell[1]] not in colors_list or self.matrix[R1_rows[row]][cell[1]] == cell[2]:
                            if self.matrix[R1_rows[row]][cell[1]] != self.matrix[cell[0]][C1_cols[col]]:
                                T2_cells.remove(cell)
                                transversal.append([cell[0], C1_cols[col], self.matrix[cell[0]][C1_cols[col]]])
                                transversal.append([R1_rows[row], cell[1], self.matrix[R1_rows[row]][cell[1]]])
                                colors_list.append(self.matrix[cell[0]][C1_cols[col]])
                                colors_list.append(self.matrix[R1_rows[row]][cell[1]])
                                R1_rows.remove(R1_rows[row])
                                C1_cols.remove(C1_cols[col])
                                break
                col += 1
            row += 1

        # Handling the H2
        row = 0
        col = 0
        while row < len(R2_rows):
            while col < len(C2_cols):
                for cell in T1_cells:
                    # Check if the inversion is legal
                    if (self.matrix[cell[0]][C2_cols[col]] not in colors_list) or self.matrix[cell[0]][C2_cols[col]] == cell[2]:
                        if self.matrix[R2_rows[row]][cell[1]] not in colors_list or self.matrix[R2_rows[row]][cell[1]] == cell[2]:
                            if self.matrix[R2_rows[row]][cell[1]] != self.matrix[cell[0]][C2_cols[col]]:
                                T1_cells.remove(cell)
                                transversal.append([cell[0], C2_cols[col], self.matrix[cell[0]][C2_cols[col]]])
                                transversal.append([R2_rows[row], cell[1], self.matrix[R2_rows[row]][cell[1]]])
                                colors_list.append(self.matrix[cell[0]][C2_cols[col]])
                                colors_list.append(self.matrix[R2_rows[row]][cell[1]])
                                R2_rows.remove(R2_rows[row])
                                C2_cols.remove(C2_cols[col])
                                break
                col += 1
            row += 1

        for cell in T1_cells:
            transversal.append(cell)
        for cell in T2_cells:
            transversal.append(cell)

        return transversal

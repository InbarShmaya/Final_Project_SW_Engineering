import math
import random
from TransversalChecks import *


class RandomColoringDiracGraphs:
    def __init__(self, n, k):
        """
        Creates a matrix which represents a  random coloring Dirac graph.
        :param n: The size of the matrix is nXn.
        :param k: The number of the different symbols (colors) in the matrix.
        """
        self.n = n
        self.k = k
        self.matrix = [[0 for i in range(n)] for j in range(n)]
        self.colored_row = [0 for i in range(n)]
        self.colored_col = [0 for j in range(n)]
        self.cells_set = []
        for i in range(n):
            for j in range(n):
                self.cells_set.append([i, j, self.matrix[i][j]])

        while math.ceil((n + 1) / 2) > min(self.colored_row) or math.ceil((n + 1) / 2) > min(self.colored_col):
            place = random.randint(0, len(self.cells_set) - 1)
            self.cells_set[place][2] = random.randint(1, k)
            self.colored_row[self.cells_set[place][0]] += 1
            self.colored_col[self.cells_set[place][1]] += 1
            self.matrix[self.cells_set[place][0]][self.cells_set[place][1]] = self.cells_set[place][2]
            self.cells_set.remove([self.cells_set[place][0], self.cells_set[place][1], self.cells_set[place][2]])
        print(CheckTransversal.is_there_transversal(self.matrix, self.n, 0, 0, []))

        print("Random Coloring Dirac graph:")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.matrix]))
        print()
        print("Number of edges in the graph: ", sum(self.colored_row))
        print()

    def find_transversal_naive(self):
        """
        Finds a transversal in the naive way, two-stages algorithm (greedy algorithm, then fixes using inversions).
        :return: A full/ partial transversal.
        """
        # Initialize:
        rows_set = set()
        columns_set = set()
        colors_set = set()
        for i in range(self.n):
            rows_set.add(i)
            columns_set.add(i)
        for i in range(1, self.k + 1):
            colors_set.add(i)
        transversal = []
        stuck_counter = 0     # The number of times the algorithm got stuck
        while len(transversal) < self.n and stuck_counter < 100:   # Choose n cells
            chosen_row = random.sample(rows_set, 1)[0]
            chosen_column = random.sample(columns_set, 1)[0]
            chosen_color = self.matrix[chosen_row][chosen_column]
            if chosen_color not in colors_set:  # The color is already chosen
                stuck_counter += 1
                continue
            else:
                stuck_counter = 0
                choice = [chosen_row, chosen_column, chosen_color]
                transversal.append(choice)
                rows_set.discard(choice[0])
                columns_set.discard(choice[1])
                colors_set.discard(choice[2])
        legal_cells = []
        for row in rows_set:
            for column in columns_set:
                color = self.matrix[row][column]
                if color in colors_set:
                    legal_cells.append([row, column, color])
        while legal_cells:
            chosen_cell = random.sample(legal_cells, 1)[0]
            choice = [chosen_cell[0], chosen_cell[1], chosen_cell[2]]
            transversal.append(choice)
            rows_set.discard(choice[0])
            columns_set.discard(choice[1])
            colors_set.discard(choice[2])
            temp_list = legal_cells
            new_legal_cells = []
            place_cell = 0
            while temp_list:
                cell = legal_cells[place_cell]
                if cell[0] == chosen_cell[0] or cell[1] == chosen_cell[1] or cell[2] == chosen_cell[2]:
                    temp_list.remove(cell)
                else:
                    temp_list.remove(cell)
                    new_legal_cells.append(cell)
            legal_cells = new_legal_cells

        # Inversions
        stuck_counter = 0
        while len(transversal) < self.n and stuck_counter < self.n:   # Choose n cells
            chosen_row = random.sample(rows_set, 1)[0]
            chosen_column = random.sample(columns_set, 1)[0]
            chosen_color = self.matrix[chosen_row][chosen_column]
            if chosen_color not in colors_set:  # The color is already chosen
                flag_inversion = False
                for cell in transversal:
                    color_1 = self.matrix[chosen_row][cell[1]]
                    color_2 = self.matrix[cell[0]][chosen_column]
                    if color_1 != color_2 and (color_1 in colors_set and color_2 in colors_set):     # Allow inversion
                        transversal.remove(cell)

                        choice = [chosen_row, cell[1], color_1]
                        transversal.append(choice)
                        rows_set.discard(choice[0])
                        columns_set.discard(choice[1])
                        colors_set.discard(choice[2])

                        choice = [cell[0], chosen_column, color_2]
                        transversal.append(choice)
                        rows_set.discard(choice[0])
                        columns_set.discard(choice[1])
                        colors_set.discard(choice[2])

                        flag_inversion = True
                        break
                if not flag_inversion:
                    stuck_counter += 1
            else:
                stuck_counter = 0
                choice = [chosen_row, chosen_column, chosen_color]
                transversal.append(choice)
                rows_set.discard(chosen_row)
                columns_set.discard(chosen_column)
                colors_set.discard(chosen_color)

        return transversal

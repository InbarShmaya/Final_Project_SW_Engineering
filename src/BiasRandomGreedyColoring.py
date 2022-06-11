import random

class BiasRandomGreedyColoring:
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

    def find_transversal_bias(self):
        """
        Finds a transversal in the bias way- First add to the transversal cells with the most uncommon symbols in
        the random coloring Dirac graph.
        :return: A full/ partial transversal.
        """
        # Initialize:
        self.colors_set = {}
        for color in range(1, self.k + 1):
            self.colors_set[color] = []
        for row in range(self.n):
            for col in range(self.n):
                self.colors_set[self.matrix[row][col]].append([row, col])
        self.remove_empty_color()
        transversal = []
        stuck_counter = 0     # The number of times the algorithm got stuck
        while len(transversal) < self.n and stuck_counter < 100:   # Choose n cells
            if len(self.colors_set) == 0:  # There are no available colors/ cells
                stuck_counter += 1
                continue
            curr_colors_list = []
            min_val = min([len(self.colors_set[ele]) for ele in self.colors_set])
            for ele in self.colors_set:
                if len(self.colors_set[ele]) == min_val:
                    curr_colors_list.append(ele)
            stuck_counter = 0
            color_choice = random.choice(curr_colors_list)
            position_choice = random.choice(self.colors_set[color_choice])
            transversal.append([position_choice[0], position_choice[1], color_choice])
            self.colors_set.pop(color_choice, None)
            for color in self.colors_set:
                curr_cells_list = []
                for cell in self.colors_set[color]:
                    if not (cell[0] == position_choice[0] or cell[1] == position_choice[1]):
                        curr_cells_list.append(cell)
                self.colors_set[color] = curr_cells_list
            self.remove_empty_color()
        return transversal

    def remove_empty_color(self):
        """
        Help function of the function find_transversal_bias.
        :return: None.
        """
        for item in list(self.colors_set):
            if len(self.colors_set[item]) == 0:
                self.colors_set.pop(item, None)

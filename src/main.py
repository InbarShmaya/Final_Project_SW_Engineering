from RandomColoringKnn import *
from RandomColoringDiracGraphs import *
from BiasRandomGreedyColoring import *
from DividedMatrixKnn import *
from TransversalChecks import *
import math


# n between 50 to 200 (10+-) what is the highest mu that for it 90% of the runs end with full transversal?

# n =     50 |  60 |  70 |  80 |  90 | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 | 180 | 190 | 200 |
# mu =  0.744|0.763|0.778|0.793|0.803|0.815|0.821| 0.83|0.834|0.842|0.844|0.848|0.855| 0.86|0.863|0.865|

def main():
    mu = 0.7
    n = 36
    k = math.floor(n / mu)

    obj_matrix = RandomColoringKnn(n, k)
    # RandomColoringKnn.cyclic_latin_square(obj_matrix)
    # RandomColoringKnn.addition_table(obj_matrix)
    print("There is a transversal in this matrix: ",
          CheckTransversal.is_there_transversal(obj_matrix.matrix, n, 0, 0, []))
    transversal = RandomColoringKnn.find_transversal_naive(obj_matrix)
    print("The transversal found for the class RandomColoringKnn: ", transversal)
    print("This is a proper transversal: ", CheckTransversal.check_transversal(transversal, n))
    print()

    obj_matrix = RandomColoringDiracGraphs(n, k)
    print("There is a transversal in this matrix: ",
          CheckTransversal.is_there_transversal(obj_matrix.matrix, n, 0, 0, []))
    transversal = RandomColoringDiracGraphs.find_transversal_naive(obj_matrix)
    print("The transversal found for the class RandomColoringKnn: ", transversal)
    print("This is a proper transversal: ", CheckTransversal.check_transversal(transversal, n))
    print()

    obj_matrix = BiasRandomGreedyColoring(n, k)
    print("There is a transversal in this matrix: ",
          CheckTransversal.is_there_transversal(obj_matrix.matrix, n, 0, 0, []))
    transversal = BiasRandomGreedyColoring.find_transversal_bias(obj_matrix)
    print("The transversal found for the class RandomColoringKnn: ", transversal)
    print("This is a proper transversal: ", CheckTransversal.check_transversal(transversal, n))
    print()

    obj_matrix = DividedMatrixKnn(n, k)
    print("There is a transversal in this matrix: ",
          CheckTransversal.is_there_transversal(obj_matrix.matrix, n, 0, 0, []))
    transversal = DividedMatrixKnn.algo(obj_matrix)
    print("The transversal found for the class RandomColoringKnn: ", transversal)
    print("This is a proper transversal: ", CheckTransversal.check_transversal(transversal, n))
    print()


if __name__ == "__main__":
    main()

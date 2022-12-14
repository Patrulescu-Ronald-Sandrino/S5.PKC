from GCDSolverBinary import BinaryAlgorithm
from GCDSolverEuclidean import EuclideanAlgorithm
from GCDSolver import GCDSolver
from GCDSolverPrimeFactorization import PrimeFactorization


class TestGCD:
    def run(self):
        solvers: list[GCDSolver] = [EuclideanAlgorithm(), BinaryAlgorithm(), PrimeFactorization()]
        self.__test_solvers(solvers)

    def __test_solvers(self, solvers: list[GCDSolver]):
        for solver in solvers:
            print(f"Testing {solver.__class__.__name__}", end=" ")
            self.__test_solver(solver)
            print("OK")

    def __test_solver(self, solver):
        test = lambda a, b, expected: solver.solve(a, b) == expected

        # assert test(1, 1, 2) # AssertionError
        try:
            assert test(0, 0, 0)
            assert False
        except ValueError:
            pass
        assert test(0, 5, 5)
        assert test(7, 0, 7)

        assert test(10, 5, 5)
        assert test(3, 12, 3)
        assert test(4, 12, 4)
        assert test(54, 24, 6)

        if type(solver) != PrimeFactorization:
            # if True:
            assert test(1234567890, 9876543210, 90)

            big_number = 100_000_000_000_000_007
            assert test(big_number, 100_000_000_000_000_009, 1)
            assert test(big_number, big_number, big_number)
            assert test(big_number, big_number * big_number, big_number)
            assert test(big_number, big_number * big_number * big_number, big_number)
            assert test(big_number, big_number * big_number * big_number * big_number, big_number)

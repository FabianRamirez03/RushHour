import AI
import time
import unittest


class LevelTesting(unittest.TestCase):

    # Beginner

    def test_01(self):
        board = [['B', 'B', '_', '_', '_', 'g'],
                 ['c', '_', '_', 'h', '_', 'g'],
                 ['c', 'A', 'A', 'h', '_', 'g'],
                 ['c', '_', '_', 'h', '_', '_'],
                 ['d', '_', '_', '_', 'F', 'F'],
                 ['d', '_', 'E', 'E', 'E', '_']
                 ]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 01 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_02(self):
        board = [['b', '_', '_', 'E', 'E', 'E'],
                 ['b', '_', '_', 'c', '_', 'd'],
                 ['A', 'A', '_', 'c', 'f', 'd'],
                 ['J', 'J', 'J', '_', 'f', 'd'],
                 ['_', '_', 'i', '_', 'G', 'G'],
                 ['K', 'K', 'i', 'H', 'H', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 02 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_03(self):
        board = [['_', '_', '_', '_', '_', '_'],
                 ['_', '_', '_', '_', '_', '_'],
                 ['_', 'A', 'A', 'g', '_', '_'],
                 ['_', 'B', 'B', 'g', '_', 'f'],
                 ['_', 'c', '_', 'g', '_', 'f'],
                 ['_', 'c', 'D', 'D', '_', 'f']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 03 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_04(self):
        board = [['c', '_', '_', 'd', '_', '_'],
                 ['c', '_', '_', 'd', '_', '_'],
                 ['c', 'A', 'A', 'd', '_', '_'],
                 ['_', '_', 'f', 'G', 'G', 'G'],
                 ['_', '_', 'f', '_', '_', 'h'],
                 ['_', '_', 'I', 'I', 'I', 'h']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 04 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_05(self):
        board = [['B', 'B', '_', 'f', '_', 'h'],
                 ['c', '_', '_', 'f', 'g', 'h'],
                 ['c', 'A', 'A', 'f', 'g', 'i'],
                 ['c', 'E', 'E', 'E', 'g', 'i'],
                 ['d', '_', '_', '_', 'K', 'K'],
                 ['d', '_', '_', '_', 'L', 'L']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 05 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_06(self):
        board = [['C', 'C', '_', 'i', '_', '_'],
                 ['B', 'B', '_', 'i', 'j', 'k'],
                 ['_', 'A', 'A', 'h', 'j', 'k'],
                 ['D', 'D', 'f', 'h', 'j', 'k'],
                 ['e', '_', 'f', 'h', '_', '_'],
                 ['e', '_', '_', 'G', 'G', 'G']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 06 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_07(self):
        board = [['_', 'b', 'C', 'C', 'g', 'h'],
                 ['_', 'b', '_', 'd', 'g', 'h'],
                 ['_', 'A', 'A', 'd', '_', 'i'],
                 ['_', '_', 'E', 'E', '_', 'i'],
                 ['_', '_', '_', 'f', '_', '_'],
                 ['_', '_', '_', 'f', '_', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 07 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_08(self):
        board = [['_', '_', '_', 'L', 'L', 'k'],
                 ['_', '_', 'N', 'N', 'm', 'k'],
                 ['A', 'A', 'e', 'i', 'm', 'k'],
                 ['B', 'B', 'e', 'i', 'J', 'J'],
                 ['C', 'C', 'f', 'H', 'H', 'H'],
                 ['D', 'D', 'f', 'G', 'G', 'G']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 08 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_09(self):
        board = [['B', 'B', '_', 'f', '_', 'h'],
                 ['c', '_', '_', 'f', 'g', 'h'],
                 ['c', 'A', 'A', 'f', 'g', 'i'],
                 ['c', 'E', 'E', 'E', 'g', 'i'],
                 ['d', '_', '_', '_', 'K', 'K'],
                 ['d', '_', '_', '_', 'L', 'L']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 09 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_10(self):
        board = [['E', 'E', 'n', '_', 'M', 'M'],
                 ['D', 'D', 'n', '_', '_', 'l'],
                 ['g', 'A', 'A', '_', '_', 'l'],
                 ['g', 'B', 'B', 'B', '_', 'l'],
                 ['g', '_', '_', 'k', 'J', 'J'],
                 ['H', 'H', '_', 'k', 'I', 'I']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 10 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    # Intermediate

    def test_11(self):
        board = [['b', 'C', 'C', 'd', '_', '_'],
                 ['b', '_', '_', 'd', '_', '_'],
                 ['b', 'A', 'A', 'd', '_', '_'],
                 ['_', '_', 'f', 'E', 'E', 'E'],
                 ['_', '_', 'f', '_', '_', 'g'],
                 ['_', '_', 'H', 'H', 'H', 'g']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 11 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_12(self):
        board = [['c', 'B', 'B', '_', '_', 'j'],
                 ['c', '_', 'd', '_', '_', 'j'],
                 ['A', 'A', 'd', '_', '_', 'j'],
                 ['_', '_', 'd', 'I', 'I', 'I'],
                 ['_', '_', '_', '_', 'h', '_'],
                 ['G', 'G', 'G', '_', 'h', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 12 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_13(self):
        board = [['C', 'C', 'B', 'B', 'm', '_'],
                 ['_', '_', 'k', '_', 'm', 'd'],
                 ['_', 'l', 'k', 'A', 'A', 'd'],
                 ['i', 'l', '_', 'H', 'H', 'd'],
                 ['i', '_', '_', 'g', 'E', 'E'],
                 ['i', 'J', 'J', 'g', 'F', 'F']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 13 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_14(self):
        board = [['E', 'E', 'f', '_', '_', '_'],
                 ['_', '_', 'f', '_', 'G', 'G'],
                 ['b', 'c', 'A', 'A', 'h', 'i'],
                 ['b', 'c', 'D', 'D', 'h', 'i'],
                 ['_', '_', 'l', '_', 'J', 'J'],
                 ['K', 'K', 'l', '_', '_', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 14 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_15(self):
        board = [['_', 'D', 'D', 'E', 'E', '_'],
                 ['B', 'B', 'C', 'C', 'f', 'g'],
                 ['l', 'm', 'A', 'A', 'f', 'g'],
                 ['l', 'm', 'n', 'o', 'f', 'g'],
                 ['l', 'm', 'n', 'o', 'I', 'I'],
                 ['_', 'K', 'K', 'J', 'J', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 15 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_16(self):
        board = [['C', 'C', '_', 'i', '_', '_'],
                 ['B', 'B', '_', 'i', 'j', 'k'],
                 ['_', 'A', 'A', 'h', 'j', 'k'],
                 ['D', 'D', 'f', 'h', 'j', 'k'],
                 ['e', '_', 'f', 'h', '_', '_'],
                 ['e', '_', '_', 'G', 'G', 'G']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 16 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_17(self):
        board = [['G', 'G', 'H', 'H', 'j', 'k'],
                 ['f', '_', 'I', 'I', 'j', 'k'],
                 ['f', 'e', 'd', 'A', 'A', 'k'],
                 ['_', 'e', 'd', 'B', 'B', 'B'],
                 ['_', '_', 'd', '_', '_', '_'],
                 ['C', 'C', '_', '_', '_', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 17 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_18(self):
        board = [['C', 'C', 'd', 'e', '_', '_'],
                 ['B', 'B', 'd', 'e', '_', '_'],
                 ['g', 'A', 'A', 'e', '_', '_'],
                 ['g', 'F', 'F', 'F', '_', '_'],
                 ['g', 'I', 'I', '_', '_', '_'],
                 ['H', 'H', 'H', '_', '_', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 18 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_19(self):
        board = [['C', 'C', 'd', 'e', '_', '_'],
                 ['B', 'B', 'd', 'e', '_', '_'],
                 ['g', 'A', 'A', 'e', '_', '_'],
                 ['g', 'F', 'F', 'F', '_', '_'],
                 ['g', 'I', 'I', '_', '_', '_'],
                 ['H', 'H', 'H', '_', '_', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 19 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_20(self):
        board = [['b', '_', '_', 'J', 'J', 'J'],
                 ['b', 'C', 'C', 'i', '_', '_'],
                 ['A', 'A', 'd', 'i', '_', 'g'],
                 ['_', '_', 'd', '_', '_', 'g'],
                 ['_', '_', 'e', 'H', 'H', 'g'],
                 ['_', '_', 'e', 'F', 'F', 'F']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 20 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    # Advanced

    def test_21(self):
        board = [['C', 'C', 'd', 'e', '_', '_'],
                 ['b', '_', 'd', 'e', '_', '_'],
                 ['b', 'A', 'A', 'e', '_', '_'],
                 ['b', 'H', 'H', 'H', '_', '_'],
                 ['_', '_', '_', '_', '_', '_'],
                 ['_', '_', '_', 'G', 'G', 'G']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 21 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_22(self):
        board = [['_', '_', 'c', 'D', 'D', 'D'],
                 ['b', '_', 'c', 'k', 'M', 'M'],
                 ['b', 'A', 'A', 'k', '_', '_'],
                 ['_', 'g', '_', 'k', 'J', 'J'],
                 ['f', 'g', 'L', 'L', '_', 'i'],
                 ['f', 'E', 'E', 'E', '_', 'i']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 22 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_23(self):
        board = [['_', '_', 'D', 'D', 'D', 'b'],
                 ['_', '_', 'e', 'C', 'C', 'b'],
                 ['_', '_', 'e', 'A', 'A', 'b'],
                 ['_', '_', 'f', 'i', 'G', 'G'],
                 ['_', '_', 'f', 'i', 'H', 'H'],
                 ['_', '_', 'J', 'J', 'J', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 23 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_24(self):
        board = [['_', '_', 'b', 'I', 'I', '_'],
                 ['_', 'c', 'b', '_', '_', '_'],
                 ['d', 'c', 'A', 'A', 'j', '_'],
                 ['d', 'E', 'E', '_', 'j', '_'],
                 ['F', 'F', 'F', '_', 'h', '_'],
                 ['G', 'G', '_', '_', 'h', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 24 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_25(self):
        board = [['L', 'L', 'm', '_', 'J', 'J'],
                 ['K', 'K', 'm', '_', '_', 'h'],
                 ['c', 'A', 'A', '_', 'i', 'h'],
                 ['c', 'B', 'B', 'B', 'i', 'h'],
                 ['c', 'd', '_', 'e', 'G', 'G'],
                 ['_', 'd', '_', 'e', 'F', 'F']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 25 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_26(self):
        board = [['_', 'l', '_', 'F', 'F', 'F'],
                 ['k', 'l', '_', 'g', 'b', '_'],
                 ['k', 'A', 'A', 'g', 'b', 'e'],
                 ['j', 'H', 'H', 'H', 'b', 'e'],
                 ['j', '_', 'i', '_', '_', 'd'],
                 ['_', '_', 'i', 'C', 'C', 'd']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 26 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_27(self):
        board = [['b', 'D', 'D', 'e', '_', '_'],
                 ['b', 'C', 'C', 'e', '_', '_'],
                 ['A', 'A', 'f', 'e', '_', 'm'],
                 ['_', '_', 'f', 'J', 'J', 'm'],
                 ['_', '_', 'g', '_', '_', 'm'],
                 ['_', '_', 'g', 'K', 'K', 'K']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 27 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_28(self):
        board = [['D', 'D', 'D', 'e', '_', '_'],
                 ['_', '_', 'c', 'e', 'F', 'F'],
                 ['A', 'A', 'c', '_', '_', '_'],
                 ['b', 'g', 'c', 'K', 'K', 'l'],
                 ['b', 'g', 'J', 'J', 'J', 'l'],
                 ['H', 'H', 'I', 'I', '_', 'l']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 28 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_29(self):
        board = [['H', 'H', 'H', '_', 'i', '_'],
                 ['_', '_', 'g', '_', 'i', '_'],
                 ['A', 'A', 'g', '_', 'i', 'j'],
                 ['b', 'C', 'C', 'M', 'M', 'j'],
                 ['b', 'D', 'D', 'e', '_', 'l'],
                 ['F', 'F', 'F', 'e', '_', 'l']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 29 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_30(self):
        board = [['c', '_', 'd', 'B', 'B', 'B'],
                 ['c', '_', 'd', 'e', '_', '_'],
                 ['c', 'A', 'A', 'e', '_', '_'],
                 ['I', 'I', 'J', 'J', '_', 'f'],
                 ['_', '_', '_', '_', '_', 'f'],
                 ['G', 'G', 'H', 'H', '_', 'f']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 30 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    # Expert

    def test_31(self):
        board = [['J', 'J', '_', 'C', 'C', 'C'],
                 ['_', '_', '_', 'i', 'H', 'H'],
                 ['b', 'A', 'A', 'i', '_', 'g'],
                 ['b', '_', 'e', 'F', 'F', 'g'],
                 ['K', 'K', 'e', '_', '_', 'g'],
                 ['_', '_', 'e', 'D', 'D', 'D']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 31 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_32(self):
        board = [['H', 'H', 'k', 'l', 'I', 'I'],
                 ['_', '_', 'k', 'l', '_', '_'],
                 ['A', 'A', 'k', '_', '_', '_'],
                 ['b', 'E', 'E', 'F', 'F', 'd'],
                 ['b', '_', '_', 'c', '_', 'd'],
                 ['G', 'G', '_', 'c', '_', 'd']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 32 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_33(self):
        board = [['_', 'b', 'k', '_', 'L', 'L'],
                 ['_', 'b', 'k', '_', '_', '_'],
                 ['A', 'A', 'k', '_', '_', '_'],
                 ['c', 'D', 'D', 'G', 'G', 'j'],
                 ['c', 'E', 'E', 'h', 'i', 'j'],
                 ['F', 'F', 'F', 'h', 'i', 'j']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 33 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_34(self):
        board = [['b', '_', '_', 'E', 'E', 'E'],
                 ['b', '_', '_', 'f', '_', 'd'],
                 ['A', 'A', '_', 'f', 'g', 'd'],
                 ['C', 'C', 'C', 'i', 'g', 'd'],
                 ['_', '_', 'n', 'i', 'J', 'J'],
                 ['M', 'M', 'n', 'K', 'K', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 34 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_35(self):
        board = [['_', '_', 'g', 'J', 'J', 'i'],
                 ['_', '_', 'g', 'd', '_', 'i'],
                 ['A', 'A', 'g', 'd', '_', 'i'],
                 ['c', 'F', 'F', 'F', '_', '_'],
                 ['c', 'E', 'E', 'h', 'k', '_'],
                 ['B', 'B', '_', 'h', 'k', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 35 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_36(self):
        board = [['c', 'B', 'B', 'B', 'L', 'L'],
                 ['c', 'k', 'J', 'J', '_', 'd'],
                 ['c', 'k', 'A', 'A', '_', 'd'],
                 ['E', 'E', 'E', 'h', '_', 'd'],
                 ['_', '_', 'g', 'h', 'I', 'I'],
                 ['F', 'F', 'g', '_', '_', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 36 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_37(self):
        board = [['D', 'D', 'l', '_', 'K', 'K'],
                 ['C', 'C', 'l', '_', 'i', 'j'],
                 ['e', 'A', 'A', '_', 'i', 'j'],
                 ['e', 'B', 'B', 'B', 'i', 'j'],
                 ['e', '_', '_', 'm', 'H', 'H'],
                 ['F', 'F', '_', 'm', 'G', 'G']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 37 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_38(self):
        board = [['b', '_', '_', 'F', 'F', 'F'],
                 ['b', 'E', 'E', 'd', '_', '_'],
                 ['A', 'A', 'c', 'd', '_', 'g'],
                 ['_', '_', 'c', 'I', 'I', 'g'],
                 ['_', '_', 'j', 'H', 'H', 'g'],
                 ['_', '_', 'j', 'K', 'K', 'K']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 38 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_39(self):
        board = [['_', '_', 'i', 'H', 'H', 'H'],
                 ['_', '_', 'i', 'k', '_', '_'],
                 ['A', 'A', 'j', 'k', '_', 'g'],
                 ['B', 'B', 'j', 'L', 'L', 'g'],
                 ['c', 'd', 'F', 'F', '_', 'g'],
                 ['c', 'd', 'E', 'E', '_', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 39 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here

    def test_40(self):
        board = [['c', 'L', 'L', '_', 'm', '_'],
                 ['c', 'j', 'k', '_', 'm', 'd'],
                 ['c', 'j', 'k', 'A', 'A', 'd'],
                 ['B', 'B', 'B', 'i', '_', 'd'],
                 ['_', '_', 'h', 'i', 'E', 'E'],
                 ['G', 'G', 'h', 'F', 'F', '_']]
        begin = time.perf_counter()

        AI.solve(board)

        end = time.perf_counter()
        print(f"Case 40 in {end - begin:0.4f} seconds")
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

class TicTacToeGame:

    def __init__(self):
        self.matrix = [['0'] * 3 for _ in range(3)]
        self._step_flag = 1
        self.check_game = True


    def __iter__(self):
        return self


    def __next__(self, coords):
        if self.check_game:
            if self._step_flag > 2:
                self._step_flag = 1

            self.print_matrix()

            turn = [int(elem) for elem in coords.split()]

            self._step(turn[0], turn[1], self._step_flag)

            if self._check_winner():
                self.print_matrix()
                print("Победил игрок", self._step_flag)
                self.check_game = False

            self._step_flag += 1
        else:
            raise StopIteration


    def _step(self, x, y, elem):
        if self.matrix[x][y] == '0':
            self.matrix[x][y] = elem
            return True
        self._step_flag -= 1
        return False


    def print_matrix(self):
        print()
        symbols = {'0': '⬛', '1': '❌', '2': '⭕'}
        for row in self.matrix:
            print(" ".join(symbols[str(elem)] for elem in row))
        print()


    def _check_winner(self):
        return (
            self._check_row(self.matrix, self._step_flag) or
            self._check_row(self._rotate_matrix(self.matrix), self._step_flag) or
            self._check_diagonal(self.matrix, self._step_flag) or
            self._check_diagonal(self._rotate_matrix(self.matrix), self._step_flag)
        )


    @staticmethod
    def _check_row(matrix, step_flag):
        for row in matrix:
            if all(elem == step_flag for elem in row):
                return True
        return False


    @staticmethod
    def _check_diagonal(matrix, step_flag):
        return all(matrix[i][i] == step_flag for i in range(3))


    @staticmethod
    def _rotate_matrix(matrix):
        size = len(matrix)
        return [[matrix[j][size - 1 - i] for j in range(size)] for i in range(size)]


my_game = TicTacToeGame()

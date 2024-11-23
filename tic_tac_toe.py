class TicTacToeGame:

    def __init__(self):
        self.matrix = [['0'] * 3 for _ in range(3)]
        self.step_flag = 1
        self._start_game()


    def _start_game(self):
        while True:
            if self.step_flag > 2:
                self.step_flag = 1

            self.print_matrix()

            try:
                turn = [int(elem) for elem in input(f"Ход игрока {self.step_flag} (введите x y): ").split()]

                if len(turn) != 2 or not (0 <= turn[0] < 3 and 0 <= turn[1] < 3):
                    raise ValueError("Некорректный ввод. Введите два числа от 0 до 2 через пробел.")
                
            except ValueError as e:
                print(e)
                continue

            if not self.step(turn[0], turn[1], self.step_flag):
                print("Эта ячейка уже занята, попробуйте снова.")
                continue

            if self.check_winner():
                self.print_matrix()
                print("Победил игрок", self.step_flag)
                break

            self.step_flag += 1


    def step(self, x, y, elem):
        if self.matrix[x][y] == '0':
            self.matrix[x][y] = elem
            return True
        return False


    def print_matrix(self):
        print()
        symbols = {'0': '⬛', '1': '❌', '2': '⭕'}
        for row in self.matrix:
            print(" ".join(symbols[str(elem)] for elem in row))
        print()


    def check_winner(self):
        return (
            self._check_row(self.matrix, self.step_flag) or
            self._check_row(self._rotate_matrix(self.matrix), self.step_flag) or
            self._check_diagonal(self.matrix, self.step_flag) or
            self._check_diagonal(self._rotate_matrix(self.matrix), self.step_flag)
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

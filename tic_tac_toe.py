class Tic_tac_toe_Game():

    matrix = [['0'] * 3 for i in range(3)]
    
    def __init__(self):
        self._start_game()


    def _start_game(self):
        self.step_flag = 1
        while True:
            if self.step_flag > 2:
                self.step_flag = 1

            print()
            self.print_matrix()
            print()
            
            turn =  [int(elem) for elem in input().split()]
            
            self.step(turn[0], turn[1], self.step_flag)
            self.step_flag += 1

            self.check_winner()


    def step(self, x, y, elem):
        if self.check_block(x, y):
            self.matrix[x][y] = elem
        else:
            self.step_flag -= 1


    def check_block(self, x, y):
        if str(self.matrix[x][y]) == '0':
            return True
        return False
    

    def print_matrix(self):
        for row in self.matrix:
            new_row = []
            for elem in row:
                
                match str(elem):   
                    case '0':
                        new_row.append('⬛')
                    case '1':
                        new_row.append('❌')
                    case '2':
                        new_row.append('⭕')
            
            print(*new_row)
            new_row.clear()


    def check_winner(self):
        print(self.matrix)

my_game = Tic_tac_toe_Game()

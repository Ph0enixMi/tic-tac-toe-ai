class SuperPuperDuperNewGame():
    matrix = [['0'] * 3 for i in range(3)]
    
    def __init__(self):
        self._start_game()


    def _start_game(self):
        while True:
            print()
            self.print_matrix()
            print()
            
            turn =  [int(elem) for elem in input().split()]
            
            self.step(turn[0], turn[1], turn[2])
        
        self.print_matrix()


    def step(self, x, y, elem):
        if self.check_block(x, y):
            self.matrix[x][y] = elem
    
    
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


my_game = SuperPuperDuperNewGame()

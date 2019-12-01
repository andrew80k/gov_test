import argparse

class Chess(object):
    def __init__(self):
        self.idx_max = 8
        char = "a"
        i = ord(char[0])
        self.board = [[chr(i+x-1)+str(y) for x in range(1,9)] for y in range(1,9)]
        self.pieces = ["king","queen","rook","knight","bishop","pawn"]

    def _get_index(self,inp):
        for x in range(self.idx_max):
            for y in range(self.idx_max):
                if self.board[x][y] == inp:
                    return (x,y)
        return None
    def validate(self,piece,start_pos):
        if piece == "queen":
            valid_list = self._queen(start_pos)
        elif piece == "rook":
            valid_list = self._rook(start_pos)
        elif piece == "knight":
            valid_list = self._knight(start_pos)
        elif piece in self.pieces:
            print("That piece is unimplemented.")
        else:
            "Invalid piece."
        return valid_list

    def _queen(self,start_pos):
        start_idx = self._get_index(start_pos)
        print(start_idx)
        # covers both rows.
        x_list = [ self.board[start_idx[0]][i] for i in range(self.idx_max) ]
        y_list = [ self.board[i][start_idx[1]] for i in range(self.idx_max) ]
        d_list = []
        # Diagonal
        j = start_idx[0] + 1
        k = start_idx[1] + 1
        while j < self.idx_max and k < self.idx_max:
            d_list.append(self.board[j][k])
            j += 1
            k += 1
        j = start_idx[0] - 1
        k = start_idx[1] - 1
        while j >= 0 and k >= 0:
            d_list.append(self.board[j][k])
            j -= 1
            k -= 1

        j = start_idx[0] + 1
        k = start_idx[1] - 1
        while j < self.idx_max and k >= 0:
            d_list.append(self.board[j][k])
            j += 1
            k -= 1

        j = start_idx[0] - 1
        k = start_idx[1] + 1
        while j >= 0 and k < self.idx_max:
            d_list.append(self.board[j][k])
            j -= 1
            k += 1

        l_list = x_list + y_list + d_list
        return l_list

    def _rook(self,start_pos):
        start_idx = self._get_index(start_pos)
        # covers both rows.
        x_list = [ self.board[start_idx[0]][i] for i in range(self.idx_max) ]
        y_list = [ self.board[i][start_idx[1]] for i in range(self.idx_max) ] 
        l_list = x_list + y_list
        return l_list

    def _knight(self,start_pos):
        start_idx = self._get_index(start_pos)
        x = start_idx[0]
        y = start_idx[1]
        pos = []
        l_list = []
        # enumerate all possibilities
        pos.append(( x + 2, y + 1 )) 
        pos.append(( x + 2, y - 1 ))
        pos.append(( x - 2, y + 1 ))
        pos.append(( x - 2, y - 1 ))
        pos.append(( x + 1, y + 2 ))
        pos.append(( x + 1, y - 2 ))
        pos.append(( x - 1, y + 2 ))
        pos.append(( x - 1, y - 2 ))
        
        for i in range(8):
            if pos[i][0] < self.idx_max and pos[i][0] >= 0 and pos[i][1] < self.idx_max and pos[i][1] >= 0:
                l_list.append(self.board[pos[i][0]][pos[i][1]])
        return l_list

if __name__ == "__main__":
    c = Chess()
    print(c.validate("queen","g5"))
    print(c.validate("rook","c3"))
    print(c.validate("knight","b6"))
    
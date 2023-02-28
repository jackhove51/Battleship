from tkinter import *

class Player:

    def __init__(self):
        self.ships = {"Destroyer": 2, "Submarine": 3, "Cruiser": 3, "Battleship": 4, "Carrier": 5}
        self.board = Tk()
        cell_width = 50
        cell_height = 50
        font_size = ("Arial", 24)
        cells = []
        for i in range(11):
            row = []
            for j in range(11):
                cell = Canvas(self.board, width=cell_width, height=cell_height, borderwidth=1, relief="solid")
                row.append(cell)
                if i == 0 and j != 0:
                    label = Label(self.board, text=str(j), font=font_size)
                    label.grid(row=i, column=j)
                elif j == 0 and i != 0:
                    label = Label(self.board, text = chr(i+64), font=font_size)
                    label.grid(row=i, column=j)
                cell.grid(row=i, column=j)
            cells.append(row)
        self.board.mainloop()

    def print_board(self):
        print(self.board)

if __name__ == "__main__":
    player1 = Player()
    player1.print_board()

from cgitb import grey
import tkinter as tk
from tkinter import ttk
from asyncio import isfuture
from audioop import minmax
from tkinter import font
from nbformat import read
import numpy as np
from sympy import true

playerTurn = True
pickBlock = False

n = np.ones((3,3))
n[0][1] = 3
n[2][1] = 2

buttons = []

def isGameOver(k, array, pos):
    if(pos[0] > 0):
        if(array[pos[0]-1][pos[1]] == 1):
            return 0
        if(pos[1] > 0):
            if(array[pos[0]-1][pos[1]] == 1):
                return 0
        if(pos[1] < k - 1):
            if(array[pos[0]-1][pos[1]+1] == 1):
                return 0

    if(pos[0] < k - 1):
        if(array[pos[0]+1][pos[1]] == 1):
            return 0
        if(pos[1] > 0):
            if(array[pos[0]+1][pos[1]-1] == 1):
                return 0
        if(pos[1] < k - 1):
            if(array[pos[0]+1][pos[1]+1] == 1):
                return 0

    if(pos[1] > 0):
        if(array[pos[0]][pos[1]-1] == 1):
            return 0
    
    if(pos[1] < k - 1):
        if(array[pos[0]][pos[1]+1] == 1):
            return 0

    if(array[pos[0]][pos[1]] == 3):
        return -100
    else:
        return 100

def isFree(k, array, pos):
    if(pos[0] < 0 or pos[1] < 0 or pos[0] > k-1 or pos[1] > k-1):
        return False

    if(array[pos[0]][pos[1]] == 1):
        return True
    else:
        return False

def posPlayer(k, array):
    pos = (0,0)
    for i in range(k):
        for j in range(k):
            if(array[i][j] == 2):
                return (i, j)
    return pos
def posBot(k, array):
    pos = (0,0)
    for i in range(k):
        for j in range(k):
            if(array[i][j] == 3):
                return (i, j)

def minimax(k, array, isMax):
    
    
    dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    pos = (0,0)
    pos_block = (0,0)
    turn = 2
    bestScore = 0
    bestMove = (-1,-1)
    bestBlock = (-1,-1)
    
    if(isMax):
        pos = posBot(k,array)
        turn = 3
        bestScore = -100
    else:
        pos = posPlayer(k,array)
        bestScore = 100

    result = ((0,0),(0,0),0)
    if(isGameOver(k, array, pos) != 0):
        return ((-1,-1), (-1,-1), isGameOver(k, array, pos),(-1,-1))

    for (x,y) in dir:
        pos_new = (pos[0]+x, pos[1]+y)
        if(isFree(k,array,pos_new)):
            array[pos_new[0]][pos_new[1]] = turn
            array[pos[0]][pos[1]] = 1
        else:
            continue

        for i in range(k):
            for j in range(k):
                pos_block = (i,j)

                if(isFree(k,array,pos_block)):
                    array[pos_block[0]][pos_block[1]] = 0
                else:
                    continue
                
                result = minimax(k,array, not isMax)
                array[pos_block[0]][pos_block[1]] = 1
                if(isMax):
                    if(result[2] > bestScore):
                        bestScore = result[2]
                        bestMove = pos_new
                        bestBlock = pos_block
                    elif(bestMove[0] == -1):
                        bestScore = result[2]
                        bestMove = pos_new
                        bestBlock = pos_block
                else:
                    if(result[2] < bestScore):
                        bestScore = result[2]
                        bestMove = pos_new
        array[pos_new[0]][pos_new[1]] = 1
        array[pos[0]][pos[1]] = turn
    return (bestMove,bestBlock, bestScore,pos)


def game(self):
    self.create_widgets()

    result = minimax(3,n,True)
    index = rem_bot()
    n[int(index/3)][index%3] = 1

    #coloring chosen buttons
    buttons[result[0][0]*3+result[0][1]].config(bg='red')
    n[result[0][0]][result[0][1]] = 3
    buttons[result[1][0]*3+result[1][1]].config(bg='black')
    n[result[1][0]][result[1][1]] = 0

def game2(self):
    self.create_widgets()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200')
        # configure the grid
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        frame = tk.Frame(self)
        frame.pack

        m1 = tk.Button(self, text="bot start", command=lambda: game(self))
        m2 = tk.Button(self, text="player", command=lambda: game2(self))

        m1.grid(row=0,column=1)
        m2.grid(row=2,column=1)
    


    def create_widgets(self):
       
        b1 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'grey', command=lambda: button_click(b1,1))
        b2 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'red', command=lambda: button_click(b2,2))
        b3 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'grey', command=lambda: button_click(b3,3))

        b4 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'grey', command=lambda: button_click(b4,4))
        b5 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'grey', command=lambda: button_click(b5,5))
        b6 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'grey', command=lambda: button_click(b6,6))

        b7 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'grey', command=lambda: button_click(b7,7))
        b8 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'green', command=lambda: button_click(b8,8))
        b9 = tk.Button(self, width=3, text=" ", font=("Helvetica", 20), bg = 'grey', command=lambda: button_click(b9,9))

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

        buttons.append(b1)
        buttons.append(b2)
        buttons.append(b3)
        buttons.append(b4)
        buttons.append(b5)
        buttons.append(b6)
        buttons.append(b7)
        buttons.append(b8)
        buttons.append(b9)

def rem_player():
    for i in range(9):
        if(buttons[i]['bg'] == 'green'):
            buttons[i].config(bg='grey')
            return i

def rem_bot():
    for i in range(9):
        if(buttons[i]['bg'] == 'red'):
            buttons[i].config(bg='grey')
            return i



def button_click(b, sorsz):
    global playerTurn,pickBlock
    sorsz-=1
    if(b['bg'] == 'grey' and playerTurn==True):
        index = rem_player()

        #freeing previous spot
        #moveing player 
        n[int(index/3)][index%3] = 1
        n[int(sorsz/3)][sorsz%3] = 2

        #coloring players button
        b.config(bg='green')

        playerTurn = False
        pickBlock = True

    elif(b['bg'] == 'grey' and pickBlock==True):
            
        #putting block on chosen button
        n[int(sorsz/3)][sorsz%3] = 0
        b.config(bg='black')

        #calculating bot's next move
        result = minimax(3,n,True)
        if(result[0][0] == -1):
            print(result)
            print("Player Wins!")
            return 

        #freeing previous block
        index = rem_bot()
        n[int(index/3)][index%3] = 1

        #coloring chosen buttons
        buttons[result[0][0]*3+result[0][1]].config(bg='red')
        n[result[0][0]][result[0][1]] = 3
        buttons[result[1][0]*3+result[1][1]].config(bg='black')
        n[result[1][0]][result[1][1]] = 0

        if(isGameOver(3,n,posPlayer(3,n)) == 100):
            print("Bot Wins!")
            return
        pickBlock = False
        playerTurn = True

        
    else:
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
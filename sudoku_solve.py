import numpy as np

sudoku = [
    [7,5,4,0,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,0,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,0,0,5,0,9,3,0],
    [9,0,0,0,6,0,0,0,5],
    [0,0,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,0,2,0,0,0,0,7]
]

sudoku = np.array(sudoku)

def valid(y,x,n):
    global sudoku

    for k in range(len(sudoku)):
        if sudoku[y][k] == n or sudoku[k][x] == n:
            return False
    
    y_box = (y//3)*3
    x_box = (x//3)*3

    for ysq in range(y_box,y_box+3):
        for xsq in range(x_box,x_box+3):
            if sudoku[ysq][xsq] == n:
                return False
    
    return True



def find_empty():
    global sudoku
    for y in range(len(sudoku)):
        for x in range(len(sudoku[0])):
            if sudoku[y][x] == 0 :
                return(y,x)
    
    return False

def solve():
    global sudoku

    kor = find_empty()

    if kor != False :
        y = kor[0]
        x = kor[1]

        for n in range(1,10):
            if valid(y, x, n):
                sudoku[y][x] = n
                solve()
                sudoku[y][x] = 0
    else : 
        print(sudoku)

if __name__ == "__main__":
    solve()




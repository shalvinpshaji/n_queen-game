def can_place(board, r, c):
    # Row check
    if sum(board[r]):
        return False
    #Column check
    for i in range(len(board[0])):
        if board[i][c] == 1:
            return False
    col = c
    row = r
    # Top left diagonal
    while col > 0 and row > 0:
        if board[row][col]:
            return False
        col -= 1
        row -= 1
    row = r
    col = c
    # Top right diagonal
    while row > 0 and col < len(board[0]):
        if board[row][col]:
            return False
        col += 1
        row -= 1
    row = r
    col = c
    # Bottom right diagonal
    while row < len(board) and col < len(board[0]):
        if board[row][col]:
            return False
        row += 1
        col += 1
    # Bottom left diagonal
    row = r
    col = c
    while row < len(board) and col > 0:
        if board[row][col]:
            return False
        row += 1
        col -= 1
    return True


def printboard(board):
    print('   ', end='')
    for i in range(len(board[0])):
        print(f'  {i + 1}  ',end='')
    print()
    for i,row in enumerate(board):
        print('   ', end='')
        print('-----' * (len(board)))
        print(f' {i+1} ', end='')
        for element in row:
            if element:
                print("| Q |", end='')
            else:
                print("| * |", end='')
        print()
    print('   ', end='')
    print('-----' * (len(board)))




def place(board, i, j):
    board[i][j] = 1
    return board

def visualizer(board, i,j):
    before = [k[:] for k in board]
    after = [k[:] for k in board]
    after = place(after, i, j)
    printboard(before)
    printboard(after)

def test(row, col):
    l = []
    for i in range(4):
        l.append([0,0,0,0])
    place(l,0,1)
    place(l,1,3)
    visualizer(l, row, col)
    print(can_place(l, row, col))


def play(board,i, j, p):
    if can_place(board, i, j):
        board = place(board, i ,j)
        print(f"Placed at ({i+1} {j+1})")
        return board,p+1
    else:
        print("Not valid Try again ")
        return board,p

def main(n):
    board = []
    p = 0
    for i in range(n):
        board.append([0]*n) 
    while p < len(board):
        printboard(board)
        try:
            i, j = map(int, input().split())
            if i <= n and j <= n:
                board, p = play(board, i-1, j-1, p)
            else:
                print("Slot number must be less than {}".format(n))
        except ValueError:
            print("Not valid Try again ")
    printboard(board)


if __name__ == "__main__":
    while True:
        try:
            i = input("Difficulty Level : ")
            i = int(i)
            i = 9 if i > 9 else i
            break
        except ValueError:
            print("Invalid input")

    main(i)


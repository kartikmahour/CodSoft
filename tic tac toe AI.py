import pygame
import sys
import math

# Constants for representing the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = None

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 300, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Fonts
FONT = pygame.font.SysFont('comicsans', 40)

# Function to draw the grid lines
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(WIN, BLACK, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), 3)
        pygame.draw.line(WIN, BLACK, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), 3)

# Function to draw the X's and O's
def draw_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == PLAYER_X:
                pygame.draw.line(WIN, BLACK, (j * WIDTH // 3 + 20, i * HEIGHT // 3 + 20), 
                                 ((j + 1) * WIDTH // 3 - 20, (i + 1) * HEIGHT // 3 - 20), 5)
                pygame.draw.line(WIN, BLACK, ((j + 1) * WIDTH // 3 - 20, i * HEIGHT // 3 + 20), 
                                 (j * WIDTH // 3 + 20, (i + 1) * HEIGHT // 3 - 20), 5)
            elif board[i][j] == PLAYER_O:
                pygame.draw.circle(WIN, BLUE, (j * WIDTH // 3 + WIDTH // 6, i * HEIGHT // 3 + HEIGHT // 6), HEIGHT // 6 - 20, 5)

# Function to check if the game is over
def game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    # Check for a draw
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return "DRAW"
    
    return None

# Function for Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    result = game_over(board)
    if result is not None:
        if result == PLAYER_X:
            return 1
        elif result == PLAYER_O:
            return -1
        else:
            return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth+1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth+1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player
def best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Main function to play the game
def main():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    turn = PLAYER_O
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == PLAYER_O:
                    x, y = pygame.mouse.get_pos()
                    row = y // (HEIGHT // 3)
                    col = x // (WIDTH // 3)
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_O
                        turn = PLAYER_X

        if turn == PLAYER_X:
            if game_over(board) is None:
                row, col = best_move(board)
                board[row][col] = PLAYER_X
                turn = PLAYER_O

        WIN.fill(WHITE)
        draw_grid()
        draw_board(board)
        pygame.display.update()

        result = game_over(board)
        if result is not None:
            if result == "DRAW":
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            running = False
            pygame.time.wait(2000)

if __name__ == "__main__":
    main()

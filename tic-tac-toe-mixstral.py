import pygame
import sys
import random

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.font = pygame.font.Font(None, 36)
        self.line_color = (255, 255, 255)  # Color for grid lines
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.minimax_depth = 5 
        self.player1_name = ''
        self.player2_name = ''
        self.restart()

    def restart(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.player1_name = self.get_input('Player 1 Name: ')
        self.player2_name = self.get_input('Player 2 Name: ')

    def get_input(self, prompt):
        input_box = pygame.Rect(100, 200, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill((30, 30, 30))
            txt_surface = self.font.render(prompt, True, (255, 255, 255))
            self.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(self.screen, color, input_box, 2)
            text_surface = self.font.render(text, True, color)
            self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
            pygame.display.flip()

        return text

    def click(self, i, j):
        if self.board[i][j] == ' ' and self.winner is None:
            self.board[i][j] = self.current_player
            self.check_game_over()
            if self.winner is None:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.ai_move()

    def ai_move(self):
        best_score = -2
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        self.board[best_move[0]][best_move[1]] = 'O'
        self.current_player = 'X'
        self.check_game_over()

    def minimax(self, board, depth, is_maximizing):
        result = self.check_win()
        if result is not None:
            return 1 if result == 'O' else -1  # AI wins = +1, Human wins = -1

        if depth == self.minimax_depth or self.is_draw():
            return 0  # Limit depth or it's a draw

        if is_maximizing:
            best_score = -2
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        best_score = max(best_score, score)
            return best_score

        else:
            best_score = 2
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        best_score = min(best_score, score)
            return best_score
    def check_win(self):
            # Check rows, columns, and diagonals 
            for row in self.board:
                if len(set(row)) == 1 and row[0] != ' ':
                    return row[0]  # Row win

            for col in range(3):
                if len(set([self.board[i][col] for i in range(3)])) == 1 and self.board[0][col] != ' ':
                    return self.board[0][col]  # Column win

            # Check diagonals
            if len(set([self.board[i][i] for i in range(3)])) == 1 and self.board[0][0] != ' ':
                return self.board[0][0]  # Main diagonal win
            if len(set([self.board[i][2 - i] for i in range(3)])) == 1 and self.board[0][2] != ' ':
                return self.board[0][2]  # Other diagonal win

            # Check for draw (all cells filled)
            for row in self.board:
                if ' ' in row:
                    return None  # Game not over

            return 'Draw'  # No winner, all cells filled 

    def draw_board(self):
        # Draw grid lines
        pygame.draw.line(self.screen, self.line_color, (213, 0), (213, 480), 3)
        pygame.draw.line(self.screen, self.line_color, (426, 0), (426, 480), 3)
        pygame.draw.line(self.screen, self.line_color, (0, 160), (640, 160), 3)
        pygame.draw.line(self.screen, self.line_color, (0, 320), (640, 320), 3)

        # Draw X's and O's
        for row in range(3):
            for col in range(3):
                if self.board[row][col] != ' ':
                    text = self.font.render(self.board[row][col], True, self.line_color)
                    text_rect = text.get_rect(center=(col * 213 + 107, row * 160 + 80))
                    self.screen.blit(text, text_rect)


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // 160
                    col = pos[0] // 213
                    self.click(row, col)

            self.screen.fill((0, 0, 0))  # Clear the screen
            self.draw_board()

            if self.winner:
                self.show_game_over(self.winner)
            elif self.is_draw():
                self.show_game_over('Draw')

            pygame.display.flip()

    def show_game_over(self, result):
        text = f"{result} wins!" if result != 'Draw' else "It's a draw!"
        text_surface = self.font.render(text, True, self.line_color)
        text_rect = text_surface.get_rect(center=(320, 240))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Pause before restart
        self.restart()

if __name__ == '__main__':
    game = TicTacToe()
    game.run()
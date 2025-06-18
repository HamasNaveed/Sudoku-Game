import pygame
import requests

# Initialize pygame
pygame.init()

# Constants
Width, Height = 600, 600
Grid = 9
Cell_Size = Width // Grid
LINE_COLOR = (0, 0, 0)  # Black
BG_COLOR = (255, 255, 255)  # White
TEXT_COLOR = (0, 0, 255)  # Blue for numbers
SELECTED_COLOR = (200, 200, 200)

# Create the window
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Sudoku Game")

# Load font
font = pygame.font.Font(None, 40)  # Default font, size 40

# Define the Sudoku board
original_board = []
solved_board = []
selected_cell = None
small_font = pygame.font.Font(None, 25)  # Smaller font size

def draw_text(text, x, y, color=(0, 0, 0), font=small_font):
    """Helper function to draw text on screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_menu():
    """Displays the main game menu."""
    screen.fill((0,0,0))  # Set the background color to black
    
    draw_text("Select Difficulty", Width // 4, 100, (255, 255, 255))  # White text
    draw_text("1 - Easy", Width // 4, 200, (0, 255, 0))  # Green text
    draw_text("2 - Medium", Width // 4, 250, (0, 0, 255))  # Blue text
    draw_text("3 - Hard", Width // 4, 300, (255, 0, 0))  # Red text
    draw_text("4 - Expert", Width // 4, 350, (255, 0, 255))  # Magenta text
    draw_text("Press 'I' for Instructions", Width // 4, 450, (255, 255, 255))  # White text
    
    pygame.display.flip()

def draw_instructions():
    """Displays the instructions and rules of the game."""
    screen.fill((0, 0, 0))  # Set background to black

    text_far = 9  # Adjust this value to move text horizontally
    start_y = 60  # Starting y position
    spacing = 35  # Line spacing

    draw_text("Sudoku Rules and Instructions!!", Width // text_far, start_y, (255, 0, 0))
    draw_text("1. Fill in the grid with numbers 1-9.", Width // text_far, start_y + spacing, (255, 0, 0))
    draw_text("2. Each number can appear only once in each row,", Width // text_far, start_y + 2 * spacing, (255, 0, 0))
    draw_text("   column, and 3x3 box.", Width // text_far, start_y + 3 * spacing, (255, 0, 0))
    draw_text("3. Use the mouse to select a cell and the keyboard", Width // text_far, start_y + 4 * spacing, (255, 0, 0))
    draw_text("   to input the numbers.", Width // text_far, start_y + 5 * spacing, (255, 0, 0))
    draw_text("4. You have 3 lives, invalid moves decrease your lives.", Width // text_far, start_y + 6 * spacing, (255, 0, 0))
    draw_text("Game created by: Hamas Naveed", Width // text_far, start_y + 8 * spacing, (255, 0, 0))
    draw_text("Press 'B' to go back to Menu.", Width // text_far, start_y + 10 * spacing, (255, 255, 255))

    pygame.display.flip()

def fetch_sudoku(difficulty="medium"):
    """Fetches a new Sudoku puzzle from the API."""
    url = f"https://sudoku-api.vercel.app/api/dosuku?difficulty={difficulty}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["newboard"]["grids"][0]["value"], data["newboard"]["grids"][0]["solution"]
    else:
        print("Error fetching Sudoku")
        return [[0] * Grid for _ in range(Grid)], [[0] * Grid for _ in range(Grid)]  # Empty board if API fails

def draw_numbers():
    """Draws the numbers from the Sudoku board."""
    for row in range(Grid):
        for col in range(Grid):
            num = original_board[row][col]
            if num != 0:
                text_surface = font.render(str(num), True, TEXT_COLOR)
                text_rect = text_surface.get_rect(
                    center=(col * Cell_Size + Cell_Size // 2, row * Cell_Size + Cell_Size // 2)
                )
                screen.blit(text_surface, text_rect)

def draw_grid():
    """Draws the Sudoku grid."""
    screen.fill(BG_COLOR)

    if selected_cell:
        row, col = selected_cell
        pygame.draw.rect(screen, SELECTED_COLOR, (col * Cell_Size, row * Cell_Size, Cell_Size, Cell_Size))

    for i in range(Grid + 1):
        line_width = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, LINE_COLOR, (0, i * Cell_Size), (Width, i * Cell_Size), line_width)
        pygame.draw.line(screen, LINE_COLOR, (i * Cell_Size, 0), (i * Cell_Size, Height), line_width)

def get_cell_from_mouse(pos):
    """Gets the row and column from mouse click."""
    x, y = pos
    return y // Cell_Size, x // Cell_Size

def is_valid_move(row, col, num):
    """Checks if the move is valid based on the solved board."""
    return solved_board[row][col] == num

def menu():
    """Handles the game menu."""
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "easy"
                elif event.key == pygame.K_2:
                    return "medium"
                elif event.key == pygame.K_3:
                    return "hard"
                elif event.key == pygame.K_4:
                    return "expert"
                elif event.key == pygame.K_i:
                    instructions()

def instructions():
    """Handles the instructions screen."""
    while True:
        draw_instructions()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                return  # Return to menu


def show_message(text, duration=1500):  # Duration in milliseconds
    screen.fill((0, 0, 0))  # Black background
    draw_text(text, Width // 3, Height // 2, (255, 0 , 0), font)  # White text in center
    pygame.display.flip()
    pygame.time.delay(duration)  # Pause execution for `duration` milliseconds


def main():
    print ("Welcome to Suduko")
    global selected_cell, original_board, solved_board
    Total_Lives = 3
    Invalid_Text="Invalid Move"
    # Main Menu
    difficulty = menu()
    if difficulty is None:
        return
    
    original_board, solved_board = fetch_sudoku(difficulty)

    running = True
    while running:
        screen.fill(BG_COLOR)
        draw_grid()
        draw_numbers()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or Total_Lives == 0:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_cell = get_cell_from_mouse(event.pos)
            elif event.type == pygame.KEYDOWN and selected_cell:
                if event.unicode.isdigit():
                    num = int(event.unicode)
                    row, col = selected_cell
                    if original_board[row][col] == 0:
                        if is_valid_move(row, col, num):
                            original_board[row][col] = num
                        else:
                            print("Invalid move")
                            show_message(Invalid_Text)
                            Total_Lives -= 1

    pygame.quit()

main()

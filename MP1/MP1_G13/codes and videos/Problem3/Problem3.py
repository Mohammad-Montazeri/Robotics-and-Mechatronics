# Libraries
import pygame
import sys
import serial
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
FPS = 60  # Adjust the FPS for slower movement

# Colors
WHITE = (255, 255, 255)
GRAY = (181, 176, 173)
DARK_BLUE = (3, 102, 150)
MEDIUM_BLUE = (7, 87, 91)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)

# Initialize clock
clock = pygame.time.Clock()

# Initialize serial communication with Arduino
ser = serial.Serial("com3", 115200)


# Maze generation - DO NOT CHANGE THIS FUNCTION!
def generate_maze():
    maze = [[0] * COLS for _ in range(ROWS)]
    stack = []
    start_cell = (1, 1)
    end_cell = (ROWS - 3, COLS - 3)
    stack.append(start_cell)
    maze[start_cell[0]][start_cell[1]] = 1

    while stack:
        current_cell = stack[-1]
        neighbors = [
            (current_cell[0] - 2, current_cell[1]),
            (current_cell[0] + 2, current_cell[1]),
            (current_cell[0], current_cell[1] - 2),
            (current_cell[0], current_cell[1] + 2),
        ]
        unvisited_neighbors = [
            neighbor
            for neighbor in neighbors
            if 0 < neighbor[0] < ROWS - 1
            and 0 < neighbor[1] < COLS - 1
            and maze[neighbor[0]][neighbor[1]] == 0
        ]

        if unvisited_neighbors:
            chosen_neighbor = random.choice(unvisited_neighbors)
            maze[chosen_neighbor[0]][chosen_neighbor[1]] = 1
            maze[(chosen_neighbor[0] + current_cell[0]) // 2][
                (chosen_neighbor[1] + current_cell[1]) // 2
            ] = 1
            stack.append(chosen_neighbor)
        else:
            stack.pop()

    return maze, start_cell, end_cell


maze, start_point, end_point = generate_maze()

# Player position
player_row, player_col = start_point

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Read data from Arduino through serial communication
    data = ser.readline().decode().strip().split(",")
    if len(data) == 2:
        roll, pitch = map(float, ser.readline().decode().strip().split(","))
        # Map roll and pitch to player movement
        if 30 < roll < 170:
            if player_col > 0 and maze[player_row][player_col - 1] == 1:
                player_col -= 1
        elif -170 < roll < -30:
            if player_col < COLS - 1 and maze[player_row][player_col + 1] == 1:
                player_col += 1
        if 30 < pitch < 170:
            if player_row > 0 and maze[player_row - 1][player_col] == 1:
                player_row -= 1
        elif -170 < pitch < -30:
            if player_row < ROWS - 1 and maze[player_row + 1][player_col] == 1:
                player_row += 1

    # Draw maze
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    MEDIUM_BLUE,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) == start_point:
                pygame.draw.rect(
                    screen,
                    LIGHT_BLUE,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )
            elif (row, col) == end_point:
                pygame.draw.rect(
                    screen,
                    LIGHT_BLUE,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )

    # Draw player
    pygame.draw.circle(
        screen,
        GRAY,
        (
            player_col * CELL_SIZE + CELL_SIZE // 2,
            player_row * CELL_SIZE + CELL_SIZE // 2,
        ),
        CELL_SIZE // 3,
    )

    # Check if the player reaches the end point
    if (player_row, player_col) == end_point:
        pygame.display.flip()
        print("Congratulations! You reached the end of the maze.")
        time.sleep(5)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(FPS)

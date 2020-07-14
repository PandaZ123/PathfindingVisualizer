import pygame
import sys
import node
import kinter

columns = 20
rows = 20
WIDTH = 20  # width of each square
HEIGHT = 20  # height of each square
MARGIN = 5
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)


def heuristic(a, b):
    """ Returns the distance from point a to b
    """
    return abs(a.position[0] - b.position[0]) + abs(a.position[1] -
                                                    b.position[1])


def optimal_path(current):
    """ Returns the current optimal path
    """
    path = []
    temp = current
    path.append(temp)
    while temp.prev is not None:
        path.append(temp.prev)
        temp = temp.prev
    return path


def search(grid, open_set, closed_set, start, end, display):
    """ The main search algorithm to find the optimal path from start to finish

    :param grid: List[List[Node]]
    :param open_set: List[Node]
    :param closed_set: List[Node]
    :param start: Node
    :param end: Node
    :param display:
    :return: List[Node]
    """
    clock = pygame.time.Clock()
    while len(open_set) > 0:
        current_node = open_set[0]
        current_index = 0
        for index, node in enumerate(open_set):
            if node.f_score < current_node.f_score:
                current_node = node
                current_index = index

        if open_set[current_index] == end:
            path = optimal_path(current_node)
            break

        open_set.pop(current_index)
        closed_set.append(current_node)

        neighbors = current_node.neighbors
        for n in neighbors:
            if n not in closed_set and n.is_wall is False:
                temp_g = current_node.g_score + heuristic(n, current_node)
                if n in open_set:
                    if temp_g < n.g_score:
                        n.g_score = temp_g
                else:
                    n.g_score = temp_g
                    open_set.append(n)
                n.h_score = heuristic(n, end)
                n.f_score = n.g_score + n.h_score
                n.prev = current_node

        for node in open_set:
            node.draw(display, ORANGE, MARGIN, WIDTH, HEIGHT)
            start.draw(display, GREEN, MARGIN, WIDTH, HEIGHT)
            end.draw(display, RED, MARGIN, WIDTH, HEIGHT)

        for node in closed_set:
            node.draw(display, BLUE, MARGIN, WIDTH, HEIGHT)
            start.draw(display, GREEN, MARGIN, WIDTH, HEIGHT)
            end.draw(display, RED, MARGIN, WIDTH, HEIGHT)

        path = optimal_path(current_node)
        for node in path:
            node.draw(display, YELLOW, MARGIN, WIDTH, HEIGHT)
            start.draw(display, GREEN, MARGIN, WIDTH, HEIGHT)
            end.draw(display, RED, MARGIN, WIDTH, HEIGHT)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j].is_wall is True:
                    grid[i][j].draw(display, GRAY, MARGIN, WIDTH, HEIGHT)

        if len(open_set) == 0:
            pass
        else:
            # Display the open set nodes
            for node in open_set:
                node.draw(display, ORANGE, MARGIN, WIDTH, HEIGHT)
                start.draw(display, GREEN, MARGIN, WIDTH, HEIGHT)
                end.draw(display, RED, MARGIN, WIDTH, HEIGHT)

            # Display the closed set nodes
            for node in closed_set:
                node.draw(display, BLUE, MARGIN, WIDTH, HEIGHT)
                start.draw(display, GREEN, MARGIN, WIDTH, HEIGHT)
                end.draw(display, RED, MARGIN, WIDTH, HEIGHT)

            # Display the path nodes
            for node in path:
                node.draw(display, YELLOW, MARGIN, WIDTH, HEIGHT)
                start.draw(display, GREEN, MARGIN, WIDTH, HEIGHT)
                end.draw(display, RED, MARGIN, WIDTH, HEIGHT)

            # Display the walls
            for i in range(rows):
                for j in range(columns):
                    if grid[i][j].is_wall is True:
                        grid[i][j].draw(display, GRAY, MARGIN, WIDTH, HEIGHT)

        clock.tick(25)
        pygame.display.update()


def setup_grid(display):
    # Setup 2D array
    grid = [[0] * rows for _ in range(columns)]

    # Assign a node to each spot on grid
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = node.Node((i, j))

    # Add neighbors for each node
    for i in range(rows):
        for j in range(columns):
            grid[i][j].add_neighbors(grid, False, columns, rows)

    # Setup the GUI of grid
    for i in range(rows):
        for j in range(columns):
            color = (255, 255, 255)
            pygame.draw.rect(display, color,
                             [(MARGIN + WIDTH) * j + MARGIN,
                              (MARGIN + HEIGHT) * i + MARGIN,
                              WIDTH, HEIGHT])

    # Display walls
    for i in range(rows):
        for j in range(columns):
            if grid[i][j].is_wall is True:
                grid[i][j].draw(display, GRAY, MARGIN, WIDTH, HEIGHT)
    pygame.display.update()

    return grid


def main():
    """ Main method for the program
    """
    display = pygame.display.set_mode((columns * (HEIGHT + MARGIN),
                                       rows * (WIDTH + MARGIN)))
    grid = setup_grid(display)

    # Builds the setting menu for starting the search algorithm
    app = kinter.App()
    app.mainloop()
    end = app.end_coord
    start = app.start_coord
    start_algo = True
    start_coord_changed = app.start_coord_changed
    end_coord_changed = app.end_coord_changed
    yes_randomize = app.randomize

    if yes_randomize:
        grid = setup_grid(display)

    # Declare some variables
    open_set = []
    closed_set = []
    if start_coord_changed:
        start = grid[int(start[0])][int(start[1])]
        start_coord_changed = False
    else:
        start = grid[0][0]
    if end_coord_changed:
        end = grid[int(end[0])][int(end[1])]
        end_coord_changed = False
    else:
        end = grid[19][19]

    start.is_wall = False
    end.is_wall = False

    open_set.append(start)  # append starting node into open set

    for i in range(rows):
        for j in range(columns):
            color = (255, 255, 255)
            pygame.draw.rect(display, color,
                             [(MARGIN + WIDTH) * j + MARGIN,
                              (MARGIN + HEIGHT) * i + MARGIN,
                              WIDTH, HEIGHT])

    # Display walls
    for i in range(rows):
        for j in range(columns):
            if grid[i][j].is_wall is True:
                grid[i][j].draw(display, GRAY, MARGIN, WIDTH, HEIGHT)

    start.draw(display, GREEN, MARGIN, WIDTH, HEIGHT)
    end.draw(display, RED, MARGIN, WIDTH, HEIGHT)

    pygame.display.update()

    pygame.init()  # Initialize program
    running = True
    play_again = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                play_again = True

        if start_algo:
            search(grid, open_set, closed_set, start, end, display)
            start_algo = False
        if play_again:
            main()


if __name__ == '__main__':
    main()


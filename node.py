import pygame
import random


class Node:
    """ Node class
    """

    def __init__(self, position):
        """ Constructor for Node class

        :param position: Tuple[int]
        """
        self.position = position
        self.f_score = 0
        self.g_score = 0
        self.h_score = 0
        self.prev = None
        self.neighbors = []
        self.is_wall = False

        if random.randint(0, 3) == 1:
            self.is_wall = True

    def draw(self, display, color, margin, width, height):
        """Draws a rectangle onto the display given a certain color

        :param display:
        :param color:
        :param margin:
        :param width:
        :param height:
        :return:
        """
        pygame.draw.rect(display, color, [(margin + width) *
                                          self.position[0] + margin,
                                          (margin + height) *
                                          self.position[1] + margin,
                                          width, height])

    def add_neighbors(self, grid, diagonal, columns, rows):
        """Add adjacent nodes of current node self.neighbors

        :param grid:
        :param diagonal:
        :param columns:
        :param rows:
        :return:
        """
        i = self.position[0]
        j = self.position[1]
        if i < columns - 1:
            self.neighbors.append(grid[i + 1][j])
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
        if j < rows - 1:
            self.neighbors.append(grid[i][j + 1])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])
        if diagonal:
            if i < columns - 1 and j < rows - 1:
                self.neighbors.append(grid[i + 1][j + 1])
            if i < columns - 1 and j > 0:
                self.neighbors.append(grid[i + 1][j - 1])
            if i > 0 and j < rows - 1:
                self.neighbors.append(grid[i - 1][j + 1])
            if i > 0 and j > 0:
                self.neighbors.append(grid[i - 1][j - 1])

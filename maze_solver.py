import pygame
from collections import deque
import heapq
import time


CELL = 30
ROWS = 15
COLS = 20
WIDTH = COLS * CELL
HEIGHT = ROWS * CELL

FPS = 60
DELAY = 0.03


COLORS = {
    "wall": (30, 30, 30),
    "free": (230, 230, 230),
    "start": (0, 0, 255),
    "goal": (255, 0, 0),
    "visited": (100, 180, 255),
    "path": (0, 255, 0)
}


MAZE = [
    [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0],
    [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
    [1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],
    [1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

START = (0, 0)
GOAL = (14, 19)
DIRS = [(1,0), (-1,0), (0,1), (0,-1)]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver – DFS / BFS / A*")
clock = pygame.time.Clock()


def draw_grid(visited=set(), path=set()):
    for r in range(ROWS):
        for c in range(COLS):
            color = COLORS["wall"] if MAZE[r][c] else COLORS["free"]
            if (r, c) in visited:
                color = COLORS["visited"]
            if (r, c) in path:
                color = COLORS["path"]
            if (r, c) == START:
                color = COLORS["start"]
            if (r, c) == GOAL:
                color = COLORS["goal"]

            pygame.draw.rect(
                screen,
                color,
                (c*CELL, r*CELL, CELL, CELL)
            )
    pygame.display.flip()


def solve(algo):
    visited = set()
    came = {START: None}

    if algo == "dfs":
        frontier = [START]
    elif algo == "bfs":
        frontier = deque([START])
    else:
        frontier = []
        heapq.heappush(frontier, (0, START))

    while frontier:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if algo == "dfs":
            current = frontier.pop()
        elif algo == "bfs":
            current = frontier.popleft()
        else:
            _, current = heapq.heappop(frontier)

        if current == GOAL:
            break

        for dr, dc in DIRS:
            nr, nc = current[0] + dr, current[1] + dc
            nxt = (nr, nc)
            if 0 <= nr < ROWS and 0 <= nc < COLS and MAZE[nr][nc] == 0 and nxt not in came:
                frontier.append(nxt) if algo != "astar" else heapq.heappush(frontier, (heuristic(nxt, GOAL), nxt))
                came[nxt] = current
                visited.add(nxt)
                draw_grid(visited)
                time.sleep(DELAY)

  
    path = set()
    cur = GOAL
    while cur:
        path.add(cur)
        cur = came.get(cur)
        draw_grid(visited, path)
        time.sleep(DELAY)


def main():
    running = True
    visited, path = set(), set()

    while running:
        clock.tick(FPS)
        draw_grid(visited, path)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                visited.clear()
                path.clear()
                if event.key == pygame.K_d:
                    solve("dfs")
                if event.key == pygame.K_b:
                    solve("bfs")
                if event.key == pygame.K_a:
                    solve("astar")
                if event.key == pygame.K_r:
                    pass

    pygame.quit()

if __name__ == "__main__":
    main()
#!/usr/bin/env python

import sys


def main() -> None:
    puzzle = load_puzzle()

    start = find_start(puzzle)
    paths = bfs(puzzle, start)
    shortest_path = min([len(path) - 1 for path in paths])
    print(f'Part 1: {shortest_path}')

    shortest_path = sys.maxsize
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 'a':
                paths = list(bfs(puzzle, (i, j)))
                if not paths:
                    continue
                best_path = min([len(path) - 1 for path in paths])
                if best_path < shortest_path:
                    shortest_path = best_path
    print(f'Part 2: {shortest_path}')


def bfs(puzzle: list[list[str]], start: tuple[int, int]) -> None:
    queue = [[start]]
    seen = {start}

    while queue:
        path = queue.pop(0)
        y, x = path[-1]

        if puzzle[y][x] == 'E':
            yield path
            continue

        for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (new_y, new_x) in seen:
                continue
            if new_y < 0 or new_y >= len(puzzle) or new_x < 0 or new_x >= len(puzzle[new_y]):
                continue
            if get_value_from_letter(puzzle[new_y][new_x]) - get_value_from_letter(puzzle[y][x]) > 1:
                continue
            queue.append(path + [(new_y, new_x)])
            seen.add((new_y, new_x))


def get_value_from_letter(letter: str) -> int:
    if letter == 'S':
        letter = 'a'
    if letter == 'E':
        letter = 'z'
    return ord(letter)


def find_start(puzzle: list[list[str]]) -> tuple[int, int]:
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 'S':
                return (i, j)


def load_puzzle() -> list[str]:
    with open('day_12_input.txt') as f:
        return [list(line.rstrip()) for line in f.readlines()]


if __name__ == '__main__':
    main()

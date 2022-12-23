#!/usr/bin/env python

from dataclasses import dataclass
from enum import Enum, auto
import math


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


@dataclass
class Instruction():
    direction: Direction
    count: int


@dataclass
class Point():
    x: int
    y: int

    def __hash__(self):
        return hash(f'X={self.x}_Y={self.y}')


def main() -> None:
    puzzle_input = load_puzzle()
    instructions = load_instructions(puzzle_input)

    print(f'Part 1: {count_visited_tail_points(2, instructions)}')
    print(f'Part 2: {count_visited_tail_points(10, instructions)}')


def load_puzzle() -> list[str]:
    with open('day_09_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_instructions(puzzle_input: list[str]) -> list[Instruction]:
    instructions = []
    for line in puzzle_input:
        parts = line.split()
        direction_str = parts[0]
        count = int(parts[1])
        if direction_str == 'U':
            direction = Direction.UP
        elif direction_str == 'D':
            direction = Direction.DOWN
        elif direction_str == 'L':
            direction = Direction.LEFT
        elif direction_str == 'R':
            direction = Direction.RIGHT
        else:
            raise Exception('Invalid direction')
        instructions.append(Instruction(direction, count))
    return instructions


def step(knots: list[Point], direction: Direction):
    if direction == Direction.UP:
        knots[0].y -= 1
    elif direction == Direction.DOWN:
        knots[0].y += 1
    elif direction == Direction.LEFT:
        knots[0].x -= 1
    elif direction == Direction.RIGHT:
        knots[0].x += 1

    for i in range(len(knots) - 1):
        lead = knots[i]
        follow = knots[i + 1]

        x_diff = lead.x - follow.x
        y_diff = lead.y - follow.y

        if abs(x_diff) > 1 or abs(y_diff) > 1:
            if x_diff > 0:
                follow.x += 1
            elif x_diff < 0:
                follow.x -= 1

            if y_diff > 0:
                follow.y += 1
            elif y_diff < 0:
                follow.y -= 1


def count_visited_tail_points(knots: int, instructions: list[Instruction]) -> int:
    knot_list = [Point(0, 0) for _ in range(0, knots)]
    visited_tail_points = set()
    visited_tail_points.add(knot_list[-1])

    for instruction in instructions:
        for _ in range(instruction.count):
            step(knot_list, instruction.direction)
            visited_tail_points.add(knot_list[-1])

    return len(visited_tail_points)


if __name__ == '__main__':
    main()

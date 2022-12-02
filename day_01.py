#!/usr/bin/env python

def main() -> None:
    puzzle_input = load_puzzle()
    elves = load_elves_from_input(puzzle_input)
    elves.sort(reverse=True)
    print(f'Part 1: {elves[0]}')
    print(f'Part 2: {elves[0] + elves[1] + elves[2]}')


def load_puzzle() -> list[str]:
    with open('day_01_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_elves_from_input(puzzle_input) -> list[int]:
    elves = []
    elf = 0

    for line in puzzle_input:
        if line:
            elf = elf + int(line)
        else:
            elves.append(elf)
            elf = 0

    if elf:
        elves.append(elf)

    return elves


if __name__ == '__main__':
    main()

#!/usr/bin/env python


def main() -> None:
    puzzle_input = load_puzzle()

    print(f'Part 1: {find_start_of_packet_marker(puzzle_input[0])}')
    print(f'Part 2: {find_start_of_message_marker(puzzle_input[0])}')


def load_puzzle() -> list[str]:
    with open('day_06_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def find_start_of_packet_marker(puzzle_input: str) -> int:
    for i in range(0, len(puzzle_input) - 3):
        part = puzzle_input[i:i+4]
        if len(set(part)) == 4:
            return i + 4


def find_start_of_message_marker(puzzle_input: str) -> int:
    for i in range(0, len(puzzle_input) - 13):
        part = puzzle_input[i:i+14]
        if len(set(part)) == 14:
            return i + 14


if __name__ == '__main__':
    main()

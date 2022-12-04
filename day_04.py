#!/usr/bin/env python

from dataclasses import dataclass


@dataclass
class Elf:
    min_section: int
    max_section: int


@dataclass
class Pair:
    first: Elf
    second: Elf


def main() -> None:
    puzzle_input = load_puzzle()
    pairs = load_elf_pairs(puzzle_input)

    print(f'Part 1: {len(list(filter(does_one_contain_other, pairs)))}')
    print(f'Part 2: {len(list(filter(does_pair_overlap, pairs)))}')


def load_puzzle() -> list[str]:
    with open('day_04_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_elf_pairs(puzzle_input: list[str]) -> list[Pair]:
    pairs = []
    for line in puzzle_input:
        section_ranges = line.split(',')

        first_range = section_ranges[0].split('-')
        first = Elf(int(first_range[0]), int(first_range[1]))

        second_range = section_ranges[1].split('-')
        second = Elf(int(second_range[0]), int(second_range[1]))

        pairs.append(Pair(first, second))
    return pairs


def does_one_contain_other(pair: Pair) -> bool:
    if pair.first.min_section <= pair.second.min_section and pair.first.max_section >= pair.second.max_section:
        return True
    elif pair.second.min_section <= pair.first.min_section and pair.second.max_section >= pair.first.max_section:
        return True
    else:
        return False


def does_pair_overlap(pair: Pair) -> bool:
    if pair.first.min_section <= pair.second.min_section and pair.first.max_section >= pair.second.min_section:
        return True
    elif pair.second.min_section <= pair.first.min_section and pair.second.max_section >= pair.first.min_section:
        return True
    else:
        return False

if __name__ == '__main__':
    main()

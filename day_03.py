#!/usr/bin/env python


def main() -> None:
    puzzle_input = load_puzzle()

    rucksacks = load_rucksacks(puzzle_input)
    common_items = [find_common_item_in_rucksack(r[0], r[1]) for r in rucksacks]
    print(f'Part 1: {sum([get_item_score(i) for i in common_items])}')

    groups = load_groups(puzzle_input)
    common_items = [find_common_item_in_group(g[0], g[1], g[2]) for g in groups]
    print(f'Part 2: {sum([get_item_score(i) for i in common_items])}')


def load_puzzle() -> list[str]:
    with open('day_03_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_rucksacks(puzzle_input) -> list[tuple[list[str], list[str]]]:
    return [split_list(line) for line in puzzle_input]


def load_groups(puzzle_input) -> list[list[str]]:
    groups = []
    group = []
    for line in puzzle_input:
        group.append(line)
        if len(group) == 3:
            groups.append(group)
            group = []
    return groups


def split_list(l: list[str]) -> tuple[list[str], list[str]]:
    midpoint = len(l) // 2
    return l[:midpoint], l[midpoint:]


def find_common_item_in_rucksack(first_half: list[str], second_half: list[str]) -> str:
    return list(set(first_half).intersection(second_half))[0]


def find_common_item_in_group(first: list[str], second: list[str], third: list[str]) -> str:
    return list(set(first).intersection(second, third))[0]


def get_item_score(item: str) -> int:
    ord_value = ord(item)
    if ord_value >= ord('a') and ord_value <= ord('z'):
        return ord(item) - ord('a') + 1
    elif ord_value >= ord('A') and ord_value <= ord('Z'):
        return ord(item) - ord('A') + 27


if __name__ == '__main__':
    main()

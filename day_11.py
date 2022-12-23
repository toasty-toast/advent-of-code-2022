#!/usr/bin/env python

import re


class Monkey():
    items: list[int]
    operation: str
    divisor: int
    target_if_true: int
    target_if_false: int
    inspected_item_count: int

    def __init__(self):
        self.items = []
        self.operation = ''
        self.divisor = 1
        self.target_if_true = 0
        self.target_if_false = 0
        self.inspected_item_count = 0


def main() -> None:
    monkeys = load_monkeys()
    for _ in range(20):
        execute_round(monkeys, True)

    sorted_monkeys = sorted(monkeys, key=lambda m: m.inspected_item_count, reverse=True)
    print(f'Part 1: {sorted_monkeys[0].inspected_item_count * sorted_monkeys[1].inspected_item_count}')

    monkeys = load_monkeys()
    for _ in range(10000):
        execute_round(monkeys, False)

    sorted_monkeys = sorted(monkeys, key=lambda m: m.inspected_item_count, reverse=True)
    print(f'Part 2: {sorted_monkeys[0].inspected_item_count * sorted_monkeys[1].inspected_item_count}')


def load_puzzle() -> list[str]:
    with open('day_11_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_monkeys() -> list[Monkey]:
    monkeys = []
    monkey = Monkey()

    for line in load_puzzle():
        if not line:
            monkeys.append(monkey)
            monkey = Monkey()
            continue

        match = re.match('\s*Starting items: (.*)', line)
        if match:
            monkey.items = [int(i) for i in match.group(1).split(',')]

        match = re.match('\s*Operation: new = (.*)', line)
        if match:
            monkey.operation = match.group(1).strip()

        match = re.match('\s*Test: divisible by (\d+)', line)
        if match:
            monkey.divisor = int(match.group(1))

        match = re.match('\s*If true: throw to monkey (\d+)', line)
        if match:
            monkey.target_if_true = int(match.group(1))

        match = re.match('\s*If false: throw to monkey (\d+)', line)
        if match:
            monkey.target_if_false = int(match.group(1))

    monkeys.append(monkey)
    return monkeys


def execute_round(monkeys: list[Monkey], reduce_worry: bool):
    divisor_product = 1
    for monkey in monkeys:
        divisor_product *= monkey.divisor

    for monkey in monkeys:
        for item in monkey.items[:]:
            monkey.inspected_item_count += 1

            operation = monkey.operation.replace('old', str(item))
            new_item = eval(operation)

            if reduce_worry:
                new_item = new_item // 3
            else:
                new_item %= divisor_product

            if new_item % monkey.divisor == 0:
                monkeys[monkey.target_if_true].items.append(new_item)
            else:
                monkeys[monkey.target_if_false].items.append(new_item)
        monkey.items = []


if __name__ == '__main__':
    main()

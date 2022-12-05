#!/usr/bin/env python

from dataclasses import dataclass
import re


@dataclass
class Instruction:
    number: int
    source_stack: int
    dest_stack: int


@dataclass
class Stack:
    number: int
    crates: list[str]


def main() -> None:
    puzzle_input = load_puzzle()
    stacks, instructions = load_instructions(puzzle_input)

    for instruction in instructions:
        execute_instruction_9000(stacks, instruction)

    top_crates = ''.join([s.crates[-1] for s in stacks])
    print(f'Part 1: {top_crates}')

    stacks, instructions = load_instructions(puzzle_input)

    for instruction in instructions:
        execute_instruction_9001(stacks, instruction)

    top_crates = ''.join([s.crates[-1] for s in stacks])
    print(f'Part 2: {top_crates}')


def load_puzzle() -> list[str]:
    with open('day_05_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_instructions(puzzle_input: list[str]) -> tuple[list[Stack], list[Instruction]]:
    input_sep_index = [line.strip() for line in puzzle_input].index('')
    stacks_input = puzzle_input[:input_sep_index]
    instructions_input = puzzle_input[input_sep_index + 1:]

    stack_numbers = stacks_input.pop()
    stacks = [Stack(int(s), []) for s in stack_numbers.split()]
    while stacks_input:
        line = stacks_input.pop()
        for i in range(0, len(stacks)):
            index = (i * 3) + i + 1
            if index >= len(line):
                break
            value = line[index]
            if value.strip():
                stacks[i].crates.append(line[index])

    instructions = []
    for line in instructions_input:
        match = re.match('move (\d+) from (\d+) to (\d+)', line)
        if match:
            instructions.append(Instruction(int(match.group(1)), int(match.group(2)), int(match.group(3))))

    return stacks, instructions


def execute_instruction_9000(stacks: list[Stack], instruction: Instruction):
    source_stack = stacks[instruction.source_stack - 1]
    dest_stack = stacks[instruction.dest_stack - 1]

    for _ in range(0, instruction.number):
        crate = source_stack.crates.pop()
        dest_stack.crates.append(crate)


def execute_instruction_9001(stacks: list[Stack], instruction: Instruction):
    source_stack = stacks[instruction.source_stack - 1]
    dest_stack = stacks[instruction.dest_stack - 1]

    temp_stack = []
    for _ in range(0, instruction.number):
        crate = source_stack.crates.pop()
        temp_stack.append(crate)

    temp_stack.reverse()
    for crate in temp_stack:
        dest_stack.crates.append(crate)



if __name__ == '__main__':
    main()

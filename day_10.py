#!/usr/bin/env python

class CPU():
    def __init__(self, instructions: list[str]):
        self.x = 1
        self.current_cycle = 1
        self.cycle_delay = 0
        self.current_instruction = 0
        self.instructions = instructions

    def step_cycle(self):
        if self.is_done():
            return

        instruction = self.instructions[self.current_instruction]
        command, *_ = instruction.split()

        match command:
            case 'noop':
                self.current_instruction += 1
            case 'addx':
                if self.cycle_delay < 1:
                    self.cycle_delay += 1
                else:
                    arg = int(instruction.split()[1])
                    self.x += arg
                    self.cycle_delay = 0
                    self.current_instruction += 1

        self.current_cycle += 1

    def is_done(self) -> bool:
        return self.current_instruction >= len(self.instructions)

    def get_signal_strength(self) -> int:
        return self.current_cycle * self.x


def main() -> None:
    puzzle_input = load_puzzle()

    cpu = CPU(puzzle_input)
    strength_sum = 0
    while not cpu.is_done():
        if cpu.current_cycle in [20, 60, 100, 140, 180, 220]:
            strength_sum += cpu.get_signal_strength()
        cpu.step_cycle()
    print(f'Part 1: {strength_sum}')

    cpu = CPU(puzzle_input)
    print(f'Part 2:')
    for _ in range(6):
        for i in range(40):
            if i in [cpu.x - 1, cpu.x, cpu.x + 1]:
                print('#', end='')
            else:
                print('.', end='')
            cpu.step_cycle()
        print()


def load_puzzle() -> list[str]:
    with open('day_10_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


if __name__ == '__main__':
    main()

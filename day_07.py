#!/usr/bin/env python

from enum import auto, Enum
from dataclasses import dataclass
from typing import Generator


class CommandType(Enum):
    CD = auto()
    LS = auto()


@dataclass
class Command():
    type: CommandType
    args: list[str]
    output: str


@dataclass
class File():
    name: str
    size: int


@dataclass
class Directory():
    name: str
    parent: 'Directory'
    directories: list['Directory']
    files: list[File]


def main() -> None:
    puzzle_input = load_puzzle()
    commands = load_commands(puzzle_input)
    root_dir = load_directory_info(commands)

    size_sum = 0
    for dir in enumerate_directories(root_dir):
        size = get_directory_size(dir)
        if size <= 100000:
            size_sum += size
    print(f'Part 1: {size_sum}')

    available_space = 70000000 - get_directory_size(root_dir)
    needed_space = 30000000 - available_space
    ordered_dirs = sorted(list(enumerate_directories(root_dir)), key=lambda d: get_directory_size(d))
    for dir in ordered_dirs:
        size = get_directory_size(dir)
        if size >= needed_space:
            print(f'Part 2: {size}')
            break


def load_puzzle() -> list[str]:
    with open('day_07_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_commands(puzzlie_input: str) -> list[Command]:
    commands = []
    command_type = None
    command_args = None
    command_output = None
    for line in puzzlie_input:
        if line.startswith('$'):
            if command_type is not None:
                commands.append(Command(command_type, command_args, command_output))
            parts = line.split()[1:]
            command_type = get_command_type(parts[0])
            command_args = parts[1:]
            command_output = None
        else:
            if command_output is None:
                command_output = line
            else:
                command_output = '\n'.join([command_output, line])
    if command_type is not None:
        commands.append(Command(command_type, command_args, command_output))
    return commands


def get_command_type(command: str) -> CommandType:
    command = command.lower()
    if command == 'ls':
        return CommandType.LS
    if command == 'cd':
        return CommandType.CD
    raise Exception('Unknown command')


def load_directory_info(commands: list[Command]) -> Directory:
    current_dir: Directory = None
    for command in commands:
        if command.type == CommandType.CD:
            target_dir = command.args[0]
            if target_dir == '..':
                current_dir = current_dir.parent
            elif target_dir == '/':
                current_dir = Directory('/', None, [], [])
            else:
                current_dir = [d for d in current_dir.directories if d.name == target_dir][0]
        elif command.type == CommandType.LS:
            for line in command.output.splitlines():
                parts = line.split()
                if parts[0] == 'dir':
                    current_dir.directories.append(Directory(parts[1], current_dir, [], []))
                else:
                    current_dir.files.append(File(parts[1], int(parts[0])))
        else:
            raise Exception('Unknown command')

    while current_dir.parent is not None:
        current_dir = current_dir.parent

    return current_dir


def enumerate_directories(directory: Directory) -> Generator[Directory, None, None]:
    for child_dir in directory.directories:
        yield child_dir
        yield from enumerate_directories(child_dir)


def get_directory_size(directory: Directory) -> int:
    size = 0
    for file in directory.files:
        size += file.size
    for dir in directory.directories:
        size += get_directory_size(dir)
    return size


if __name__ == '__main__':
    main()

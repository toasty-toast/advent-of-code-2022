#!/usr/bin/env python

from dataclasses import dataclass


@dataclass
class Tree():
    height: int
    visible: bool
    scenic_score: int


@dataclass
class Forest():
    trees: list[list[Tree]]

    def populate_tree_visibility(self):
        for (row_index, tree_row) in enumerate(self.trees):
            for (column_index, tree) in enumerate(tree_row):
                tree.visible = False

                if row_index == 0 or row_index == len(self.trees) - 1 or column_index == 0 or column_index == len(tree_row) - 1:
                    tree.visible = True
                    continue

                visible_from_top = True
                for i in range(0, row_index):
                    if tree.height <= self.trees[i][column_index].height:
                        visible_from_top = False
                        break

                visible_from_bottom = True
                for i in range(row_index + 1, len(self.trees)):
                    if tree.height <= self.trees[i][column_index].height:
                        visible_from_bottom = False
                        break

                visible_from_left = True
                for i in range(0, column_index):
                    if tree.height <= self.trees[row_index][i].height:
                        visible_from_left = False
                        break

                visible_from_right = True
                for i in range(column_index + 1, len(tree_row)):
                    if tree.height <= self.trees[row_index][i].height:
                        visible_from_right = False
                        break

                tree.visible = visible_from_top or visible_from_bottom or visible_from_left or visible_from_right

    def populate_scenic_scores(self):
        for (row_index, tree_row) in enumerate(self.trees):
            for (column_index, tree) in enumerate(tree_row):
                visible_from_top = 0
                for i in reversed(range(0, row_index)):
                    visible_from_top += 1
                    if tree.height <= self.trees[i][column_index].height:
                        break

                visible_from_bottom = 0
                for i in range(row_index + 1, len(self.trees)):
                    visible_from_bottom += 1
                    if tree.height <= self.trees[i][column_index].height:
                        break

                visible_from_left = 0
                for i in reversed(range(0, column_index)):
                    visible_from_left += 1
                    if tree.height <= self.trees[row_index][i].height:
                        break

                visible_from_right = 0
                for i in range(column_index + 1, len(tree_row)):
                    visible_from_right += 1
                    if tree.height <= self.trees[row_index][i].height:
                        break

                tree.scenic_score = visible_from_top * visible_from_bottom * visible_from_left * visible_from_right

    def count_visible_trees(self) -> int:
        return sum([sum([1 if tree.visible else 0 for tree in row]) for row in self.trees])

    def get_highest_scenic_score(self) -> int:
        return max([max([tree.scenic_score for tree in row]) for row in self.trees])


def main() -> None:
    puzzle_input = load_puzzle()
    forest = load_forest(puzzle_input)
    forest.populate_tree_visibility()
    forest.populate_scenic_scores()

    print(f'Part 1: {forest.count_visible_trees()}')
    print(f'Part 2: {forest.get_highest_scenic_score()}')


def load_puzzle() -> list[str]:
    with open('day_08_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_forest(puzzle_input: list[str]) -> Forest:
    return Forest([[Tree(int(height), False, 0) for height in line] for line in puzzle_input])


if __name__ == '__main__':
    main()

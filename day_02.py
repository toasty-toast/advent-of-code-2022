#!/usr/bin/env python

from enum import Enum, auto


class GameMove(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class GameResult(Enum):
    WIN = auto()
    LOSS = auto()
    TIE = auto()


class Matchup():
    def __init__(self, opponent_move: GameMove, player_move: GameMove = None, result: GameResult = None) -> None:
        self._opponent_move = opponent_move

        if player_move is not None:
            self._player_move = player_move
        elif result is not None:
            if opponent_move == GameMove.ROCK:
                if result == GameResult.WIN:
                    self._player_move = GameMove.PAPER
                elif result == GameResult.TIE:
                    self._player_move = GameMove.ROCK
                elif result == GameResult.LOSS:
                    self._player_move = GameMove.SCISSORS
            elif opponent_move == GameMove.PAPER:
                if result == GameResult.WIN:
                    self._player_move = GameMove.SCISSORS
                elif result == GameResult.TIE:
                    self._player_move = GameMove.PAPER
                elif result == GameResult.LOSS:
                    self._player_move = GameMove.ROCK
            elif opponent_move == GameMove.SCISSORS:
                if result == GameResult.WIN:
                    self._player_move = GameMove.ROCK
                elif result == GameResult.TIE:
                    self._player_move = GameMove.SCISSORS
                elif result == GameResult.LOSS:
                    self._player_move = GameMove.PAPER

    @property
    def player_move(self) -> GameMove:
        return self._player_move

    @property
    def opponent_move(self) -> GameMove:
        return self._opponent_move

    def get_score(self) -> int:
        if self.player_move == GameMove.ROCK:
            if self.opponent_move == GameMove.ROCK:
                return 4
            elif self.opponent_move == GameMove.PAPER:
                return 1
            elif self.opponent_move == GameMove.SCISSORS:
                return 7
        elif self.player_move == GameMove.PAPER:
            if self.opponent_move == GameMove.ROCK:
                return 8
            elif self.opponent_move == GameMove.PAPER:
                return 5
            elif self.opponent_move == GameMove.SCISSORS:
                return 2
        elif self.player_move == GameMove.SCISSORS:
            if self.opponent_move == GameMove.ROCK:
                return 3
            elif self.opponent_move == GameMove.PAPER:
                return 9
            elif self.opponent_move == GameMove.SCISSORS:
                return 6
        else:
            return 0


CHAR_TO_OPPONENT_GAMEMOVE = {
    'A': GameMove.ROCK,
    'B': GameMove.PAPER,
    'C': GameMove.SCISSORS
}


CHAR_TO_PLAYER_GAMEMOVE = {
    'X': GameMove.ROCK,
    'Y': GameMove.PAPER,
    'Z': GameMove.SCISSORS
}


CHAR_TO_GAME_RESULT = {
    'X': GameResult.LOSS,
    'Y': GameResult.TIE,
    'Z': GameResult.WIN
}


def main() -> None:
    puzzle_input = load_puzzle()

    matchups = load_matchups_by_move(puzzle_input)
    print(f'Part 1: {sum(m.get_score() for m in matchups)}')

    matchups = load_matchups_by_result(puzzle_input)
    print(f'Part 2: {sum(m.get_score() for m in matchups)}')


def load_puzzle() -> list[str]:
    with open('day_02_input.txt') as f:
        return [line.rstrip() for line in f.readlines()]


def load_matchups_by_move(puzzle_input: list[str]) -> list[Matchup]:
    return [Matchup(CHAR_TO_OPPONENT_GAMEMOVE[line[0]], player_move=CHAR_TO_PLAYER_GAMEMOVE[line[2]]) for line in puzzle_input]


def load_matchups_by_result(puzzle_input: list[str]) -> list[Matchup]:
    return [Matchup(CHAR_TO_OPPONENT_GAMEMOVE[line[0]], result=CHAR_TO_GAME_RESULT[line[2]]) for line in puzzle_input]


if __name__ == '__main__':
    main()

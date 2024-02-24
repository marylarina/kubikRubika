import copy
import random
import random as rnd
from enum import Enum


class GameState(Enum):
    PLAYING = 0  # игра не закончена
    WIN = 1  # игра закончена победой


class CellState(Enum):
    SELECTED = 1
    NOT_SELECTED = 0


class Color(Enum):
    FIRST = 0
    SECOND = 1


class KubikRubikaCell:
    def __int__(self, color: Color = Color.FIRST, state: CellState = CellState.NOT_SELECTED):
        self._color = color
        self._state = state

    @property
    def color(self) -> Color:
        return self._color

    @property
    def state(self) -> CellState:
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @color.setter
    def color(self, value):
        self._color = value


class KubikRubikaGame:
    def __init__(self, row_count: int, col_count: int, colorIndex: int):
        self._row_count = row_count
        self._col_count = col_count
        self._colorIndex = colorIndex
        self.new_game()

    def new_game(self) -> None:
        self._field = [copy.deepcopy([KubikRubikaCell() for c in range(self.col_count)]) for r in range(self.row_count)]
        for p in [(r, c) for r in range(self.row_count) for c in range(self.col_count)]:
            self[p]._color = random.choice(list(Color))
            self[p]._state = CellState.NOT_SELECTED
        self._state = GameState.PLAYING

    @property
    def row_count(self) -> int:
        return self._row_count

    @property
    def col_count(self) -> int:
        return self._col_count

    @property
    def colorIndex(self) -> int:
        return self._colorIndex

    @property
    def state(self) -> GameState:
        return self._state

    def _update_playing_state(self):
        count = 0
        for p in [(r, c) for r in range(self.row_count) for c in range(self.col_count)]:
            if self[p]._color == Color.FIRST:
                count = count + 1
        if count == self.col_count * self.row_count or count == 0:
            self._state = GameState.WIN
        else:
            self._state = GameState.PLAYING

    def left_mouse_click(self, row: int, col: int, countElem: int) -> None:
        if self.state != GameState.PLAYING:
            return
        cells = []
        i = 0
        while i < countElem:
            varCell = self[row, i]
            cells.append(varCell)
            i += 1
        for elem in cells:
            if elem.color == Color.FIRST:
                elem.color = Color.SECOND
            else:
                elem.color = Color.FIRST
        k = 0
        while k < countElem // 2:
            c = cells[k].color
            cells[k].color = cells[len(cells) - 1 - k].color
            cells[len(cells) - 1 - k].color = c
            k += 1
        self._update_playing_state()

    def right_mouse_click(self, row: int, col: int, countElem: int) -> None:
        if self.state != GameState.PLAYING:
            return
        cells = []
        i = 0
        while i < countElem:
            varCell = self[i, col]
            cells.append(varCell)
            i += 1
        for elem in cells:
            if elem.color == Color.FIRST:
                elem.color = Color.SECOND
            else:
                elem.color = Color.FIRST
        k = 0
        while k < countElem // 2:
            c = cells[k].color
            cells[k].color = cells[len(cells) - 1 - k].color
            cells[len(cells) - 1 - k].color = c
            k += 1
        self._update_playing_state()

    def __getitem__(self, indices: tuple) -> KubikRubikaCell:
        return self._field[indices[0]][indices[1]]

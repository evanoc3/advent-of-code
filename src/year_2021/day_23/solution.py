#!/usr/bin/env python3

from pathlib import Path
from src.common import ISolution


input_file_path = Path(__file__).parent / "input.txt"


class Solution(ISolution):

  _TYPE_COST = { "A": 1, "B": 10, "C": 100, "D": 1000 }

  _ROOMS = { "A": 3, "B": 5, "C": 7, "D": 9 }

  def _parse_input(self, input_file_lines: list[str]):
    return (*((*line,) for line in input_file_lines),)
  

  def _room_size(self, state):
    return len(state)-3

  def _field(self, state, x, y):
    return state[y][x]

  def _stoppable_fields(self, state):
    return tuple(i for i in range(1, len(state[0]) - 1) if i not in Solution._ROOMS.values())

  def _is_in_own_room(self, state, x, y):
    if not self._is_amphipod(state, x, y):
      return False
    if x == Solution._ROOMS[self._field(state, x, y)]:
      return True
    return False

  def _is_in_any_room(self, state, x, y):
    return y > 1

  def _is_room_complete(self, state, x):
    for y in range(2,2+self._room_size(state)):
      if not self._is_in_own_room(state, x, y):
        return False
    return True

  def _rooms_complete(self, state):
    for room in Solution._ROOMS.values():
      if not self._is_room_complete(state, room): return False
    return True

  def _is_amphipod(self, state, x, y):
    val = self._field(state, x, y)
    return val if val in Solution._ROOMS.keys() else False

  def _is_empty(self, state, x, y):
    return self._field(state, x, y) == '.'

  def _is_room_empty(self, state, x):
    for y in range(2,2+self._room_size(state)):
      if not self._is_empty(state, x, y):
        return False
    return True

  def _has_room_available(self, state, x, y):
    amphipod = self._field(state, x, y)
    room = Solution._ROOMS[amphipod]
    if self._is_room_empty(state, room): return True
    for y in range(2,2+self._room_size(state)):
      if not self._is_empty(state, room, y) and not self._is_in_own_room(state, room, y):
        return False
    return True

  def _is_path_empty(self, state, x, targetX):
    while x != targetX:
      if x > targetX:
        x -= 1
      if x < targetX:
        x += 1
      if not self._is_empty(state, x, 1):
        return False
    return True

  def _is_blocking_room(self, state, x, y):
    for j in range(y + 1, 2 + self._room_size(state)):
      if self._is_amphipod(state, x, j) and not self._is_in_own_room(state, x, j):
        return True
    return False

  def _is_blocked_in_room(self, state, x, y):
    if y < 3: return False
    return not self._is_empty(state, x, y-1)

  def _move_in_pos(self, state, room):
    for y in range(1 + self._room_size(state), 1, -1):
      if self._is_empty(state, room, y):
        return y

  def _can_move(self, state, x, y):
    return (not self._is_in_own_room(state, x, y) or self._is_blocking_room(state, x, y)) and not self._is_blocked_in_room(state, x, y)

  def _move_cost(self, state, x, y, i, j):
    return ((y - 1) + abs(x - i)  + (j - 1)) * Solution._TYPE_COST[self._field(state, x,y)]

  def _move(self, d, x, y, i, j):
    newData = (*((*(((self._field(d,a,b), self._field(d,x,y)) [ a==i and b==j ], self._field(d,i,j))[a==x and b==y] for a in range(len(d[b]))),) for b in range(len(d))),)
    return (newData, self._move_cost(d, x, y, i, j))

  def _check_state(self, state, cache):
    cached = cache.get(state)
    if cached is not None:
      return cached
    if self._rooms_complete(state):
      return 0
    costs = []
    for y in range(1, len(state)):
      for x in range(1, len(state[y])):
        amphipod = self._is_amphipod(state, x, y)
        if not amphipod:
          continue
        if self._can_move(state, x, y):
          room = Solution._ROOMS[amphipod]
          if self._has_room_available(state, x, y) and self._is_path_empty(state, x, room):
            newState, newCost = self._move(state, x, y, room, self._move_in_pos(state, room))
            cost = self._check_state(newState, cache)
            if cost != -1:
              costs.append(cost + newCost)
          elif self._is_in_any_room(state, x, y):
            for i in self._stoppable_fields(state):
              if not self._is_path_empty(state, x, i):
                continue
              newState, newCost = self._move(state, x, y, i, 1)
              cost = self._check_state(newState, cache)
              if cost != -1:
                costs.append(cost + newCost)
    cache[state] = min(costs) if costs else -1
    return cache[state]

  def part_1(self) -> int:
    return self._check_state(self.input, {})
  

  def _extend(self, state):
    return (*state[:3], (*"  #D#C#B#A#",), (*"  #D#B#A#C#",), *state[3:],)

  def part_2(self) -> int:
    return self._check_state(self._extend(self.input), {})


  def main(self) -> None:
    print(f"1. The required energy cost is: {self.part_1()}")
    print(f"2. The least energy required is: {self.part_2()}")


if __name__ == "__main__":
	with open(input_file_path, "r") as input_file:
		solution = Solution(input_file.readlines())
	solution.main()

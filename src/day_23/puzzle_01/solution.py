#!/usr/bin/env python3

from pathlib import Path


# Constants

TYPE_COST = { "A":1, "B":10, "C":100, "D":1000 }
ROOMS = { "A": 3, "B":5, "C":7, "D":9 }


# Functions

def main() -> None:
	input_file_path = Path(__file__).parents[1] / "input.txt"
	with open(input_file_path, "r") as input_file:
		data = parse_input(input_file.readlines())

	print(f"1. The required energy cost is: {check_state(data, {})}")
	return

def parse_input(input_lines: list[str]):
	return (*((*line,) for line in input_lines),)

def extend(state):
  return (*state[:3], (*"  #D#C#B#A#",), (*"  #D#B#A#C#",), *state[3:],)

def room_size(state):
  return len(state)-3

def field(state, x, y):
  return state[y][x]

def stoppable_fields(state):
  return tuple(i for i in range(1, len(state[0]) - 1) if i not in ROOMS.values())

def is_in_own_room(state, x, y):
  if not is_amphipod(state, x, y):
    return False
  if x == ROOMS[field(state, x, y)]:
    return True
  return False

def is_in_any_room(state, x, y):
  return y > 1

def is_room_complete(state, x):
  for y in range(2,2+room_size(state)):
    if not is_in_own_room(state, x, y):
      return False
  return True

def rooms_complete(state):
  for room in ROOMS.values():
    if not is_room_complete(state, room): return False
  return True

def is_amphipod(state, x, y):
  val = field(state, x, y)
  return val if val in ROOMS.keys() else False

def is_empty(state, x, y):
  return field(state, x, y) == '.'

def is_room_empty(state, x):
  for y in range(2,2+room_size(state)):
    if not is_empty(state, x, y):
      return False
  return True

def has_room_available(state, x, y):
  amphipod = field(state, x, y)
  room = ROOMS[amphipod]
  if is_room_empty(state, room): return True
  for y in range(2,2+room_size(state)):
    if not is_empty(state, room, y) and not is_in_own_room(state, room, y):
      return False
  return True

def is_path_empty(state, x, targetX):
  while x != targetX:
    if x > targetX:
      x -= 1
    if x < targetX:
      x += 1
    if not is_empty(state, x, 1):
      return False
  return True

def is_blocking_room(state, x, y):
  for j in range(y + 1, 2 + room_size(state)):
    if is_amphipod(state, x, j) and not is_in_own_room(state, x, j):
      return True
  return False

def is_blocked_in_room(state, x, y):
  if y < 3: return False
  return not is_empty(state, x, y-1)

def move_in_pos(state, room):
  for y in range(1 + room_size(state), 1, -1):
    if is_empty(state, room, y):
      return y

def can_move(state, x, y):
  return (not is_in_own_room(state, x, y) or is_blocking_room(state, x, y)) and not is_blocked_in_room(state, x, y)

def move_cost(state, x, y, i, j):
  return ((y - 1) + abs(x - i)  + (j - 1)) * TYPE_COST[field(state, x,y)]

def move(d, x, y, i, j):
  newData = (*((*(((field(d,a,b),field(d,x,y))[a==i and b==j],field(d,i,j))[a==x and b==y] for a in range(len(d[b]))),) for b in range(len(d))),)
  return (newData, move_cost(d, x, y, i, j))

def check_state(state, cache):
  cached = cache.get(state)
  if cached is not None:
    return cached
  if rooms_complete(state):
    return 0
  costs = []
  for y in range(1, len(state)):
    for x in range(1, len(state[y])):
      amphipod = is_amphipod(state, x, y)
      if not amphipod:
        continue
      if can_move(state, x, y):
        room = ROOMS[amphipod]
        if has_room_available(state, x, y) and is_path_empty(state, x, room):
          newState, newCost = move(state, x, y, room, move_in_pos(state, room))
          cost = check_state(newState, cache)
          if cost != -1:
            costs.append(cost + newCost)
        elif is_in_any_room(state, x, y):
          for i in stoppable_fields(state):
            if not is_path_empty(state, x, i):
              continue
            newState, newCost = move(state, x, y, i, 1)
            cost = check_state(newState, cache)
            if cost != -1:
              costs.append(cost + newCost)
  cache[state] = min(costs) if costs else -1
  return cache[state]


# Entry Point

if __name__ == "__main__":
	main()

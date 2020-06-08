from typing import List
BOARD_SIZE = 8

def put_queen(line: int, stones: List[int]) -> int:
    if line >= BOARD_SIZE:
        return 1
    # check if we can put a stone in each postion
    ans = 0
    for i in range(BOARD_SIZE):
        # see stones that are already put
        for j in range(line):
            if stones[j] == i:
                break
            if stones[j] == i - (line - j):
                break
            if stones[j] == i + (line - j):
                break
        else:
            stones[line] = i
            ans += put_queen(line + 1, stones)
    return ans

if __name__ == "__main__":
    initial_stones = [None] * BOARD_SIZE
    print(put_queen(0, initial_stones))

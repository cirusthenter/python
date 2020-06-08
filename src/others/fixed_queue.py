from typing import Any


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.que = [None] * capacity
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.no = 0

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    def enque(self, value: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear >= self.capacity:
            self.rear %= self.capacity

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front >= self.capacity:
            self.front %= self.capacity
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> int:
        for offset in range(self.no):
            index = (self.front + offset) % self.capacity
            if self.que[index] == value:
                return index
        return -1

    def count(self, value: Any) -> int:
        cnt = 0
        for offset in range(self.no):
            index = (self.front + offset) % self.capacity
            if self.que[index] == value:
                cnt += 1
        return cnt

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.front = self.rear = self.no = 0

    def dump(self) -> None:
        if self.is_empty():
            print('queue is empty')
            return
        print(f'[{self.que[self.front]}', end='')
        for offset in range(1, self.no):
            index = (self.front + offset) % self.capacity
            print(f', {self.que[index]}', end='')
        print(']')

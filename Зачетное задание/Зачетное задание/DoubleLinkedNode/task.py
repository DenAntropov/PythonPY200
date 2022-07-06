from typing import Any, Optional


class Node:

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):

    def __init__(self, value, next_, prev):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self):
        next_repr: str = str(None) \
            if self.next is None \
            else f'DoubleLinkedNode({self.next.value}, {None}, {None})'
        prev_repr: str = str(None) \
            if self.next is None \
            else f'DoubleLinkedNode({self.prev.value}, {None}, {None})'
        return f'DoubleLinkedNode({self.value}, {next_repr}, {prev_repr})'


if __name__ == "__main__":
    list_ = [1, 2, 3, 4]

    ll = DoubleLinkedNode(list_)
    print(ll)

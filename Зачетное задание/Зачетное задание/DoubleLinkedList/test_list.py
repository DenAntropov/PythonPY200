from task import LinkedList, DoubleLinkedList


def test_get():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    assert lst[0].value == 1
    assert lst[1].value == 2
    try:
        lst[2]
    except IndexError as er:
        assert er.args[0] == 'invalid index'
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    assert lst[0].value == 1
    assert lst[1].value == 2
    try:
        lst[2]
    except IndexError as er:
        assert er.args[0] == 'invalid index'


def test_set():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst[0] = 2
    lst[1] = 1
    assert lst[0].value == 2
    assert lst[1].value == 1
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst[0] = 2
    lst[1] = 1
    assert lst[0].value == 2
    assert lst[1].value == 1


def test_del():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    del lst[0]
    assert lst[0].value == 2
    try:
        lst[1]
    except IndexError as er:
        assert er.args[0] == 'invalid index'
    del lst[0]
    lst.append(12)
    lst.append(13)
    assert lst[0].value == 12
    assert lst[1].value == 13
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    del lst[0]
    assert lst[0].value == 2
    try:
        lst[1]
    except IndexError as er:
        assert er.args[0] == 'invalid index'
    del lst[0]
    lst.append(12)
    lst.append(13)
    assert lst[0].value == 12
    assert lst[1].value == 13


def test_len():
    lst = LinkedList()
    assert len(lst) == 0
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert len(lst) == 3
    del lst[0]
    assert len(lst) == 2
    del lst[0]
    del lst[0]
    assert len(lst) == 0
    lst = DoubleLinkedList()
    assert len(lst) == 0
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert len(lst) == 3
    del lst[0]
    assert len(lst) == 2
    del lst[0]
    del lst[0]
    assert len(lst) == 0


def test_str():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert str(lst) == '1 2 3 '
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert str(lst) == '1 2 3 '


def test_repr():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert repr(lst) == '[1, 2, 3]'
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert repr(lst) == '[1, 2, 3]'


def test_insert():
    lst = LinkedList()
    lst.insert(100, 1)
    lst.insert(0, 2)
    lst.insert(1, 3)
    assert lst[0].value == 2
    assert lst[1].value == 3
    assert lst[2].value == 1
    lst = DoubleLinkedList()
    lst.insert(100, 1)
    lst.insert(0, 2)
    lst.insert(1, 3)
    assert lst[0].value == 2
    assert lst[1].value == 3
    assert lst[2].value == 1


def test_append():
    lst = LinkedList()
    lst.append(3)
    lst.append(2)
    lst.append(1)
    assert lst[0].value == 3
    assert lst[1].value == 2
    assert lst[2].value == 1
    lst = DoubleLinkedList()
    lst.append(3)
    lst.append(2)
    lst.append(1)
    assert lst[0].value == 3
    assert lst[1].value == 2
    assert lst[2].value == 1


def test_iter():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    s = [1, 2, 3]
    k = 0
    for i in lst:
        assert i == s[k]
        k += 1
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    s = [1, 2, 3]
    k = 0
    for i in lst:
        assert i == s[k]
        k += 1


def test_contains():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert 1 in lst == True
    assert 4 in lst == False
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert (1 in lst) == True
    assert (4 in lst) == False


def test_reversed():
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    s = [3, 2, 1]
    k = 0
    for i in reversed(lst):
        assert i == s[k]
        k += 1


def test_count():
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(2)
    assert lst.count(3) == 1
    assert lst.count(2) == 2
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(2)
    assert lst.count(3) == 1
    assert lst.count(2) == 2


def test_pop():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert lst.pop(0) == 1
    assert lst[0].value == 2
    assert lst.pop(1) == 3
    assert len(lst) == 1
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert lst.pop(0) == 1
    assert lst[0].value == 2
    assert lst.pop(1) == 3
    assert len(lst) == 1


def test_extend():
    lst = LinkedList()
    lst.extend([1, 2, 3])
    s = [1, 2, 3]
    k = 0
    for i in lst:
        assert i == s[k]
        k += 1
    lst = DoubleLinkedList()
    lst.extend([1, 2, 3])
    s = [1, 2, 3]
    k = 0
    for i in lst:
        assert i == s[k]
        k += 1


def test_remove():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.remove(2)
    assert len(lst) == 2
    assert lst[0].value == 1
    assert lst[1].value == 3
    lst.remove(1)
    lst.remove(3)
    assert len(lst) == 0
    lst.insert(0, 100)
    lst.append(15)
    lst.insert(1, 4)
    assert lst[1].value == 4
    assert len(lst) == 3
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.remove(2)
    assert len(lst) == 2
    assert lst[0].value == 1
    assert lst[1].value == 3
    lst.remove(1)
    lst.remove(3)
    assert len(lst) == 0
    lst.insert(0, 100)
    lst.append(15)
    lst.insert(1, 4)
    assert lst[1].value == 4
    assert len(lst) == 3


def test_index():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert lst.index(2) == 1
    assert lst.index(3) == 2
    assert lst.index(1) == 0
    try:
        lst.index(4)
    except ValueError as er:
        assert er.args[0] == 'invalid value'
    lst = DoubleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert lst.index(2) == 1
    assert lst.index(3) == 2
    assert lst.index(1) == 0
    try:
        lst.index(4)
    except ValueError as er:
        assert er.args[0] == 'invalid value'


if __name__ == "__main__":
    test_index()

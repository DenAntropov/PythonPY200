from task import DoubleLinkedNode, Node


def test_repr():
    node = DoubleLinkedNode(10)
    expected_value = "DoubleLinkedNode(10, None, None)"
    actual_value = repr(node)
    assert expected_value == actual_value


def test_str():
    nde = Node()
    nde.append(1)
    nde.append(2)
    nde.append(3)
    assert str(nde) == '1 2 3 '
    nde = DoubleLinkedNode()
    nde.append(1)
    nde.append(2)
    nde.append(3)
    assert str(nde) == '1 2 3 '


if __name__ == "__main__":
    test_repr()
    test_str()

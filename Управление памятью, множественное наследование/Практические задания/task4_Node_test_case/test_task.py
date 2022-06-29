import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)
        self.assertIsNone(node.next,
                          msg="При инициализации значение по умолчанию следующего узла не None")     # TODO с помощью метода assertIsNone проверить следующий узел

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        second_node = Node("second_node")
        first_node = Node("first_node", next_=second_node)

        expected_value = second_node
        actual_value = first_node.next
        self.assertIs(actual_value, expected_value,
                      msg="Узлы не эквивалентны друг другу")    # TODO проверить что узлы связались

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node_value = 5
        node = Node(node_value)
        expected_value = f"Node({node_value}, None)"
        actual_value = repr(node)

        self.assertEqual(expected_value, actual_value,
                         msg="Неверный repr для ноды без следующего узла")      # TODO проверить метод __repr__ без следующего узла

    @unittest.skip(reason="Еще не реализованная функциональность")  # TODO пропустить тест с помощью декоратора unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        expected_value = str(some_value)
        self.assertEqual(expected_value, str(node))
        self.assertEqual(expected_value, f"{node}")    # TODO проверить строковое представление

    def test_is_valid(self):
        Node.is_valid(Node(5))
        Node.is_valid(None)     # TODO проверить метод is_valid при корректных узлах

        with self.assertRaises(TypeError):
            invalid_node = "invalid_node"
            Node.is_valid(invalid_node)     # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки

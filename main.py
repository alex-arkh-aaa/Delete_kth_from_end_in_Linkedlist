class Node:
    """
    Класс узла связанного списка.
    Хранит данные и ссылку на следующий узел.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Класс связанного списка.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Добавляет новый узел с заданными данными в конец списка.
        """
        new_node = Node(data)  # Создаем новый узел
        if not self.head:  # Если список пуст
            self.head = new_node  # Новый узел становится первым
            return
        current = self.head  # Начинаем с первого узла
        while current.next:  # Идем до последнего узла
            current = current.next
        current.next = new_node  # Добавляем новый узел в конец

    def delete_kth_from_end(self, k):
        """
        Удаляет k-й узел с конца списка.

        Args:
            k: Позиция узла для удаления (считая с конца).
        """

        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        if self.head == None or k <= 0 or k > length:
            return

        if k == length:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(length - k - 1):
                current = current.next
            current.next = current.next.next

    def print_list(self):
        """
        Печатает все элементы списка в удобном формате.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Пример использования
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# Полученный список:
linked_list.print_list()  # Вывод: 1 -> 2 -> 3 -> 4 -> 5 -> None

linked_list.delete_kth_from_end(1)  # Удаляем 2-ой узел с конца (4)
linked_list.delete_kth_from_end(1)
# Список после удаления 2-го узла с конца:
linked_list.print_list()  # Вывод: 1 -> 2 -> 3 -> 5 -> None

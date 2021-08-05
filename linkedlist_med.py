class LinkedListNode:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next

    def __str__(self):
        return f"{self._data}"

    def __repr__(self):
        return f"data={self._data}, next={id(self._next)}"


class LinkedList:
    def __init__(self, iterable=None):
        self._head = None
        self._size = 0
        # Added 4/5/21: made it easier to initialize the list
        if iterable is not None:
            for i in reversed(iterable):
                self.add_to_head(i)

    @property
    def size(self):
        return self._size

    def __len__(self):
        return self.size

    def add_to_head(self, data):
        node = LinkedListNode(data)
        node.next = self._head
        self._head = node
        self._size += 1

    def __iter__(self):
        curr = self._head
        while curr:
            yield curr.data
            curr = curr.next

    def __str__(self):
        return " ".join([str(d) for d in self])

    def find(self, data):
        """
        :param data: the data to look for in the list
        :return: data if it exists in the list
        :raise: KeyError if data is not in the list
        """
        for d in self:
            if d == data:
                return d
        raise KeyError

    def __contains__(self, data):
        try:
            self.find(data)
            return True
        except KeyError:
            return False

    def __getitem__(self, index):
        self.validate_index(index)

        for i, d in enumerate(self):
            if i == index:
                return d

    def validate_index(self, index):
        if type(index) is not int:
            raise TypeError("index should be int")

        if index < 0 or index >= self.size:
            raise ValueError(f"index {index} is invalid")

    def remove(self, data):
        prev, curr = None, self._head
        while curr:
            if data == curr.data:
                if prev:
                    prev.next = curr.next
                else:
                    self._head = curr.next
                self._size -= 1
                return
            prev, curr = curr, curr.next
        raise KeyError

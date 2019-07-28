"""

"""
import hashlib
from collections import namedtuple


Item = namedtuple("Item", ["key", "value"])


class HashTable:

    def __init__(self):
        self._array_size = 10
        self._added_items_amount = 0
        self._array = self._create_empty_array()

    def put(self, key, value):
        if self.load_factor > 0.7:
            self._duplicate_array_size()

        index = self._calculate_position(key)
        self._array[index].append(Item(key=key, value=value))
        self._added_items_amount += 1

    def get(self, key):
        item_list = self._get_item_list(key)
        for item in item_list:
            if item.key == key:
                return item.value

    def remove(self, key):
        item_list = self._get_item_list(key)
        for item in item_list:
            if item.key == key:
                item_list.remove(item)
                self._added_items_amount -= 1
                return item.value

    @property
    def load_factor(self):
        return self._added_items_amount / self._array_size

    def _create_empty_array(self):
        return [[] for _ in range(self._array_size)]

    def _duplicate_array_size(self):
        self._array_size *= 2
        self._added_items_amount = 0

        current_array = self._array
        self._array = self._create_empty_array()

        for item_list in current_array:
            for item in item_list:
                self.put(item.key, item.value)

    def _calculate_position(self, key):
        return self._hash(key) % self._array_size

    def _hash(self, key):
        key = str(key)
        hash_key = hashlib.sha3_512(key.encode()).hexdigest()
        return int(hash_key, 16)

    def _get_item_list(self, key):
        index = self._calculate_position(key)
        item_list = self._array[index]
        if item_list == []:
            raise KeyError()

        return item_list

    def __str__(self):
        item_str = ""
        for item_list in self._array:
            item_str += f"{item_list}\n"
        return item_str


hash_table = HashTable()

hash_table.put("A", 1)
hash_table.put("B", 2)
hash_table.put("C", 3)
hash_table.put("D", 4)
hash_table.put("E", 5)
hash_table.put("F", 6)
hash_table.put("G", 7)
hash_table.put("H", 8)

assert hash_table._array_size == 10
assert hash_table._added_items_amount == 8
assert hash_table.load_factor == 0.8

hash_table.put("I", 9)

assert hash_table._array_size == 20
assert hash_table._added_items_amount == 9
assert hash_table.load_factor == 0.45

hash_table.put("J", 10)
hash_table.put("K", 11)

print(hash_table)

assert hash_table.get("A") == 1
assert hash_table.get("B") == 2
assert hash_table.get("C") == 3
assert hash_table.get("D") == 4
assert hash_table.get("E") == 5
assert hash_table.get("F") == 6
assert hash_table.get("G") == 7
assert hash_table.get("H") == 8
assert hash_table.get("I") == 9
assert hash_table.get("J") == 10
assert hash_table.get("K") == 11


try:
    hash_table.get("Key does not exists")
except KeyError:
    pass


assert hash_table.remove("A") == 1
assert hash_table._added_items_amount == 10
try:
    hash_table.remove("A")
except KeyError:
    pass

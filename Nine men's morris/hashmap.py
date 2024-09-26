#element
import random


class MapElement(object):
    __slots__ = '_key', '_value'

    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


#bucket
class Map(object):
    def __init__(self):
        self._data = []

    def __getitem__(self, key):
        for item in self._data:
            if item.key == key:
                return item.value
        raise KeyError("Nema elemnta sa tim kljucem!")

    def __setitem__(self, key, value):
        for item in self._data:
            if item.key == key:
                item.value = value
                return
        self._data.append(MapElement(key, value))

    def __delitem__(self, key):
        for i in range(len(self._data)):
            if self._data[i].key == key:
                self._data.pop(i)
                return
        raise KeyError("Nema element sa tim kljucem!")

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        for item in self._data:
            if item.key == key:
                return True
        return False

    def __iter__(self):
        for item in self._data:
            yield item.key

    def items(self):
        for item in self._data:
            yield item.key, item.value

    def keys(self):
        keys = []
        for item in self._data:
            keys.append(item.key)
        return keys

    def values(self):
        values = []
        for item in self._data:
            values.append(item.value)
        return values

    def clear(self):
        self._data = []

# if __name__ == '__main__':
#     table = Map()
#     table[3] = 10
#     table['x'] = 11
#     table['asd'] = "abcdefg"
#
#     print(table['asd'])
#     print(table.values())
#     print(table.keys())
#
#     if 'y' in table:
#         print("Tabela sadrzi kljuc y")
#     else:
#         print("Tabela ne sadrzi kljuc y")
#
#     for item in table:
#         print(item, table[item])
#
#     del table['asd']
#     print(len(table) == 2)
#
#     table.clear()
#     print(len(table) == 0)


class HashMap(object):
    def __init__(self, capacity):
        self._data = capacity * [None]
        self._capacity = capacity
        self._size = 9
        self.prime = 109345121

        self._a = 1 + random.randrange(self.prime-1)
        self._b = random.randrange(self.prime)

    def __len__(self):
        return self._size

    def hash(self, x):
        hashed_value = (hash(x)*self._a + self._b) % self.prime
        compressed = hashed_value % self._capacity
        return compressed

    def _resize(self, capacity):
        old_data = list(self.items())
        self._data = capacity * [None]
        self._size = 0

        for (k,v) in old_data:
            self[k] = v

    def __getitem__(self, key):
        bucket_index = self.hash(key)
        return self._bucket_getitem(bucket_index, key)

    def __setitem__(self, key, value):
        bucket_index = self.hash(key)
        self._bucket_setitem(bucket_index, key, value)

        current_capacity = len(self._data)
        if self._size > current_capacity // 2:
            self._resize(2*current_capacity-1)

    def _bucket_getitem(self, index, key):
        bucket = self._data[index]
        if bucket is None:
            raise KeyError("Nema elementa u bucketu")
        return bucket[key]

    def _bucket_setitem(self, index, key, value):
        bucket = self._data[index]
        if bucket is None:
            self._data[index] = Map()

        current_size = len(self._data[index])
        self._data[index][key] = value
        if len(self._data[index]) > current_size:
            self._size += 1

    def __iter__(self):
        for bucket in self._data:
            if bucket is not None:
                for key in bucket:
                    yield key

    def items(self):
        for bucket in self._data:
            if bucket is not None:
                for key, value in bucket.items():
                    yield key, value


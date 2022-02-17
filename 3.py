# --------------- Task 1 --------------------

import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be greater than zero."
        self._size = size
        createarray = ctypes.py_object * size
        self._values = createarray()
        self.clear( None )

    def __len__(self):
        return self._size

    def __contains__(self, item):
        return item in self._values

    def __getitem__(self, index):
        assert 0 <= index < len(self), "Array index out of range."
        temp = self._values[index]
        return temp

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Array index out of range."
        self._values[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._values[i] = value

    def __iter__(self):
        return _ArrayIterator(self._values)

class _ArrayIterator:
    def __init__(self, array):
        self._array = array
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._array):
            temp = self._array[self._index]
            self._index += 1
            return temp
        else:
            raise StopIteration

def Frequency(file):
    temp = open(file, 'r')
    data = temp.read()
    temp.close()
    character = Array(len(data))
    count = Array(len(data))
    for i in range(len(data)):
        if character.__contains__(data[i]) == False:
            character.__setitem__(i, data[i])
            count.__setitem__(i, data.count(data[i]))
    for x in range(len(character)):
        if character[x] and count[x] is not None:
            print("{} come {} times.".format(character[x],count[x]))

Frequency("exp.txt")
            
# --------------- Task 2 --------------------

class Set:
    def __init__(self):
        self._values = list()

    def __len__(self):
        return len(self._values)

    def __contains__(self, item):
        return item in self._values

    def add(self, item):
        if item not in self._values:
            self._values.append(item)

    def remove(self, item):
        assert item in self._values, "The element must be in the Set"
        self._values.remove(item)

    def __iter__(self):
        return _SetIterator(self._values)

class _SetIterator:
    def __init__(self, sett):
        self._sett = sett
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sett):
            temp = self._sett[self._index]
            self._index += 1
            return temp
        else:
            raise StopIteration

set1 = Set()
set1.add('Basit')
set1.add('Jakwani')
print(set1.__len__())
set1.remove('Basit')
print(set1.__len__())

# --------------- Task 3 --------------------

def SelectionSort( values ):
    length = len(values)
    for i in range(length - 1):
        firstelement = i
        for j in range(i + 1, length):
            if values[j] < values[firstelement]:
                firstelement = j

        if firstelement != i:
            temp = values[i]
            values[i] = values[firstelement]
            values[firstelement] = temp
    return values

nums = [5,6,7,1,2,4,9,0,5]
print(SelectionSort(nums))

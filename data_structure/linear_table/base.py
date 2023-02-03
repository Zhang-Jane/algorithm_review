

class LineTable:
    def __init__(self, max_cap: int = 10) -> None:
        self.max_cap = max_cap
        self.current_num = 0
        self.box = [None] * self.max_cap

    @property
    def is_full(self) -> bool:
        if self.max_cap == 0:
            return True
        else:
            return False

    def __len__(self):
        return self.current_num

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max_cap:
            self.box[index] = value
        else:
            raise IndexError

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max_cap:
            return self.box[index]
        else:
            raise IndexError

    def clear(self):
        self.__init__()

    def count(self) -> int:
        return self.current_num

    def __repr__(self) -> str:
        return str(self.box)

    def insert(self, index, vaule):
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max_cap:
            if index >= self.current_num:
                self.append(vaule)
            else:
                # 插入改变了后面的位置，让后位置+1，从最后面开始挪动
                for i in range(self.current_num, index, -1):
                    self.box[i] = self.box[i - 1]
                self.box[index] = vaule
            self.current_num += 1

    def append(self, value):
        if not self.is_full:
            self.box[self.current_num] = value
            self.current_num += 1
        else:
            raise Exception("list is overflow")

    def pop(self, index=-1):
        if not isinstance(index, int):
            raise TypeError
        if self.current_num <= 0:
            raise IndexError("pop is empty list")
        elif index == -1:
            self.box[self.current_num - 1] = None
            self.current_num -= 1
        else:
            for i in range(index, self.current_num):
                self.box[i] = self.box[i + 1]
            self.current_num -= 1

    def find_index(self, value: int, index=0):
        for i in range(index, self.current_num):
            if self.box[i] == value:
                return i
        raise ValueError(f"{value} cant find")

    def find_value(self, index):
        if not isinstance(index, int):
            raise TypeError
        if index <= self.current_num:
            return self.box[index]


if __name__ == '__main__':
    list = LineTable()
    list.append(1)
    list.append(2)
    list.append(3)
    list.insert(1, 21)
    list.pop()
    print(list)
    print(list.find_index(2))

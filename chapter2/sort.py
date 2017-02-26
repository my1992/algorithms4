class Sort(object):
    """
    定义排序算法需要使用的通用方法
    """
    def less(self, v, w):
        return v - w < 0

    def exch(self, a, i, j):
        t = a[i]
        a[i] = a[j]
        a[j] = t

    def show(self, a):
        p = ''
        for i in range(len(a)):
            p += str(a[i]) + ' '
        print(p)
        print()

    def is_sorted(self, a):
        for i in range(1, len(a)):
            if self.less(a[i], a[i-1]):
                return False
        return True


class Selection(Sort):
    """
    选择排序
    """
    def __init__(self, a):
        self.a = a

    def sort(self):
        N = len(self.a)
        for i in range(N):
            min_index = i
            for j in range(i+1, N):
                if self.less(self.a[j], self.a[min_index]):
                    min_index = j
            self.exch(self.a, i, min_index)

    def main(self):
        self.sort()
        assert self.is_sorted(self.a)
        self.show(self.a)


class Insertion(Sort):
    """
    插入排序
    """
    def __init__(self, a):
        self.a = a

    def sort(self):
        N = len(self.a)
        for i in range(N):
            for j in range(i, 0, -1):
                if not self.less(a[j], a[j-1]):
                    continue
                self.exch(self.a, j, j-1)

    def main(self):
        self.sort()
        assert self.is_sorted(self.a)
        self.show(self.a)


if __name__ == '__main__':
    a = [1, -1, 1, 2, 10, -2]
    sort = Insertion(a)
    sort.main()

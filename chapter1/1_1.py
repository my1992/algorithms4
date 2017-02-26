import math


def inverse_rank(a):
    """
    点到一个list的元素
    :param a:
    :return:
    """
    n = len(a)
    for i in range(int(n/2)):
        temp = a[i]
        a[i] = a[n-1-i]
        a[n-1-i] = temp

    return a


def abs(x):
    """
    计算一个数的绝对值
    :param x:
    :return:
    """
    if x < 0.0:
        return -x
    else:
        return x


def is_prime(x):
    """
    判断一个数是不是素数
    :param x:
    :return:
    """
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if i * i > x:
                break
            if x % i == 0:
                return False
        return True


def sqrt(x):
    """
    牛顿法球平方根
    :param x:
    :return:
    """
    if x < 0:
        return math.nan
    err = 10e-5
    t = x
    while math.fabs(t - x/t) > err * t:
        t = (x/t + t) / 2.0
    return t


if __name__ == '__main__':
    print(sqrt(3))
def gcd(p, q):
    """
    欧几里得算法:查找两个数的最大公约数
    :param p:
    :param q: 
    :return:
    """
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


if __name__ == '__main__':
    r = gcd(3, 2)
    print(r)

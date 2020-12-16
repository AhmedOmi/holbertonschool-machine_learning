#!/usr/bin/env python3

"""
create class Poisson
"""


class Poisson:
    """
    create a constructor
    """
    def __init__(self, data=None, lambtha=1.):
        """function init"""
        self.data = data
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 3:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)

    def factor(self, n):
        """ calculates the factorial of n"""
        self.n = n
        fac = 1
        if self.n == 0:
            return 1
        for i in range(1, self.n + 1):
            fac *= i
        return fac

    def pmf(self, k):
        """function to calculate the value of pmf """
        self.k = int(k)
        exp = 2.7182818285
        if self.k < self.lambtha:
            return 0
        return self.lambtha ** self.k * exp ** \
            (-self.lambtha) / self.factor(self.k)

    def cdf(self, k):
        """ calculates the cdf"""
        e = 2.7182818285
        self.lambtha
        k = int(k)
        if k < self.lambtha:
            return 0
        s = 0
        for x in range(k + 1):
            s = s + (e ** (-self.lambtha) * self.lambtha ** x / self.factor(x))
        return s

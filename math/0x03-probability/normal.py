#!/usr/bin/env python3

"""
class normal for normal distribuation
"""


class Normal:
    """constructor of normal"""

    def __init__(self, data=None, mean=0., stddev=1.):
        self.data = data
        if data is None:
            self.mean = float(mean)
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 3:
                raise ValueError("data must contain multiple values")
            else:
                self.mean = sum(data) / len(data)
                deviations = [(x - self.mean) ** 2 for x in data]
                self.stddev = (sum(deviations) / len(data)) ** (1 / 2)

    def z_score(self, x):
        """function to calculate z score"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """function to calculate x value"""
        return z * self.stddev + self.mean

    def sqrt(self, x):
        """ return square"""
        return x ** (1 / 2)

    def pdf(self, x):
        """function pdf"""
        e = 2.7182818285
        p = 3.1415926536
        return e ** ((-1 / 2) * self.z_score(x) ** 2) / \
                    (self.stddev * self.sqrt(2 * p))

    def error(self, x):
        """ Calculates error"""
        pi = 3.1415926536
        one = x
        two = (x ** 3) / 3
        three = (x ** 5) / 10
        four = (x ** 7) / 42
        five = (x ** 9) / 216
        return 2 * (one - two + three - four + five) / self.sqrt(pi)

    def cdf(self, x):
        """function cdf"""
        return (1 + self.error(self.z_score(x) / self.sqrt(2))) / 2

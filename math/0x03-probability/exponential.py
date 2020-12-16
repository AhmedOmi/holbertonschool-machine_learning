#!/usr/bin/env python3

"""
create class exponential
"""


class Exponential:
    """constructor"""
    def __init__(self, data=None, lambtha=1.):
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
            else:
                self.lambtha = len(data) / sum(data)

    def pdf(self, x):
        """pdf of exponential"""
        e = 2.7182818285
        if x < 0:
            return 0
        return self.lambtha * e ** (-self.lambtha * x)

    def cdf(self, x):
        """cdf of exponential"""
        e = 2.7182818285
        if x < 0:
            return 0
        return 1 - e ** (-self.lambtha * x)

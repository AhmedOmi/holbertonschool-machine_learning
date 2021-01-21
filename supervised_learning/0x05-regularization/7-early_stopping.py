#!/usr/bin/env python3
"""early stopping """


def early_stopping(cost, opt_cost, threshold, patience, count):
    """
    :returns res count
    """
    if (opt_cost - threshold) <= cost:
        count += 1
    else:
        count = 0
    if count != patience:
        res = False
    else:
        res = True
    return (res, count)

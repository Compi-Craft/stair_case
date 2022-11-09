'''Staircase problem'''
import math
def staircase(_n: int) -> int:
    '''
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    >>> staircase(1)
    1
    >>> staircase(2)
    2
    >>> staircase(3)
    3
    >>> staircase(14)
    610
    >>> staircase(57)
    591286729879
    '''

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

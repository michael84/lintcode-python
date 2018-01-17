#!/usr/bin/env python
# coding:utf-8
# Author: Wei Tong


class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        numbers = [a, b]
        return sum(numbers)

if __name__ == '__main__':
    s = Solution()
    print(s.aplusb(3, 6))
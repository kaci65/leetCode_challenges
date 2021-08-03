#!/usr/bin/python3
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)
"""

class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 2**31 and x != (2**31 - 1):
            strX = str(x)
            ans = strX[::-1]
            return (int(ans))
        else:
            return 0

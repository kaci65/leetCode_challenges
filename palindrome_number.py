#!/usr/bin/python3
"""
Given an integer x, return true if x is palindrome integer

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        revsdX = strX[::-1]
        numX = int(revsdX)
        if x == numX:
            return 'true'

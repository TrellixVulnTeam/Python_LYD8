# -*- coding:utf-8 -*-
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
做法：f(n) = f(n-1) + f(n-2) + f(n-3) ... f(1) + f[0)
f(n) = 2f(n-1)
'''
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 1 << (number-1)
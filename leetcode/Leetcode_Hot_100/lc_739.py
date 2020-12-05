class Solution:
    def dailyTemperatures(self, T):

        res = [0] * len(T)
        #暴力
        # for i in range(len(T)):
        #     begin, end = i, i + 1
        #     while end < len(T):
        #         if T[begin] >= T[end]:
        #             end += 1
        #         else:
        #             res.append(end - begin)
        #             break
        #     if end == len(T):
        #         res.append(0)
        for i in range(len(T) - 2, -1,-1):
            j = i+1
            while j < len(T):
                if T[i] >= T[j]:
                    if res[j] == 0:
                        res[i] = 0
                        break
                    else:
                        j += res[j]
                else:
                    res[i] = j - i
                    break
        return res
s = Solution()
a = [34,34,47,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,34,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,34,34,34,34,47,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,47,34,47,47,47,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,34,34,47,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,47,47,34,34,47,34,34,47,34,47,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,47,34,34,47,47,34,34,34,34,47,47,34,47,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,34,34,34,47,34,47,34,34,47,34,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,34,47,47,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,34,47,47,34,34,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,34,34,47,47,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,34,47,47,47,34,47,34,47,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,47,34,47,34,34,34,34,34,47,47,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,47,47,47,34,34,47,47,47,34,34,34,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,34,47,34,34,47,34,34,34,34,34,47,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,47,34,34,47,47,34,34,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,47,34,47,47,34,34,34,34,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,47,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,47,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,47,34,34,34,34,47,47,47,34,47,47,34,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,47,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,34,34,34,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,34,47,34,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,34,47,34,47,34,34,34,34,47,34,34,34,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,34,34,47,47,34,34,34,34,47,34,47,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,47,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,47,34,47,34,47,34,47,47,34,34,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,47,47,34,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,47,34,34,47,34,34,34,47,47,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,34,47,34,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,34,47,47,47,47,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,47,47,34,34,47,47,34,34,47,47,34,47,47,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,34,34,34,34,47,47,47,47,47,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,47,34,34,47,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,34,47,47,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,34,34,34,34,47,34,34,34,47,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,47,47,47,34,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,47,34,34,34,34,47,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,47,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,47,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,34,47,47,47,34,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,47,47,34,34,34,47,34,34,47,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,47,34,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,34,34,34,34,34,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,34,47,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,34,34,34,34,34,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,34,34,47,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,47,34,47,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,47,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,34,47,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,34,47,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,47,34,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,47,47,34,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,47,47,34,34,47,34,34,47,47,34,34,47,34,47,47,34,34,47,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,34,47,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,34,34,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,34,34,47,47,47,47,34,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,47,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,34,34,34,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,34,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,47,47,47,34,34,34,47,47,47,47,34,47,47,47,34,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,47,47,34,34,34,47,47,47,34,34,34,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,47,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,47,47,47,47,47,47,47,47,47,34,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,34,47,34,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,34,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,34,47,47,34,34,34,47,47,34,34,34,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,47,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,34,47,47,47,47,34,34,47,47,47,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,34,34,47,47,34,47,47,34,34,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,47,47,47,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,34,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,34,47,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,47,34,34,47,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,47,47,47,34,34,47,47,47,34,34,47,47,47,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,34,47,47,34,47,34,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,34,34,47,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,34,34,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,34,34,34,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,34,47,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,34,47,34,47,47,34,47,47,47,47,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,47,47,34,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,34,47,47,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,34,34,34,47,47,47,34,34,47,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,34,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,34,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,47,47,47,34,47,34,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,47,34,34,34,47,47,34,34,34,47,47,34,34,47,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,47,47,47,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,34,47,47,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,34,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,47,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,47,47,34,47,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,47,34,34,34,34]
print(s.dailyTemperatures(a))
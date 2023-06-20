class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        sum = 0
        max_sum = 0
        sub = []
        max_sub = []
        for i in A:
            if i >= 0:
                sum += i
                sub.append(i)
            else:
                sum = 0
                sub = []

            if max_sum <= sum:
                max_sum = sum
                max_sub = sub

        return max_sub


print(Solution().maxset([756898537, -1973594324, -2038664370, -184803526, 1424268980]))

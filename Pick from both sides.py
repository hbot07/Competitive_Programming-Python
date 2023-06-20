class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sum_from_left = 0
        sum_from_right = sum(A[-B:])
        max_total_sum = sum_from_right
        for i in range(1, B+1):
            elements_taken_from_left = i
            elements_taken_from_right = B - i

            sum_from_left = sum_from_left + A[elements_taken_from_left-1]
            sum_from_right = sum_from_right - A[-elements_taken_from_right-1]

            total_sum = sum_from_left + sum_from_right

            if total_sum > max_total_sum:
                max_total_sum = total_sum

        return max_total_sum



print(Solution().solve(
    [-533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396,
     902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322,
     -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35], 48))

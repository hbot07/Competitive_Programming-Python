from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(target - position[i], speed[i]) for i in range(len(position))]
        cars.sort()
        time = [cars[i][0]/cars[i][1] for i in range(len(position))]
        stack = [time[0]]
        for i in time:
            if i > stack[-1]:
                stack.append(i)
        return len(stack)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(Solution().carFleet(target, position, speed))

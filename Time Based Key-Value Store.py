import bisect


class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        if len(self.d[key]) == 0:
            return ""
        i = bisect.bisect_left(self.d[key], (timestamp, ))
        if i == len(self.d[key]):
            i -= 1
        else:
            if self.d[key][i][0] > timestamp:
                if i == 0:
                    return ""
                i -= 1
        return self.d[key][i][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
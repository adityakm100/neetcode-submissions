class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        left = 0
        right = len(self.time_map[key]) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            item = self.time_map[key][mid]
            if timestamp == item[0]:
                return item[1]
            elif item[0] < timestamp:
                res = item[1]
                left = mid + 1
            else:
                right = mid - 1
        return res
            

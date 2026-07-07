class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list) #hashmap with default value of an empty list, key: key, value: pair of [timestamp stored, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value]) #add value into hashmap, no need to check for the edge case, thats what defaultdict allows for

    def get(self, key: str, timestamp: int) -> str:
        left = 0 #left pointer
        right = len(self.time_map[key]) - 1 #right pointer
        res = "" #result, default value is empty, but there could be a partial value that works

        while left <= right:
            mid = (left + right) // 2 #compute mid
            item = self.time_map[key][mid] #find the item there
            if timestamp == item[0]: #if they're even, just return that one
                return item[1]
            elif item[0] < timestamp: #if the item's timestamp stored is less than the one being asked, it could be a potential option, store it, but move the left pointer to that next value to see if we can get a better value
                res = item[1]
                left = mid + 1
            else: #move the right value in, its too far
                right = mid - 1
        return res #either empty or a partial value, the true value is returne
            

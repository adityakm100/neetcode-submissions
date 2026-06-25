class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed))

        time = [0] * len(pairs)
        for i in range(len(pairs)):
            time[i] = float((target - pairs[i][0]) / pairs[i][1])
        
        for i in range(len(time) - 1, -1, -1):
            if stack and time[i] <= stack[-1]:
                continue
            stack.append(time[i])
        return len(stack)

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map[key]
        result = ""
        left,right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                left = mid + 1
            else:
                right = mid -1
        return result
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] # tracks highest temp by index
        result = [0] * len(temps) # counts

        for i in range(len(temps)):
            if not stack: 
                stack.append(i)
                continue
            if temps[stack[-1]] < temps[i]:
                while stack and temps[stack[-1]] < temps[i]:
                    index = stack.pop()
                    result[index] = i - index
            stack.append(i)        
        return result

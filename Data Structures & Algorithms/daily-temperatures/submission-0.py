class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                result[stack.pop()] = i-stack[-1]
            stack.append(i)
            
        return result


        
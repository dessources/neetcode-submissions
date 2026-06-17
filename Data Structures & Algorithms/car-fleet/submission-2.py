class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(list(zip(position,speed)), reverse=True)
        cur_time = 0
        fleets = 0
        for car in cars:
            time = (target-car[0])/ car[1]
            if time  > cur_time:
                fleets +=1
                cur_time = time
        return fleets

        
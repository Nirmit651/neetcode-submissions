class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:     
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleets = []

        for pos, spd in cars:
            currentTime = (target - pos) / spd
            if(len(fleets) == 0 or currentTime > fleets[-1]):
                fleets.append((target - pos) / spd)


        return len(fleets)


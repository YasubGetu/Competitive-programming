class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        together = []
        
        for i in range (len (speed)):
            together.append([position[i] , speed[i]])
        together.sort() 
        
        for i in range (len(speed)):
            while fleets and fleets[-1] <= ((target - together[i][0]) / together[i][1]):
                fleets.pop()
            fleets.append((target - together[i][0]) / together[i][1])

        return len(fleets)
            

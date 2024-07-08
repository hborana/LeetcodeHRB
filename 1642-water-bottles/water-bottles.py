class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        totalDrank = numBottles  
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange  
            totalDrank += newBottles 
            numBottles = newBottles + (numBottles % numExchange)  
        return totalDrank
        
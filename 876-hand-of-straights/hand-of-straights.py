from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        sort = sorted(count.keys())

        for key in sort:
            if count[key] > 0 :
                num_needed = count[key]
                for i in range(groupSize):
                    if count[key + i] < num_needed:
                        return False
                    count[key + i] -= num_needed
        
        return True 

        
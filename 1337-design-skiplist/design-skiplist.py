class Skiplist:

    def __init__(self):
        self.d = defaultdict(int)        

    def search(self, target: int) -> bool:
        
        if self.d[target] > 0:
            return True
        return False

    def add(self, num: int) -> None:
        self.d[num] += 1

    def erase(self, num: int) -> bool:
        if num in self.d:
            if self.d[num] > 0:
                self.d[num] -= 1
                return True
            else:
                return False
        return False



# Example usage:
# skiplist = Skiplist()
# skiplist.add(1)
# skiplist.add(2)
# skiplist.add(3)
# print(skiplist.search(0))  # Output: False
# skiplist.add(4)
# print(skiplist.search(1))  # Output: True
# skiplist.add(5)
# print(skiplist.search(3))  # Output: True
# print(skiplist.search(6))  # Output: False
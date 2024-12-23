# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = [root]
        
        while queue:
            n = len(queue)
            res = []
            
            for i in range(n):
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            temp = sorted(res)
            dic = {val: idx for idx, val in enumerate(temp)}
            vis = [0] * len(res)
            
            for j in range(len(res)):
                cnt = 0
                while not vis[j] and j != dic[res[j]]:
                    vis[j] = 1
                    cnt += 1
                    j = dic[res[j]]
                ans += max(0, cnt - 1)
        
        return ans
        # def min_swaps_to_sort(arr):
        #     n = len(arr)
        #     indexed_arr = list(enumerate(arr))
        #     indexed_arr.sort(key=lambda x: x[1])  # Sort by values
        #     visited = [False] * n
        #     swaps = 0
            
        #     for i in range(n):
        #         if visited[i] or indexed_arr[i][0] == i:
        #             continue
        #         cycle_size = 0
        #         x = i
        #         while not visited[x]:
        #             visited[x] = True
        #             x = indexed_arr[x][0]
        #             cycle_size += 1
        #         if cycle_size > 1:
        #             swaps += cycle_size - 1
            
        #     return swaps

        # if not root:
        #     return 0
        
        # queue = deque([root])
        # total_swaps = 0
        
        # while queue:
        #     level_size = len(queue)
        #     level_values = []
            
        #     for _ in range(level_size):
        #         node = queue.popleft()
        #         level_values.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     # Pass the collected level_values to min_swaps_to_sort
        #     total_swaps += min_swaps_to_sort(level_values)
        
        # return total_swaps

        
               
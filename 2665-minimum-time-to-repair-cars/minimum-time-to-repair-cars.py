class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_all_cars(time):
            total_cars = 0
            for rank in ranks:
                max_cars = int((time / rank) ** 0.5)  # n such that rank * n^2 <= time
                total_cars += max_cars
                if total_cars >= cars:
                    return True
            return False

        left, right = 1, min(ranks) * cars * cars  # Upper bound assumption
        while left < right:
            mid = (left + right) // 2
            if can_repair_all_cars(mid):
                right = mid  # Try to find a smaller valid time
            else:
                left = mid + 1  # Increase time since `mid` is too small
        return left
            
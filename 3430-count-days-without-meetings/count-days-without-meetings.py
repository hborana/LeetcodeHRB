class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        # Sort the meetings based on start day
        meetings.sort()
        
        merged = []
        for meeting in meetings:
            if not merged:
                merged.append(meeting)
            else:
                last_start, last_end = merged[-1]
                current_start, current_end = meeting
                if current_start <= last_end + 1:
                    # Overlapping or adjacent, merge them
                    new_start = last_start
                    new_end = max(last_end, current_end)
                    merged[-1] = [new_start, new_end]
                else:
                    merged.append(meeting)
        
        total_meeting_days = 0
        for interval in merged:
            start, end = interval
            total_meeting_days += end - start + 1
        
        free_days = days - total_meeting_days
        return free_days if free_days >= 0 else 0
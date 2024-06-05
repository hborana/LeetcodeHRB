class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize a list to store the minimum frequency of each character (a-z)
        min_freq = [float('inf')] * 26
        
        # Iterate through each word in the list
        for word in words:
            # Initialize a list to count the frequency of each character in the current word
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            # Update the minimum frequency for each character
            for i in range(26):
                min_freq[i] = min(char_count[i], min_freq[i])
        
        # Prepare the result list based on the minimum frequencies
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * min_freq[i])
        
        return result

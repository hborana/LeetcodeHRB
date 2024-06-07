class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort the dictionary by the length of the roots
        dictionary.sort(key=len)
        
        def replace(word):
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word
        
        words = sentence.split()
        replaced_sentence = ' '.join(map(replace, words))
        return replaced_sentence
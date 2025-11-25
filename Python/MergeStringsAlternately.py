class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for a, b in zip(word1, word2): # zip handles any alternating
            merged.append(a)
            merged.append(b)
        merged.append(word1[len(word2):]) # append any additional from word1 
        merged.append(word2[len(word1):]) # append any additional from word2
        return "".join(merged)
    # Very simple to understand, zip pairs up the words by their index, allowing us to traverse them simultaneously at the same location
    # Append word1's letter first, then word2's
    # After loop ends,
    # Whoever has a shorter length (word1 or word2) will have their length used as the starting index of the slicing
    # The one with a longer length will still be used for the slicing but will yield zero appending due to being out of bounds
    # Hence, both execute but only one has any actual impact. We effectively add the excess characters
    # Note we can do it for both because Python's slicing syntax is forgiving
# Runtime 115 ms Beats 54.72%
# Memory 21.6 MB Beats 22.46%

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26  # Create a count list for each word a-z lowercase

            for char in word:
                # Count the frequency of each character, for a its a-a=0, b-a=1, c-a=2 etc.
                count[ord(char) - ord('a')] += 1

            result[tuple(count)].append(word)  # Use the count list as a key in the dictionary

        return list(result.values())

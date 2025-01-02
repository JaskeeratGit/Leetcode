class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for string in strs:
            key = [0]*26
            for character in string:
                key[ord(character) - ord('a')] += 1
            if tuple(key) in anagramDict:
                anagramDict[tuple(key)].append(string)
            else:
                anagramDict[tuple(key)] = [string]
        return anagramDict.values()

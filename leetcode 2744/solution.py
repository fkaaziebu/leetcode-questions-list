class Solution:
    def maximumNumberOfStringPairs(self, words) -> int:
        hashset = set()
        res = 0

        for word in words:
            if tuple(sorted(word)) in hashset:
                res += 1
                continue
            hashset.add(tuple(sorted(word)))

        return res


obj = Solution()
words = ["cd", "ac", "dc", "ca", "zz"]
print(obj.maximumNumberOfStringPairs(words))

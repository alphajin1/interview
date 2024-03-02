class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i, v in enumerate(s):
            result += self.countPalindromes(s, i, i)
            result += self.countPalindromes(s, i, i + 1)

        return result

    def countPalindromes(self, s, i, j) -> int:  # 가운데에서 부터 점검하는 방법
        result = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            result += 1
            i -= 1
            j += 1

        return result

# TODO 정답을 보았음.
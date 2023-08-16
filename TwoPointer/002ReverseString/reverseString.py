class Solution:
    def reverseString(self, s):
        low, high = 0, len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        return s

if __name__ == '__main__':
    case = Solution()
    s = list('abc')
    print(case.reverseString(s))

    s = list('hello')
    print(case.reverseString(s))

    s = list('Hannah')
    print(case.reverseString(s))
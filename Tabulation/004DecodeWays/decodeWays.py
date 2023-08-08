class Solution():
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def decodings(self,s: str):
        if s[0] == '0': return 0
        prev, curr = 1, 1
        for i in range(1,len(s)):
            temp = 0
            if 9 < int(s[i-1:i+1]) < 27:
                temp = prev
            prev = curr
            if s[i] == '0':
                curr = temp
            else:
                curr += temp
        return curr
    
if __name__ == '__main__':
    from random import randint
    ans = Solution()

    s = ''
    for i in range(1):
        s += str(randint(0,9))
    print(s)
    print("Result: ",ans.decodings(s),'\n')

    s = ''
    for i in range(5):
        s += str(randint(0,9))
    print(s)
    print("Result: ",ans.decodings(s),'\n')

    s = ''
    for i in range(10):
        s += str(randint(0,9))
    print(s)
    print("Result: ",ans.decodings(s),'\n')

    s = ''
    for i in range(15):
        s += str(randint(0,9))
    print(s)
    print("Result: ",ans.decodings(s),'\n')
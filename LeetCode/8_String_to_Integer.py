class Solution:
    def myAtoi(self, s: str) -> int:
        
        sign_check = False
        answer = ''
        def backtracking(result, s):
            
            nonlocal sign_check, answer
            # Conversion
            if not s:
                answer = result
                return

            # whitespace
            elif s[0] == " " and not sign_check:
                backtracking(result, s[1:])

            # sign_check
            elif (s[0] == '-' or s[0] == "+") and not sign_check:
                sign_check = True
                backtracking(result + s[0], s[1:])
            
            # digit_check
            elif '0' <= s[0] <= '9':
                sign_check = True
                backtracking(result + s[0], s[1:])
            
            else:
                backtracking(result, "")
        
        backtracking("", s)

        if answer == "" or answer == "-" or answer == "+":
            return 0
        else:
            return max(min(int(answer), 2**31-1), -2**31)
            
s = Solution()
print( s.myAtoi("42") )
print( s.myAtoi(" -042") )
print( s.myAtoi("1337c04b2") )
print( s.myAtoi("0-1") )
print( s.myAtoi("words and 987"))
print( s.myAtoi("+-12"))
print( s.myAtoi("   +0 123"))
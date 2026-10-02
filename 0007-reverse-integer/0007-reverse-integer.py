class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2147483648,2147483647
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0 

        while x != 0:
            digit = x % 10
            x //= 10 
            if reverse > INT_MAX // 10 or (reverse == INT_MAX // 10 and digit > 7):
                 if sign == -1 and reverse == INT_MAX // 10 and digit == 8:
                    reverse = reverse * 10 + digit
                    break
                 return 0

            reverse = reverse * 10 + digit
            
        return reverse * sign
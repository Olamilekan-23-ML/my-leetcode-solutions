class Solution(object):
    def letterCombinations(self, digits):
        # Return an empty list if the input string is empty
        if not digits:
            return []
        # Creating a telephone dictionary
        phone = {
            '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
            '7':'pqrs','8':'tuv','9':'wxyz'
        }
        # Initialize an empty list 
        combinations = []
        # define a function backtrack
        def backtrack(index, current_path):
            # if the current combination is the same length as the digits then we join the letter
            if len(current_path) == len(digits):
                combinations.append("".join(current_path))
                return
            possible_letters = phone[digits[index]]
            # Loop through the letter and recurse
            for letter in possible_letters:
                current_path.append(letter)
                backtrack(index + 1, current_path)
                current_path.pop()
        
        backtrack(0, [])
        return combinations
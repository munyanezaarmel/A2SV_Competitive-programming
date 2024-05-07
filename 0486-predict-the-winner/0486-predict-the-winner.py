class Solution:
    def predictTheWinner(self, nums):
        def rec(arr, score1, score2, turn):
            if not arr: 
                if score1 >= score2:
                    return "player1"
                return "player2"
            if turn:
                branch1 = rec(arr[1:], score1 + arr[0], score2, False)
                branch2 = rec(arr[:-1], score1 + arr[-1], score2, False)
                if branch1 == branch2 == "player2":
                    return "player2"
                return "player1"
            else:
                branch1 = rec(arr[1:], score1, score2 + arr[0], True)
                branch2 = rec(arr[:-1], score1, score2 + arr[-1], True)
                if branch1 == branch2 == "player1":
                    return "player1"
                return "player2"
        
        return rec(nums, 0, 0, True) == "player1"
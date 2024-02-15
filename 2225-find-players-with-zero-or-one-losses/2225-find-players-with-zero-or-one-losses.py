class Solution(object):
    def findWinners(self, matches):
        winners = {}
        losers = {}
        w=[]
        l=[]
        arr=[w]+[l]
        for match in matches:
            winner, loser = match  
            winners[winner] = winners.get(winner, 0) + 1
            losers[loser] = losers.get(loser, 0) + 1

        for keys,values in winners.items():
            if(keys not in losers):
                w.append(keys)
        for keys,values in losers.items():
              if values<2:
                l.append(keys)
        w.sort()
        l.sort()

        return arr

        
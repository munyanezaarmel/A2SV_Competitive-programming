class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        first = 0
        second = 0
        count = 0
        trainers.sort()
        players.sort()

        while first < len(players) and second < len(trainers):
                if players[first] <= trainers[second]:
                        count += 1
                        first += 1
                        second+=1
                       
                else:
                        second += 1

        return count
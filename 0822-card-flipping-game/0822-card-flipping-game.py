class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same_card_indices = { i for i,j in zip(fronts,backs) if i==j}
        
        return min( [ el for el in fronts+backs if el not in same_card_indices ] or [0])

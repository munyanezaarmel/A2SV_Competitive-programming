class Solution(object):
  def pivotIndex(self, nums):
    """
    Finds the pivot index in an array where left and right sums are equal.

    Args:
        nums: A list of integers.

    Returns:
        The index of the pivot element, or -1 if no pivot exists.
    """

    left_sum, right_sum = 0, sum(nums)

    for idx, ele in enumerate(nums):
      right_sum -= ele

      if left_sum == right_sum:
        return idx

      left_sum += ele

    return -1
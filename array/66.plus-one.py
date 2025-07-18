#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            if i == 0:
                return [1] + digits

        
# @lc code=end


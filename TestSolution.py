from unittest import TestCase
from Solution import Solution
from Solution import ListNode


class TestSolution(TestCase):

    solution = Solution()

    def testMyAtio(self):
        num = self.solution.myAtoi('')
        self.assertEqual(0, num)

        num = self.solution.myAtoi('42')
        self.assertEqual(42, num)

        num = self.solution.myAtoi('    -42')
        self.assertEqual(-42, num)

        num = self.solution.myAtoi('4193 with words')
        self.assertEqual(4193, num)

        num = self.solution.myAtoi('words and 987')
        self.assertEqual(0, num)

        num = self.solution.myAtoi('-91283472332')
        self.assertEqual(-2147483648, num)

    def testLengthOfLongestSubstring(self):
        len1 = self.solution.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, len1)

        len2 = self.solution.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(1, len2)

        len3 = self.solution.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, len3)

        len4 = self.solution.lengthOfLongestSubstring("abcabzw")
        self.assertEqual(5, len4)

    def testMultiply(self):
        num1 = self.solution.multiply("2", "3")
        self.assertEqual("6", num1)

        num2 = self.solution.multiply("123", "456")
        self.assertEqual("56088", num2)

        num3 = self.solution.multiply("1", "000")
        self.assertEqual("0", num3)

        num4 = self.solution.multiply("4", "123456789")
        self.assertEqual("493827156", num4)


    def testAddTwoNumbers(self):
        l1 = self.__buildList(2, 4, 9)
        l2 = self.__buildList(5, 6, 4, 9, 9)

        lRes = self.__buildList(7, 0, 4, 0, 0, 1)

        solRes = self.solution.addTwoNumbers(l1, l2)

        self.assertTrue(lRes.equals(solRes))
        # self.assertEqual(lRes.val, solRes.val)
        # self.assertEqual(lRes.next.val, solRes.next.val)
        # self.assertEqual(lRes.next.next.val, solRes.next.next.val)


    #region Private Methods
    def __buildList(self, *nums):
        head = ListNode(0)
        currentNode = head
        for i in range(len(nums)):
            currentNode.next = ListNode(nums[i])
            currentNode = currentNode.next

        head = head.next
        return head
    #endregion

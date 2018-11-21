from unittest import TestCase
from Solution import Solution
from Solution import ListNode


class TestSolution(TestCase):

    solution = Solution()

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

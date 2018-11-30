class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lettersSoFar = set()
        maxCounter = 0
        currentCounter = 0
        startIndex = 0
        for i in range(len(s)):
            while lettersSoFar.__contains__(s[i]):
                lettersSoFar.remove(s[startIndex])
                startIndex += 1
                currentCounter -= 1

            currentCounter += 1
            lettersSoFar.add(s[i])
            if currentCounter > maxCounter:
                maxCounter = currentCounter

        return maxCounter


    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        finalNumber = 0
        currentDigitCount = 0
        for i in range(len(num2)-1, -1, -1):
            finalNumber += self.__multiplyNumberDigit(num1, num2[i]) * pow(10, currentDigitCount)

            currentDigitCount += 1

        return str(finalNumber)


    def __multiplyNumberDigit(self, num, digit):
        carry = 0
        finalNumber = 0
        currentDigitCount = 0
        for i in range(len(num)-1, -1, -1):
            currNum = (int(num[i]) * int(digit)) + carry
            finalNumber += (currNum % 10) * pow(10, currentDigitCount)
            carry = currNum // 10

            currentDigitCount += 1
        finalNumber += carry * pow(10, currentDigitCount)

        return finalNumber


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currentNode = ListNode(0)
        head = currentNode
        carry = 0
        while l1 is not None and l2 is not None:
            nextDigit = l1.val + l2.val + carry
            if nextDigit > 9:
                carry = 1
                nextDigit = nextDigit % 10
            else:
                carry = 0

            currentNode.next = ListNode(nextDigit)
            currentNode = currentNode.next

            l1 = l1.next
            l2 = l2.next

        rest = None
        if l1 is not None:
            rest = l1
        elif l2 is not None:
            rest = l2

        while (rest is not None):
            nextDigit = rest.val + carry
            if nextDigit > 9:
                carry = 1
                nextDigit = nextDigit % 10
            else:
                carry = 0

            currentNode.next = ListNode(nextDigit)
            currentNode = currentNode.next

            rest = rest.next

        if carry == 1:
            currentNode.next = ListNode(1)

        head = head.next
        return head




#region Aux types
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def equals(self, list):
        currentList = self
        while list is not None and currentList is not None:
            if currentList.val != list.val:
                return False
            list = list.next
            currentList = currentList.next
        if currentList is not None or list is not None:
            return False
        return True

#endregion
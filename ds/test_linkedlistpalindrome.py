import unittest
from linkedlistpalindrome import *

class TestLinkedListPalindrome(unittest.TestCase):
    def test_1_isLinkedListPalindrome(self):
        """
        Test case for the `isLinkedListPalindrome` function with a Palindrome Linked List.
        """
        palin3 = Node(10, None)
        palin2 = Node(20, palin3)
        palin1 = Node(10, palin2)

        self.assertTrue(isLinkedListPalindrome(palin1), "Should be True")

    def test_2_isLinkedListPalindrome(self):
        """
        Test case for the `isLinkedListPalindrome` function with a Non-Palindrome Linked List.
        """
        notpalin4 = Node(40, None)
        notpalin3 = Node(10, notpalin4)
        notpalin2 = Node(30, notpalin3)
        notpalin1 = Node(10, notpalin2)

        self.assertFalse(isLinkedListPalindrome(notpalin1), "Should be False")
        
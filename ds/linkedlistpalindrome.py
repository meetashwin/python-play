# Check if given linkedlist is a palindrome or not.

class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

def isLinkedListPalindrome(head):
	"""
	Check if a linked list is a palindrome.

	Parameters:
	- head: The head node of the linked list.

	Returns:
	- isReverse: A boolean indicating whether the linked list is a palindrome or not.
	"""
	tempList = []
	isReverse = False

	while(head != None):
		tempList.append(head.data)
		head = head.next

	if (tempList == tempList[::-1]):
		isReverse = True
	else:
		isReverse = False

	return(isReverse)


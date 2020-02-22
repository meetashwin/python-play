#Your task is to check if given linkedlist is a pallindrome or not.

class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

palin3 = Node(10, None)
palin2 = Node(20, palin3)
palin1 = Node(10, palin2)

notpalin4 = Node(40, None)
notpalin3 = Node(10, notpalin4)
notpalin2 = Node(30, notpalin3)
notpalin1 = Node(10, notpalin2)

def isLinkedListPalindrome(head):
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

if (isLinkedListPalindrome(palin1) == True):
	print("Yes, the LL  is a palindrome")
else:
	print("No, the LL  is not a palindrome")

if (isLinkedListPalindrome(notpalin1) == True):
	print("Yes, the LL is a palindrome")
else:
	print("No, the LL  is not a palindrome")

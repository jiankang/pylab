#!/usr/local/bin/python3

import random

class Solution(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		temp1=head
		prev = None
		if (head != None and head.next != None):
			head = temp1.next
		
		while (temp1 != None and temp1.next!=None):
			temp2 = temp1.next
			if prev != None:
				prev.next = temp2
			temp1.next = temp2.next
			temp2.next = temp1
			prev = temp1
			temp1 = temp1.next

		return head

def buildList(nodeCount):
	
	if nodeCount == 0:
		return None

	s2 = None
	for i in range(nodeCount,0,-1):
		s1=Solution(random.randint(0,100))
		if (s2 != None):
			s1.next = s2
		s2 = s1
	return s1

def printList(head):
	temp = head
	while temp != None:
		if(temp.next != None):
			print(temp.val,'->',sep='',end='')
		else:
			print(temp.val,sep='')
		temp = temp.next

#test code
#nodeCount=random.randint(0,100)
for i in range(10):
	head = buildList(i)
	printList(head)
	head = Solution(0).swapPairs(head)
	printList(head)

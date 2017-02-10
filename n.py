#!/usr/local/bin/python3

'''
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: integers
		:type: List[int]
		"""
		#1
		'''
		#indices=[[nums.index(a),nums.index(target-a)] for a in nums if target-a in nums and nums.index(a) < nums.index(target-a)]
		#indices=[[idx_a,idx_b] for idx_a in range(len(nums)) for idx_b in range(len(nums)) if nums[idx_a] + nums[idx_b] == target and idx_a < idx_b]
		#if len(indices)>0:
		#	return indices[0]
		#else:
		#	return []
		'''

		#2
		'''
		#for i in range(len(nums)):
		#	for j in range(len(nums)):
		#		if i == j: continue
		#		if nums[i] + nums[j] == target:
		#			return [i,j]

		#return []
		'''

		#3
		'''
		for i in range(len(nums)):
			try:
				j = nums.index(target - nums[i])
				if i != j:
					return [i,j]
			except:
				continue

		return []
		'''

		#4
		d = {}
		for i in range(len(nums)):
			if target - nums[i] in d and d[target - nums[i]] != i:
				return [d[target - nums[i]],i]
			d[nums[i]] = i
		return []

nums=[a*2 for a in range(100000)]
sl = Solution()
print(sl.twoSum(nums,390000))
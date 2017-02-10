#!/usr/bin/env python3

#encoding=utf-8
nums=[]
try:
	for i in range(4):
		nums.append(int(input("please input 4 numbers,[{0}]:".format(i))))
except ValueError:
	print("please supply integer arguments")
	exit()
	

ops=['+','-','*','/']

print("发到手的牌是:{0},运算符是:{1}".format(nums,ops))



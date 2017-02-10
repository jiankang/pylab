#!/usr/local/bin/python3
import argparse

parser = argparse.ArgumentParser(description="打印乘法表")
parser.add_argument("-n", metavar='N', default=10, type=int,
                        help="打印NxN乘法表")

args = parser.parse_args()
n = args.n

for i in range(1,n):
	for j in range(1,i+1):
		print("{0:12}".format("{0}x{1}={2}".format(j,i,i*j)),end='')
	print('')

#!/usr/bin/env python
#coding=utf-8
num=1
for x in range(1,11):#x為三角形的行數,10行
	for y in range(0,x):#y為每一排的數字數量，第幾行就幾個數字
		print num,
		print ' ',
		num=num+1
	print '\n'#一行結束後再換行
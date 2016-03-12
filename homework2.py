#!/usr/bin/env python
#coding=utf-8
while 1:#無限迴圈
	print '--Prime number system--'
	num=input('Input a number >= 2:')
	if num<2:
		print 'Please input a number >=2'+'\n'
		continue #繼續迴圈
	true=1 #先視num為質數
	for x in range(2,num):#x為2~num-1之除數
		if num%x==0:
			true=0	#一整除就判定num不為質數
	if true:
		print '%d is a prime number'%num+"\n"
	else:
		print '%d is not a prime number'%num+"\n"
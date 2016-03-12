#!/usr/bin/env python
#coding=utf-8
f=open("input.txt","r")
lines = len(f.readlines())#len()可以找到陣列中的元素數目，利用他找出文件有幾行
print "There are %d lines" %lines
f.close
f=open("input.txt","r")
e_tnum=0
s_tnum=0
tchar=0
#'e','空白鍵','字元'的總數
while lines>0:#做lines次的迴圈
	line=f.readline()#讀出文件的一行並存入line
	e_num=line.count('e')
	s_num=line.count(' ')
	print line
	print "e appear %d times."%e_num
	print "Spacebar appear %d times."%s_num
	if lines==1:#當為文件最後一行時，不考慮\n
		print "%d character"%(len(line)-s_num)#用len找出line中的元素，減掉空白鍵數目，及為字元數
	else:
		print "%d character"%(len(line)-s_num-1)#用len找出line中的元素，減掉空白鍵數目和\n，及為字元數
	print '\n'
	e_tnum=e_num+e_tnum
	s_tnum=s_num+s_tnum
	tchar=tchar+(len(line)-s_num-lines+1)
	lines=lines-1
e=float(e_tnum)
s=float(s_tnum)
c=float(tchar)
print 'Totally,e appear %d time.It is %f percent'%(e_tnum,e/c*100)
print 'Totally,Spacebar appear %d time.It is %f percent'%(s_tnum,s/c*100)
print 'Totally,%d character.'%tchar
f.close
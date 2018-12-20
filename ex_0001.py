# -*- coding: utf-8 -*
# 加入中文符号

'''
生成激活码：
位数：16位
随机大写字母和数字？
每个激活码不可以重复，但是激活码内部的东西是可以重复的
'''
"""
步骤：
1. 生成16位激活码（采用随机数？） -> import random
2. 储存生成的生成码并对应index（比如0-199的index对应不同的生成码） -> 字典（无顺序key value对应
可以直接在string里面加，神奇的python
3. 生成新的的时候在字典里面比较存不存在，历遍dict，看存的里面key存不存在

问题：
1. 生成的随机数够不够随机（基于时间的？）应该可以吧

进阶：
1. 定义一个函数实现这个功能

"""

import random


def avtivetion_code(numbers, length):
	names = {}
	for j in range(0,numbers):
		coding = ""
		for i in range(0,length):
			num = random.randint(0,9)
			# 小写字母ascii
			c_low = chr(random.randint(97,122))
			# 大写字母ascii
			c_upper = chr(random.randint(65,90))
	 
			index = random.randint(0,1)
			if index == 0:
				coding = coding + str(num)
			else:
				coding = coding + c_upper

			# 上面的问题可以统一用random.choice（list）来确定一个范围
		if coding in names:
				# print("hahaha")
			pass
		else:
			names[coding] = 1 

	for key in names:
		print key

# if __name__ == "__main__"
num = 200
length = 16
avtivetion_code(num, length)
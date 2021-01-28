#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os

inputlist = []

option_responsibility1 = ['0','1']
option_responsibility2 = ['0','1']
option_responsibility3 = ['0','1']

inputlist = []

def getResponsibility():
	# 必选责任1，有社保
	# for h in haveSocials:
	num = 0
	responsibilityCodes = []
	for a in option_responsibility3:
		for b in option_responsibility2:
			for c in option_responsibility1:
				# print c,b,a,d
				num = num + 1
				datas = [c,b,a]

				# if((int(c)|int(b))!=int(a)):
				# 	pass
				# else:
				inputlist.append([c, b, a])

				maxposition = 2
				if(c=='0'):
					datas.pop(0)
					maxposition = maxposition-1
				if(c=='1'):
					datas[maxposition-2] = 'C10012'
				if(b=='0'):
					datas.pop(maxposition-1)
					maxposition = maxposition - 1
				if(b=='1'):
					datas[maxposition-1] = 'C10013'
				if(a=='0'):
					datas.pop(maxposition)
					maxposition = maxposition - 1
				if(a=='1'):
					datas[maxposition] = 'C10014'

				# print datas
				responsibilityCodes.append(datas)
				# inputlist.append(datas)
				# if(c == '0'):
				# 	inputlist.append([b,a,d])
				# if(c == '1'):
				# 	inputlist.append(["C10012",b,a,d])
# print inputlist
# print responsibilityCodes
# print num
	print (responsibilityCodes)
	return responsibilityCodes

def get_totalfee(resp,amount,mainfee,optional1fee,optional2fee,optional3fee):


		if (resp == []):
			respect_fee = mainfee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp,respect_fee


		if (resp == ['C10012']):
			respect_fee = mainfee + optional1fee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp, respect_fee


		if (resp == ['C10013']):
			respect_fee = mainfee + optional2fee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp, respect_fee


		if (resp == ['C10014']):
			respect_fee = mainfee + optional3fee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp, respect_fee



		if (resp == ['C10012', 'C10013']):
			respect_fee = mainfee + optional2fee +  optional1fee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp, respect_fee


		if (resp == ['C10012', 'C10014']):
			respect_fee = mainfee + optional1fee +  optional3fee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp, respect_fee


		if (resp == ['C10013', 'C10014']):
			respect_fee = mainfee + optional2fee +  optional3fee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp, respect_fee



		if (resp == ['C10012', 'C10013', 'C10014']):
			respect_fee = mainfee + optional2fee +  optional3fee +  optional1fee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp, respect_fee


# if __name__ == '__main__':
# 	getResponsibility()
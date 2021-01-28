#!/usr/bin/env python
#-*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import unittest
import  utils.responsibility as res
import pyexcel as py
import requests
import json
import pdb
import copy
# from utils import send


import utils.excelUtil as ex
# import utils.plan

proDir = 'C:\Users\Administrator\Documents\Mamibaobei'
# print os.getcwd()
# print os.path.join(os.getcwd())
# print proDir
xlsxPath = os.path.join(proDir, "data", "mami2021.xlsx")
print(xlsxPath)


class TestUnderwriting(unittest.TestCase):
    """测试趸交"""

    def setUp(self):
        self.num = 0
        self.gender = ['M', 'F']
        self.productCode1 =  ['10270831']
        self.guarantee_periods = ['20','25','30','至70','至80','至105']
        self.Payment_period1 = ['1','5','10']
        self.Payment_period2 = ['1','5','10','15']
        self.Payment_period3 = ['1','5','10','15','20']
        self.Payment_period4 = ['1','5','10','15','20','30']
        self.nowamount = 100000
        # self.dict20 = dict(zip(self.guarantee_period,self.Payment_period1))
        # self.dict25 = dict(zip(self.guarantee_period,self.Payment_period2))
        # self.dict30 = dict(zip(self.guarantee_period,self.Payment_period3))
        # self.dict70 = dict(zip(self.guarantee_period,self.Payment_period4))

        self.plan = [1,2,3,4,5,6,7,8]
        self.insured_amount1 = [100000,200000,300000,500000,600000,700000,800000]
        self.insured_amount = [100000, 200000]
        self.age1 = range(0,18,1)
        self.age2 = range(18,50,1)

        plancodes = res.getResponsibility()

        # self.ages1 = ex.get_inputAge(xlsxPath, u'个人版保障利益表', 0, u"年龄段（周岁）")
        # print(ex.get_titlecolums(self.ages1))


        # # 切片前面包含，后面不包含
        # self.ages1 = self.ages[0:106]
        # self.ages2 = self.ages[0:19]

        # self.single_hasSocial = ex.readsheet(self.single_Sheet, 18, u"有社保")
        # print single_hasSocial
        # self.single_noSocial = ex.readsheet(ex.readexcel(xlsxPath, u"个人版保障利益表"), 18, u"无社保")

        # self.family_hasSocial = ex.readsheet(self.family_Sheet,18 , u"有社保")

        # self.family_noSocial = ex.readsheet(self.year_sheet3, 3, u"年交保费")
        # # 可选责任二首年保费=续年保费
        # self.option2_yearfee = ex.readsheet(self.year_sheet4, 3, u"年交保费")
        # # 可选责任三
        # self.option3_yearfee = ex.readsheet(self.year_sheet5, 3, u"首年")
        # self.option3_yearfee = ex.readsheet(ex.readexcel(xlsxPath, u"趸交费率v可选3"), 3, u"续年")

        print('test start1')

    def test_a(self):
        """测试"""
        # gole_payment = []
        for p in self.plan:
            print ("计划%d"%p)
            for g in self.gender:
                print("性别:%s" %g)
                for a in self.age1:
                    print ("年龄：%d" %a )
                    print ("*****************************************************")
                    for gu_period in self.guarantee_periods:
                        print("********* 保障期限：%s **********" %gu_period)
                        if gu_period == '20':
                            gole_payment = self.Payment_period1
                        if gu_period == '25':
                            gole_payment= self.Payment_period2
                        if gu_period == '30':
                            gole_payment = self.Payment_period3
                        else:
                            if (gu_period == ("至70" or "至80" or "至105")):
                                gole_payment = self.Payment_period4
                        # print (gole_Payment)
                        for go in gole_payment:
                            print ("*****************")
                            print ("缴费期限：%s" %go)
                            # print ('\n')
                            respect_mainfee = ex.get_mainfee(xlsxPath=xlsxPath,sheetname="mainfee",start_row=2,plan=p,gender=g,age=a,g_p=gu_period,p_p=int(go))
                            for amount in self.insured_amount:
                                # self.nowamount = amount
                                if(a<6 and amount>600000):
                                    continue
                                print("保额：%d,主险费率：%f"  %(amount,respect_mainfee*amount/1000))
                            # print ('\n')
                            respect_optional2fee =  ex.get_option_fee(xlsxPath=xlsxPath,sheetname=u'少儿意外住院津贴责任费率',start_row=1,gender=g,g_p=gu_period,p_p=int(go),age=a)
                            respect_optional3fee = ex.get_option_fee(xlsxPath=xlsxPath, sheetname=u'少儿意外医疗责任费率',
                                                                     start_row=1, gender=g, g_p=gu_period, p_p=int(go),
                             age=a)
                            print("少儿意外住院津贴责任费率:%f"%respect_optional2fee)
                            print("少儿意外医疗责任费率：%f"%respect_optional3fee)
                            # if go=="1":
                            #     for amount in self.insured_amount:
                            #         if gole_payment == 1:
                            #             print("当前保额:%f,当前总保费:%f" % (amount, respect_optional2fee + respect_optional3fee))
                            #     continue
                            if go!='1':
                                respect_optional1fee = ex.get_option_fee(xlsxPath=xlsxPath,sheetname='optional1',start_row=1,gender=g,g_p=str(int(go)-1),p_p=int(go)-1,age=a+18)
                            else:
                                respect_optional1fee = 0

                            print("投保人豁免费率：%f" %respect_optional1fee)
                            for amount in self.insured_amount:
                                if go=='1':
                                    print("当前保额:%f,当前总保费:%f" % (amount, respect_mainfee*amount/1000+respect_optional2fee + respect_optional3fee))
                                else:
                                    resps = res.getResponsibility()
                                    for resp in resps:
                                        resp,respect_tolfee = res.get_totalfee(resp=resp,amount=amount,mainfee=respect_mainfee*amount/1000, optional1fee=respect_optional1fee, optional2fee=respect_optional2fee, optional3fee=respect_optional3fee)
                                        print("当前保额:%f,当前总保费:%f" %(amount, respect_tolfee))


                        # self.assert_assertEqual(respect_optional1fee,1,msg="rewr")
                            print ('\n')
                            #
                            # retext = send.senddatas(data)
                            # print (retext.text)
                            # print (age)
                            # outputdata = json.loads(retext.text)["body"]["payment"]
                            # if (float(respect_fee) != float(outputdata)):
                            #     print (float(respect_fee), float(outputdata))
                            # with self.subTest():
                            #     self.assertEqual(float(respect_fee), float(outputdata), msg="222")



    def tearDown(self):
        print("test  end")

if __name__ == '__main__':
    unittest.main()

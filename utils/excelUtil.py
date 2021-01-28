#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import pyexcel as p
import json
import os
import copy
# from pyexcel_xlsx import save_data
# from pyexcel_xlsx import get_data
from collections import OrderedDict
# from pyexcel_xlsx import get_data
# from pyexcel_xlsx import save_data

# def get_inputAge(xlsxPath,sheetname,row_number,colum_name,start_row):
#     """取得输入的年龄值"""
#     # single_Sheet = readexcel(xlsxPath, sheetname)
#     single_Sheet = p.get_sheet(file_name=xlsxPath,sheet_name=sheetname,start_row=start_row,skip_empty_rows=True)
#     ages = readsheet(single_Sheet,row_number, colum_name)
#     ages1 = []
list_plan1 = []
list_plan2 = []
list_plan3 = []
list_plan4 = []
list_plan5 = []
list_plan6 = []
list_plan7 = []
list_plan8 = []

def get_Row(xlsxPath,sheetname,rowname,startrow):
    """取得1行"""
    single_Sheet = p.get_sheet(file_name=xlsxPath, sheet_name=sheetname, start_row=startrow, skip_empty_rows=True)
    single_Sheet.name_rows_by_column(0)
    # for row in single_Sheet.named_rows():
    #     print json.dumps(row,encoding='utf-8',ensure_ascii=False)
    # gole_list = single_Sheet.named_row_at(rowname)
    data_dict = single_Sheet.to_dict()
    return  data_dict[rowname]

def get_list(xlsxPath,sheetname,startrow):
    single_dict = p.get_book_dict(file_name=xlsxPath, sheet_name=sheetname, start_row=startrow, skip_empty_rows=True)
    row_list = single_dict[sheetname]
    # for key,item in single_dict.items():
    # 	print(json.dumps(item, ensure_ascii=False, sort_keys=False, indent=1))
    return row_list

def del_list(rowlist,g_p,gindex,p_p,pindex,age,aindex):
    golelist1 = copy.deepcopy(rowlist)
    for iterm in rowlist:
        if (str(iterm[gindex]) != g_p):
            golelist1.remove(iterm)
            # print(goleplanlist)
            continue
        if (iterm[pindex] != p_p):
            golelist1.remove(iterm)
            # print(goleplanlist)
            continue
        if (iterm[aindex] != age):
            golelist1.remove(iterm)
            # print(goleplanlist1)
            continue

    return golelist1

def get_goleplanlist(plan):
    if plan == 1:
        goleplanlist = list_plan1
    if plan == 2:
        goleplanlist = list_plan2
    if plan == 3:
        goleplanlist = list_plan3
    if plan == 4:
        goleplanlist = list_plan4
    if plan == 5:
        goleplanlist = list_plan5
    if plan == 6:
        goleplanlist = list_plan6
    if plan == 7:
        goleplanlist = list_plan7
    if plan == 8:
        goleplanlist = list_plan8
    return  goleplanlist

def get_option_fee(xlsxPath,sheetname,start_row,gender,g_p,p_p,age):

    list_M = []
    list_F = []
    row_list = get_list(xlsxPath,sheetname,start_row)
    for it in row_list:
        if(it[0]=="M"):
            list_M.append(it)
        if(it[0]=="F"):
            list_F.append(it)
        # if(it[])
    if(gender == "M"):
        golelist = list_M
    else:
        golelist = list_F


    final_list = del_list(rowlist=golelist, g_p=g_p,gindex=1, p_p=p_p, pindex=2,age=age, aindex=3)
    return final_list[0][4]

# def trans_to(xlsxPath, sheetname, start_row,group,group_index):
#     row_list = get_list(xlsxPath, sheetname, start_row)
#     row_list.pop(0)
#     i = 0
#     len(group)
#     for iterm in row_list:
#         for g in group:
#             if(iterm[group_index] == g):





def get_mainfee(xlsxPath,sheetname,start_row,plan,gender,age,g_p,p_p):
    row_list = get_list(xlsxPath,sheetname,start_row)
    row_list.pop(0)

    for item in row_list:
        if(item[4] == 1):
            list_plan1.append(item)
        if(item[4] == 2):
            list_plan2.append(item)
        if (item[4] == 3):
            list_plan3.append(item)
        if (item[4] == 4):
            list_plan4.append(item)
        if (item[4] == 5):
            list_plan5.append(item)
        if (item[4] == 6):
            list_plan6.append(item)
        if (item[4] == 7):
            list_plan7.append(item)
        if (item[4] == 8):
            list_plan8.append(item)
        else:
            pass

    goleplanlist = get_goleplanlist(plan)
    # print(goleplanlist)
    # goleplanlist1 = goleplanlist[:] 浅拷贝
    goleplanlist1 = copy.deepcopy(goleplanlist)
    for iterm in goleplanlist:

        if(iterm[0]!= gender):

            goleplanlist1.remove(iterm)
            # print(goleplanlist)
            continue
        if(str(iterm[1])!= g_p):
            goleplanlist1.remove(iterm)
            # print(goleplanlist)
            continue
        if(iterm[3]!= p_p):
            goleplanlist1.remove(iterm)
            # print(goleplanlist1)
            continue
        if(iterm[5]!= age):
            goleplanlist1.remove(iterm)
            # print(goleplanlist)
            continue
    # print(goleplanlist1)
    return goleplanlist1[0][6]
    # list_plan1.insert(0, ['性别', '保险期间', '单位', '缴费期限', '计划', '年龄','保费'])
    # list_plan2.insert(0, ['性别', '保险期间', '单位', '缴费期限', '计划', '年龄', '保费'])
    # list_plan3.insert(0, ['性别', '保险期间', '单位', '缴费期限', '计划', '年龄', '保费'])
    # list_plan4.insert(0, ['性别', '保险期间', '单位', '缴费期限', '计划', '年龄', '保费'])
    # list_plan5.insert(0, ['性别', '保险期间', '单位', '缴费期限', '计划', '年龄', '保费'])
    # list_plan6.insert(0, ['性别', '保险期间', '单位', '缴费期限', '计划', '年龄', '保费'])
    # list_plan7.insert(0, ['性别', '保险期间', '单位', '缴费期限', '计划', '年龄', '保费'])
    # list_plan8.insert(0, ['性别', '保险期间', '单位', '缴费期限', '计划', '年龄', '保费'])

    # print (list_plan1)
    # print (list_plan2)
    # print (list_plan3)
    # print (list_plan4)
    # print (list_plan5)
    # print (list_plan6)
    #
    #
    # sheetnames = ['list_plan1','list_plan2','list_plan3','list_plan4','list_plan5','list_plan6','list_plan7','list_plan8']
    # values = [list_plan1,list_plan2,list_plan3,list_plan4,list_plan5,list_plan6,list_plan7,list_plan8]
    #
    # new_tuple = zip(sheetnames,values)
    # new_dict = dict(new_tuple)
    # print (type(new_dict))
    # print (new_dict.keys())
    # for key,values in new_dict:
    #     print (key,values)
        # for value in values:
        #     print(value)

    #
    # p.save_as(array=list_plan1,dest_file_name='C:\Users\Administrator\Documents\Mamibaobei\data\list_plan1')
    #
    # p.save_as(array=list_plan1, dest_file_name='C:\Users\Administrator\Documents\Mamibaobei\data\list_plan2')
    # p.save_book_as(bookdict=new_dict,dest_file_name=r'C:\Users\Administrator\Documents\Mamibaobei\data\plan.xlsx')




if __name__ == '__main__':
    proDir = r"C:\Users\Administrator\Documents\Mamibaobei"
    # print os.getcwd()
    # print os.path.join(os.getcwd())
    # print proDir
    xlsxPath = os.path.join(proDir, "data", "mami2021.xlsx")
    # get_mainfee(xlsxPath,'mainfee',start_row=2,plan=1,gender="M",age=0,g_p='20',p_p=10)
    # option1_fee = get_option_fee(xlsxPath, "optional1", start_row=1, gender="M", g_p='19', p_p=19, age=18)
    # option2_fee = get_option_fee(xlsxPath, u"少儿意外住院津贴责任费率", start_row=1, gender="M", g_p='20', p_p=1, age=0)
    # print(option1_fee)
    # print(option2_fee)
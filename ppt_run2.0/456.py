# # {'-HEIGHT': [], '-WEIGHT': [], '-EAT': ['|', '苹', '果'], '-BAD': [], '-EMO': []}
# #
# # # cc=''.join(a)
# # # print(cc)
# # # b='我了'
# # #
# # # if b in cc:
# # #     print(True)
# #
# # cc='我吃了苹果好烦'
# #
# # cc=[i for i in cc]
# # print(cc)
#
# import numpy as np
#
# # a=np.array([[0.08,0.91,0.01]])
# # blist=['体征','吃的或抽烟喝酒','心情']
# # for i in a:
# #  ind=list(i).index((max(list(i))))
# #  print(blist[ind])
# # zero={'-HEIGHT': [], '-WEIGHT': [], '-EAT': [], '-BAD': [], '-EMO': []}
# # a={'-HEIGHT': ['aa'], '-WEIGHT': [], '-EAT': ['|', '饭'], '-BAD': [], '-EMO': []}
# # b={'-HEIGHT': [], '-WEIGHT': ['a'], '-EAT': ['|', '肉'], '-BAD': [], '-EMO': []}
# # c={'-HEIGHT': [], '-WEIGHT': ['a'], '-EAT': ['|', '肉'], '-BAD': [], '-EMO': ['a']}
# #
# # # for i in a:
# # #  a[i]=a[i]+b[i]
# # #  print(a[i])
# # clist=[]
# # clist.append(a)
# # clist.append(b)
# # clist.append(c)
# #
# # print(clist)
# #
# # for dict in clist:
# #  for i in dict:
# #   zero[i]=zero[i]+dict[i]
# # print(zero)
#
# a=[1,2,3,4]
# for i in a :
#  a=a+[1]
#  print(i)
#
# dicti={'-HEIGHT':[2],'WEIGHT':[3],'-EAT':[1],'-BAD':[1],'-EMO':[]}
# add=[]
# # for i in dicti:
# #  if dicti[i]:
# #   add.append(True)
# #
# # print(len(add))
#
#  # if len(dict [i])==0:
#  #  print(True)
#
# if ([]in dicti.values()):
#  print(True)
#  print(dicti.keys())
#
# print([dicti[i]  for i in dicti])
# print(len([dicti[i] for i in dicti]))
#
# # if [dicti[i] for i in dicti]==[[], [], [], [], []]:
# #  print(True)
# from datetime import datetime
# dt=datetime.now() #创建一个datetime类对象
# print (  '时间：(%Y-%m-%d %H:%M:%S %p): ' , dt.strftime( '%y-%m-%d %I:%M:%S %p' ))
# print (dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,dt.month)
#
# WuHao = {
#     'Time': '20170101',
#     'Height': 'Jordan',
#     'W': 20,
#     'gender': 'male'
# }
#
# dict={'-HEIGHT': [], '-WEIGHT': [], '-EAT': [], '-BAD': ['|', '没', '有', '喝', '|', '有', '抽'], '-EMO': []}
# for i in dict:
#  dict[i]="".join(dict[i]).replace("|"," ")
#
#
#
#
# dict['TIME']= dt.strftime( '%y-%m-%d %I:%M:%S %p' )
# print(dict)
#
# import pymongo
#
# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client.test
# collection=db.students
# # result = collection.find({},{'Lisa':1})
# cc={"-HEIGHT" : " 180", "-WEIGHT" : " 99"}
# NAME = collection.find({"WUHAO":{'$exists':'true'}})
# # result['1']=2
# # print([i for i in NAME])
# # print(len([i for i in NAME]))
# # print([i for i in NAME])
# # print(len([i for i in NAME]))
# if len([i for i in NAME]) != 0:
#     print('存在')
#     NAME = collection.find({"WUHAO": {'$exists': 'true'}})
#     p1 = dict((key, value) for key, value in NAME[0].items() if key == "WUHAO")
#     new_list = NAME[0]["WUHAO"] + [cc]
#     print(new_list)
# for i in NAME:
#     print(i)
#     print(type(i))
#
# a=[]
# print(len(a))
# p1 = dict((key, value) for key, value in NAME[0].items() if key == "Lisa")
# new_list=NAME[0]['Lisa']+[cc]
# new_dict={'Lisa':new_list}
# print(p1)
# print(new_dict)
# result = collection.update(p1, {'$set': new_dict})
# set=(max([len(i) for i in result]))
# max_index=[len(i)!=1 for i in result].index(True)
# condition = {'name': 'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 26
# result = collection.update(condition, {'$set': student})

# condition = {'name': 'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 27
# result = collection.update_one(condition, {'$set': student})
# print(result)



# print(result)

# # print([cc].insert(len([cc]),cc))
# for i in result:
#  print('xiangxiangxiangxiangxiangxiangxiangxiangxiangxiang',i)
#  if len(i)!=1:
#   print(i)
#   p1 = dict((key, value) for key, value in i.items() if key == "Lisa")
#
#   new1=p1['Lisa']+[cc]
#   new_dic={'Lisa':new1}
#   print(new_dic)
#   print(p1)
#   up=collection.update(p1, {'$set':new_dic})
#   print(up)
def get_index(lst=None, item=''): ##获取全部索引
    return [i for i in range(len(lst)) if lst[i] == item]
def cut_max(num=10,alist=[2,8,19,30]): ##相减取绝对值最大索引
    cutlist=[abs(i-num) for i in alist]
    # print(cutlist.index(max(cutlist)))
    return  alist[cutlist.index(min(cutlist))]


text_eat='三箱西瓜苹果五十斤,一瓶来自天山呼伦贝尔妈妈带的矿泉水'
label_eat=['S-NUM', 'S-UNI', 'B-EAT', 'E-EAT','B-EAT', 'E-EAT', 'S-NUM','S-NUM', 'S-UNI',  'O', 'O', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-EAT', 'I-EAT', 'E-EAT']
text_bad='抽了三根烟,喝了五十瓶呼伦贝尔来的啤酒'
label_bad=['B-BAD', 'E-BAD', 'S-NUM', 'S-UNI', 'O', 'O', 'B-BAD', 'E-BAD', 'S-NUM', 'S-NUM', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'S-BAD', 'O']

dicti={'-EAT':[{'entity':'','uni':'','num':''},{'entity':'','uni':'','num':''}],'-BAD':[{'entity':'','uni':'','num':''},{'entity':'','uni':'','num':''}]}


def get_char_list(text_eat,label,inde,uni_or_num):  #输入i,输出标点内的所有uni索引
    def in_char(test=text_eat,indexd=inde):
        import re
        pattern = r',|，|。|\.|!|！|？'
        result_list=re.split(pattern,test)
        count=0
        for i in result_list:
            count=count+len(i)+1
            if indexd < count:
                break
        return i

    char_uni_list=[]
    char_num_list=[]
    for i,ele in enumerate(label):  #抓uni
        if ele[1:] =='-UNI':
            # print(i)
            # print(text_bad[i])
            if text_eat[i] in in_char(text_eat):
                char_uni_list.append(i)
        if ele[1:] =='-NUM':
            # print(i)
            # print(text_bad[i])
            if text_eat[i] in in_char(text_eat):
                char_num_list.append(i)
    if uni_or_num =='UNI':
        print(char_uni_list)
        return char_uni_list

    if uni_or_num == 'NUM':
        print(char_num_list)
        return char_num_list
# get_char_list(text_eat=text_eat,label=label_eat,inde=2,uni_or_num='UNI')




aa={'-HEIGHT': '  2.5  公斤', '-WEIGHT': '  90公斤'}

chnumber=['零''一','二','三','四','五','六','七','八','九','十','点']

def hw_to_nor(aa):

    import re

    if aa['-HEIGHT']!='':
        number = re.findall(r"\d+\.?\d*",aa['-HEIGHT'])
        number_start=aa['-HEIGHT'].find(''.join(str(s) for s in number))
        uni=aa['-HEIGHT'][number_start+len(''.join(str(s) for s in number)):]
        aa['-HEIGHT']=[{"NUM":''.join(str(s) for s in number),"UNI":uni}]

    if aa['-WEIGHT']!='':
        number = re.findall(r"\d+\.?\d*", aa['-WEIGHT'])
        number_start = aa['-WEIGHT'].find(''.join(str(s) for s in number))
        uni = aa['-WEIGHT'][number_start + len(''.join(str(s) for s in number)):]
        aa['-WEIGHT'] = [{"NUM": ''.join(str(s) for s in number), "UNI": uni}]


    print(aa)
    return aa
hw_to_nor(aa=aa)
    # print(uni)
# aaa={'-HEIGHT': [], '-WEIGHT': ['|', '四', '十', '公'], '-EAT': [{'B-EAT': '西瓜', 'NUM': '五', 'UNI': '斤'}, {'B-EAT': '苹果', 'NUM': '五', 'UNI': '个'}, {'B-EAT': '矿泉水', 'NUM': '一', 'UNI': '瓶'}], '-BAD': [{'B-BAD': '抽了', 'NUM': '三', 'UNI': '根'}, {'B-BAD': '喝了', 'NUM': '五十', 'UNI': '瓶'}], '-EMO': []}
# print(aaa)
# for i in dicti:
#     if i != '-EAT' and i != '-BAD':
#         dicti[i] = "".join(dicti[i]).replace("|", " ")
#
# print(dicti)

# print('33333333333',get_char_list(text_eat,label_eat,23,uni_or_num ='NUM'))
# all_uni_inchar=get_char_list(text_eat,label_eat,i,uni_or_num ='UNI')
# all_num_inchar=get_char_list(text_eat,label_eat,i,uni_or_num ='NUM:')

# for i ,ele in enumerate(label_bad):
#     if 'B-BAD'== ele:
#         all_uni_inchar = get_char_list(text_bad, label_bad, i, uni_or_num='UNI')
#         all_num_inchar = get_char_list(text_bad, label_bad, i, uni_or_num='NUM')
#         print('\n',text_bad[i])
#         if all_uni_inchar !=[]:
#             print('UNI:',cut_max(i,all_uni_inchar))  #算和uni距离最小的               ##记得抓双数
#             if label_bad[cut_max(i,all_uni_inchar) - 1][1:]==label_bad[cut_max(i,all_uni_inchar)][1:]:
#                 print(text_bad[cut_max(i,all_uni_inchar) - 1]+text_bad[cut_max(i,all_uni_inchar)])
#             elif label_bad[cut_max(i, all_uni_inchar) + 1][1:] == label_bad[cut_max(i, all_uni_inchar)][1:]:
#                 print(text_bad[cut_max(i,all_uni_inchar)]+text_bad[cut_max(i, all_uni_inchar) + 1])
#             else:
#                 print(text_bad[cut_max(i,all_uni_inchar)])
#         else:
#             print('[]')
#         if all_num_inchar != []:
#             print('NUM:',cut_max(i,all_num_inchar))  #算和uni距离最小的
#             if label_bad[cut_max(i,all_num_inchar) - 1][1:]==label_bad[cut_max(i,all_num_inchar)][1:]:
#                 print(text_bad[cut_max(i,all_num_inchar) - 1]+text_bad[cut_max(i,all_num_inchar)])
#             elif label_bad[cut_max(i, all_num_inchar) + 1][1:] == label_bad[cut_max(i, all_num_inchar)][1:]:
#                 print(text_bad[cut_max(i,all_num_inchar)]+text_bad[cut_max(i, all_num_inchar) + 1])
#             else:
#                 print(text_bad[cut_max(i,all_num_inchar)])
#
#
#
#         else:
#             print('[]')
#         # print('NUM:',cut_max(i,get_char_list(text_eat,label_eat,i,uni_or_num ='NUM:')), get_char_list(text_eat,label_eat,i,uni_or_num ='NUM:'))  #算和uni距离最小的

mytext='四箱西瓜五公斤苹果,一瓶来自天山呼伦贝尔妈妈带的矿泉水,抽了三根烟,喝了五十瓶呼伦贝尔来的啤酒'
label_list=['S-NUM', 'S-UNI', 'B-EAT', 'E-EAT', 'S-NUM', 'S-UNI', 'S-UNI', 'B-EAT', 'E-EAT', 'O', 'O', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-EAT', 'I-EAT', 'E-EAT','O','B-BAD', 'E-BAD', 'O', 'S-UNI', 'O', 'O', 'B-BAD', 'E-BAD', 'S-NUM', 'S-NUM', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'S-BAD', 'O']
name=mytext[label_list.index('I-EAT')]
# print(name)
for i,ele in enumerate(label_list):
    if ele=='I-EAT':
        if ele[1:]==label_list[i+1][1:]:
            name=name+mytext[i+1]
        if ele[1:]==label_list[i-1][1:]:
            name=mytext[i-1]+name

# print(name)

aaa={'B-BAD': '抽了', 'NUM': '[]', 'UNI': '根'}



# print(text_eat[2])
#
# text_eat=[i for i in text_eat]
# for i ,ele in enumerate(label_eat):
#     if ele[1:] in dicti:
#         if label_eat[i - 1] == 'O':
#             dicti[label_eat[i][1:]].append('|')
#             dicti[label_eat[i][1:]].append(text_eat[i])
#         else:
#             dicti[label_eat[i][1:]].append(text_eat[i])
#
# print(dicti)

# print(set)

# print(max_index)
# print(set[max_index])
#
# print( [i for i in result])

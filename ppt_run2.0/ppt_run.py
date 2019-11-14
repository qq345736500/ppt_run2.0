from datetime import datetime
dt=datetime.now() #创建一个datetime类对象
from main import evaluate_line
import  tensorflow as tf
import keras
from tensorflow.python.platform import flags
import pymongo

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


client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection=db.students
FLAGS = tf.app.flags.FLAGS
look_up=['身高','体重','吃的','抽烟喝酒','情绪',]
all_dict=[]
from mainto_diction import cut_max,get_char_list,dictionary

input_id=input('请输入ID\n')

# keras.backend.clear_session()
mytext,label_list=evaluate_line(save=FLAGS.ckpt_path)


dii=dictionary(label_list=label_list,mytext=mytext)

keras.backend.clear_session()

if [] in dii.values():    ##缺什么问什么
    for i, key in enumerate(dii):
        if dii[key] ==[]:
            re_ask=input('那今天的%s状况怎么样呢?\n'%(look_up[i]))
            keras.backend.clear_session()
            mytext2,label_list2=evaluate_line(if_ask=True, another_input=re_ask, save=FLAGS.ckpt_path)
            all_dict.append(dictionary(label_list=label_list2,mytext=mytext2))
    for diction in all_dict:
        for i in diction:

            dii[i]=dii[i]+diction[i]



# for i in dii:
#  dii[i]="".join(dii[i]).replace("|"," ")
for i in dii:
    if i != '-EAT' and i != '-BAD':
        dii[i] = "".join(dii[i]).replace("|", "  ")
print('dddddddddddddddddddddddddddddd',dii)
dii=hw_to_nor(aa=dii)

dii['-TIME']= dt.strftime( '%y-%m-%d %I:%M:%S %p' )
print(dii)
# NAME = collection.find({},{input_id:1})
NAME = collection.find({input_id:{'$exists':'true'}})
# print('看看',[i for i in NAME])
# print(len([i for i in NAME]))

if len([i for i in NAME]) == 0:     ##
    print('不存在')
    ins = collection.insert({input_id: [dii]})
else:
    print('存在')
    NAME = collection.find({input_id: {'$exists': 'true'}})
    p1 = dict((key, value) for key, value in NAME[0].items() if key == input_id)
    new_list = NAME[0][input_id] + [dii]
    new_dict = {input_id: new_list}
    print(p1)
    print(new_dict)
    up = collection.update(p1, {'$set': new_dict})


# for i in NAME:
#     print(True)
#     print('i',i)
#     if len(i) != 1:
#         p1 = dict((key, value) for key, value in i.items() if key == input_id)
#         print("p1",p1)
#         new1=p1[input_id]+[dii]
#         print(new1)
#         new_dic = {input_id: new1}
#         print('new_dic',new_dic)
#         up = collection.update(p1, {'$set': new_dic})
# for i in dii:        #一米八，90公斤，喝了酒，吃苹果，焦虑
#  if dii[i]:
#   add.append(True)
#
#
# while   len(add) !=5 :
#     for i, key in enumerate(dii):
#         # if [dicti[i] for i in dicti]==[[], [], [], [], []]:
#         #     re_ask = input('今天过的如何:\n')
#         if dii[key] ==[]:
#             re_ask=input('那今天的%s状况怎么样呢?\n'%(look_up[i]))
#
#             keras.backend.clear_session()
#             all_dict.append(evaluate_line(if_ask=True, another_input=re_ask, save=FLAGS.save_all))


# for diction in all_dict:            #错的
#     for i in diction:
#         dii[i]=dii[i]+diction[i]





# print(evaluate_line(save=FLAGS.save_all))

# mytext=list[mytext]
# for i,element in enumerate(label_list):
#     if element[1:] in dicti:
#         if label_list[i-1]=='O':
#             dicti[label_list[i][1:]].append('|')
#             dicti[label_list[i][1:]].append(mytext[i])
#         else:
#             dicti[label_list[i][1:]].append(mytext[i])
#         # print((label_list[i][1:]))
#         # print(mytext[i ])
# print(dicti)
# a=['我','吃','了','火','龙','果','，','西','瓜','哈','抽','了','，','好','烦']
# b=[ 'O',  'O',  'O', 'B-EAT','E-EAT','E-EAT','O', 'B-EAT','E-EAT','O','B-BAD','E-BAD','O','O','B-EMO']
# # print(dic['我'])
# cc=['-EAT','-BAD','-EMO']
# save={'-EAT':[],'-BAD':[],'-EMO':[] }
# for  i,element in enumerate(b):
#     if element[1:] in  save:
#         if b[i-1]=='O':
#             save[b[i][1:]].append('|')
#             save[b[i][1:]].append(a[i])
#         else:
#             save[b[i][1:]].append(a[i])
#         print((b[i][1:]))
#         print(a[i ])
#
# print(save)








# import json


# name = input("please enter your name:")
# password = input("please enter your password:")
# confirm_password = input("confirm your password:")
# while password != confirm_password:
#     print("input password inconsistencies,please try again")
#     password = input("please enter your password:")
#     confirm_password = input("confirm your password:")
#
# user_info = json.dumps({'username': name, 'password': password}, sort_keys=True, indent=4, ensure_ascii=False)
# print(user_info)
#
# with open('user_info.json', 'w', encoding='utf-8') as json_file:
#     json.dump(user_info, json_file, ensure_ascii=False)
#     print("write json file success!")
#




# with open('user_info.json', 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)
#     print(type(data))
#     print(data)
#     data=json.loads(data)
#     print(type(data))
#     print(data['username'])
#

# data = [1,2,3,4,5]
# with open('user_info.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, ensure_ascii=False)
#
# with open('user_info.json', 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)
#     print(type(data))
#     print(data)
# import  tensorflow as tf
# import os
#
#
#
#
# FLAGS = tf.app.flags.FLAGS
# assert FLAGS.clip < 5.1, "gradient clip should't be too much"
# assert 0 <= FLAGS.dropout < 1, "dropout rate between 0 and 1"
# assert FLAGS.lr > 0, "learning rate must larger than zero"
# assert FLAGS.optimizer in ["adam", "sgd", "adagrad"]










# for i in hello():
#     if i <=0.5:
#         class_result=input('您需要的服务是修理本公司的产品吗(回答 yes or no )？\n')
#         if class_result=='yes':
#             print('抱歉，修理产品系统维护中，敬请期待！')
#         else:
#             hello()
#     else:
#         body_query=input('您需要的服务是检查身体吗(回答 yes or no )？\n')
#
#         if body_query=='yes':
#             from main import evaluate_line
#             evaluate_line()
#         else:
#             hello()







# a = np.empty([0, 3])
# b = np.array([[1, 2, 3], [4, 5, 6]])
# c = [[7, 8, 9]]
# print(a)
# print(a.shape)
# print(b.shape)
#
# a = np.append(a, b, axis=0)
#
# a = np.append(a, c, axis=0)
#
#
# print(a)
# print(a.shape)
# print(b)
# print(b.shape)


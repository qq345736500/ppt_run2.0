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

from datetime import datetime
dt=datetime.now() #创建一个datetime类对象
from main import evaluate_line
import  tensorflow as tf
import keras
from tensorflow.python.platform import flags

from flask import Flask, request, render_template, Markup
app = Flask(__name__)
app.debug = True

import pymongo
from datetime import datetime
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection=db.students
dt=datetime.now() #创建一个datetime类对象
from my_ut import suo


client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection=db.students
FLAGS = tf.app.flags.FLAGS
look_up=['身高','体重','吃的','抽烟喝酒','情绪',]
all_dict=[]
used=[]
from mainto_diction import cut_max,get_char_list,dictionary

dii = {'-HEIGHT': [], '-WEIGHT': [], '-EAT': [], '-BAD': [], '-EMO': []}
@app.route('/first_ask', methods=['GET', 'POST'])
def first_ask():
    final_dii = {'-HEIGHT': [], '-WEIGHT': [], '-EAT': [], '-BAD': [], '-EMO': []}
    global idd
    global special
    global all_dict
    global dii
    if request.method=='GET':
        return render_template('first_ask.html')
    if request.method=='POST':

        id1 = request.form.get("idtext")
        if id1!='':
            idd=id1
        input_text=request.form.get("input_text")
        if input_text=='':
            return render_template('first_ask.html',res_text = '最近如何？')

        if input_text!='' and dii =={'-HEIGHT': [], '-WEIGHT': [], '-EAT': [], '-BAD': [], '-EMO': []}:  ##有输入的话
            mytext, label_list = evaluate_line(if_ask=True, another_input=input_text, save=FLAGS.ckpt_path)
            print(label_list,mytext)
            dii = dictionary(label_list=label_list, mytext=mytext)
            all_dict.append(dii)
            keras.backend.clear_session()
            if [] not in dii.values():                                     #一次输完的话
                final_dii=dii
                print('finalllllllllllll',final_dii)
                suo(dii=final_dii,input_id=idd)
                return render_template('first_ask.html', res_text='Thankyou')
            if [] in dii.values():
                for i, ele in enumerate(dii):
                    if dii[ele] == []:
                        used.append(ele)
                        return render_template('first_ask.html', res_text='那今天的%s状况怎么样呢?\n' % (look_up[i]))

        if input_text!='' and dii!={'-HEIGHT': [], '-WEIGHT': [], '-EAT': [], '-BAD': [], '-EMO': []}: #第二次询问
            print('2_ask')                   #我的身高90公分
            cou = 0
            for i in dii:
                if dii[i] != []:
                    cou = cou + 1

            for i,ele in enumerate(dii):
                print(i,ele,dii[ele],used)
                if dii[ele] ==[] and ele not in used:
                    used.append(ele)
                    mytext2, label_list2 = evaluate_line(if_ask=True, another_input=input_text,save=FLAGS.ckpt_path)
                    all_dict.append(dictionary(label_list=label_list2, mytext=mytext2))
                    # print(i,ele)
                    print('看看吧',all_dict)
                    return render_template('first_ask.html', res_text='那今天的%s状况怎么样呢?\n' % (look_up[i]))
                elif len(used)==5-cou:                    ##最后一条
                    mytext2, label_list2 = evaluate_line(if_ask=True, another_input=input_text, save=FLAGS.ckpt_path)
                    all_dict.append(dictionary(label_list=label_list2, mytext=mytext2))
                    print('看看final吧', all_dict)
                    for diction in all_dict:
                        for i in diction:
                            final_dii[i] = final_dii[i] + diction[i]

                    print('finalllllllllllll',final_dii)

                    suo(dii=final_dii, input_id=idd)


                    return render_template('first_ask.html', res_text='Thankyou')
                else:
                    continue
if __name__ == '__main__':
    app.run(host="0,0,0,0",port=1919)
                    # try:               #吃了西瓜，心情焦虑，抽了三根烟，喝了五瓶酒
                    #     continue
                    # except TypeError:
                    #     return render_template('first_ask.html', res_text='thank you')
                    # else:
                    #     # print(all_dict)
                    #     # mytext2, label_list2 = evaluate_line(if_ask=True, another_input=input_text,
                    #     #                                      save=FLAGS.ckpt_path)
                    #     # all_dict.append(dictionary(label_list=label_list2, mytext=mytext2))
                    #     # keras.backend.clear_session()
                    #     # return render_template('first_ask.html', res_text='thank you')

print(all_dict)
            # mytext, label_list = evaluate_line(if_ask=True, another_input=input_text, save=FLAGS.ckpt_path)
            # dii2 = dictionary(label_list=label_list, mytext=mytext)
            # keras.backend.clear_session()
            #
            #
            #     # for diction in all_dict:
            #     #     for i in diction:
            #     #         save_dii[i] = save_dii[i] + diction[i]
            #
            # return render_template('first_ask.html',res_text = '那今天的')




                # for i, key in enumerate(save_dii):
                #     if save_dii[key] == []:
                #         # re_ask = input('那今天的%s状况怎么样呢?\n' % (look_up[i]))
                #         re_ask=input_text
                #         keras.backend.clear_session()
                #         mytext2, label_list2 = evaluate_line(if_ask=True, another_input=re_ask, save=FLAGS.ckpt_path)
                #         all_dict.append(dictionary(label_list=label_list2, mytext=mytext2))
                #
                #         return render_template('first_ask.html', res_text='那今天的%s状况怎么样呢?\n' % (look_up[i]))


            # if [] not in dii.values():
            #     return render_template('first_ask.html',res_text = 'Thank you')
# input_id=id1





# keras.backend.clear_session()
# mytext,label_list=evaluate_line(save=FLAGS.ckpt_path)
#
# dii=dictionary(label_list=label_list,mytext=mytext)
#
# keras.backend.clear_session()
#
# if [] in dii.values():    ##缺什么问什么
#     for i, key in enumerate(dii):
#         if dii[key] ==[]:
#             re_ask=input('那今天的%s状况怎么样呢?\n'%(look_up[i]))
#             keras.backend.clear_session()
#             mytext2,label_list2=evaluate_line(if_ask=True, another_input=re_ask, save=FLAGS.ckpt_path)
#             all_dict.append(dictionary(label_list=label_list2,mytext=mytext2))
#     for diction in all_dict:
#         for i in diction:
#
#             dii[i]=dii[i]+diction[i]








# for i in dii:
#     if i != '-EAT' and i != '-BAD':
#         dii[i] = "".join(dii[i]).replace("|", "  ")
# print('dddddddddddddddddddddddddddddd',dii)
# dii=hw_to_nor(aa=dii)
#
# dii['-TIME']= dt.strftime( '%y-%m-%d %I:%M:%S %p' )
# print(dii)
#
# NAME = collection.find({input_id:{'$exists':'true'}})
#
#
# if len([i for i in NAME]) == 0:     ##
#     print('不存在')
#     ins = collection.insert({input_id: [dii]})
# else:
#     print('存在')
#     NAME = collection.find({input_id: {'$exists': 'true'}})
#     p1 = dict((key, value) for key, value in NAME[0].items() if key == input_id)
#     new_list = NAME[0][input_id] + [dii]
#     new_dict = {input_id: new_list}
#     print(p1)
#     print(new_dict)
#     up = collection.update(p1, {'$set': new_dict})




# dii={'-HEIGHT': [2], '-WEIGHT': [3], '-EAT': ['|', '苹', '果'], '-BAD': [1], '-EMO': []}
# look_up=['身高','体重','吃的','抽烟喝酒','情绪',]
# for i, key in enumerate(dii):
#     print(dii[key])
#     if dii[key] ==[]:
#         re_ask=input('请问您今天的%s状况怎么样呢'%(look_up[i]))
#
#     else:
#         print(False)

# a=[]
# b={"-HEIGHT" : " 180", "-WEIGHT" : " 90"}
# c={"HEIGHT" : " 180", "WEIGHT" : " 90"}

# def get_index(lst=None, item=''): ##获取全部索引
#     return [i for i in range(len(lst)) if lst[i] == item]


# def in_char(test_text='我是猪，我很胖，我好吃',indexd=6):
#     import re
#     pattern = r',|，|。|\.|!|！|？'
#     result_list=re.split(pattern,test_text)
#
#     count=0
#     for i in result_list:
#         count=count+len(i)+1
#         if indexd < count:
#             break
#     return i



# from main import evaluate_line
# import tensorflow as tf
# FLAGS = tf.app.flags.FLAGS
# dii=evaluate_line(save=FLAGS.ckpt_path)
# mytext,label_list=dii





# keras.backend.clear_session()

mytext='四十公斤西瓜和苹果五个,一瓶来自天山呼伦贝尔妈妈带的矿泉水,抽了三根烟,喝了五十瓶呼伦贝尔来的酒'
label_list=['S-NUM','S-NUM', 'S-UNI', 'S-UNI', 'B-EAT', 'E-EAT', 'O', 'B-EAT', 'E-EAT', 'S-NUM', 'S-UNI', 'O', 'S-NUM', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-EAT', 'I-EAT', 'E-EAT', 'O', 'B-BAD', 'E-BAD', 'S-NUM', 'S-UNI', 'O', 'O', 'B-BAD', 'E-BAD', 'S-NUM', 'E-NUM', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
# print(len(mytext),len(label_list))

# mytext='抽了三根烟,喝了五十瓶呼伦贝尔来的啤酒'
# label_list=['B-BAD', 'E-BAD', 'S-NUM', 'S-UNI', 'O', 'O', 'B-BAD', 'E-BAD', 'S-NUM', 'S-NUM', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'S-BAD', 'O']

# diction={'-EAT':[{'entity':'','uni':'','num':''},{'entity':'','uni':'','num':''}],'-BAD':[{'entity':'','uni':'','num':''},{'entity':'','uni':'','num':''}]}
# dicti = {'-HEIGHT': [], '-WEIGHT': [], '-EAT': [], '-BAD': [], '-EMO': []}

def cut_max(num=10,alist=[2,8,19,30]): ##相减取绝对值最大索引
    cutlist=[abs(i-num) for i in alist]
    # print(alist[cutlist.index(min(cutlist))])
    return  alist[cutlist.index(min(cutlist))]

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
        return char_uni_list
    if uni_or_num == 'NUM':
        return char_num_list

def dictionary(label_list,mytext):
    dicti = {'-HEIGHT': [], '-WEIGHT': [], '-EAT': [], '-BAD': [], '-EMO': []}

    for i ,ele in enumerate(label_list):
        if 'B-BAD'== ele or 'B-EAT'== ele:
            name=mytext[i]                               ###到break都是加多字的名字
            for shu,x in enumerate(label_list[i:]):
                if label_list[i:][shu][1:]==label_list[i:][shu+1][1:]:
                    name=name+mytext[i+shu+1]
                else:
                    break
            evert_dic={ele:name,'NUM':'','UNI':''}

            all_uni_inchar = get_char_list(mytext, label_list, i, uni_or_num='UNI')
            all_num_inchar = get_char_list(mytext, label_list, i, uni_or_num='NUM')
            # print('\n'+mytext[i])

            print('\n')
            print(i)
            if all_uni_inchar !=[]:
                print('UNI:',cut_max(i,all_uni_inchar),all_uni_inchar,mytext[cut_max(i,all_uni_inchar)])  #算和uni距离最小的               ##记得抓双数

                name_uni=mytext[cut_max(i,all_uni_inchar)]                ###到break都是加多字的名字
                for x in range(1,3):
                    # print(label_list[cut_max(i,all_uni_inchar)+x][1:])
                    if label_list[cut_max(i,all_uni_inchar)][1:]==label_list[cut_max(i,all_uni_inchar)+x][1:]:
                        name_uni=name_uni+mytext[cut_max(i,all_uni_inchar)+x]

                    if label_list[cut_max(i,all_uni_inchar)][1:]==label_list[cut_max(i,all_uni_inchar)-x][1:]:
                        name_uni = mytext[cut_max(i,all_uni_inchar)-x]+name_uni

                # for shu, x in enumerate(label_list[cut_max(i,all_uni_inchar):]):
                #     print('222222222222222',label_list[cut_max(i,all_uni_inchar)][shu - 1][1:])
                #     if label_list[1:][shu][1:]==label_list[1:][shu+1][1:]:
                #         name_uni = name_uni + mytext[cut_max(i,all_uni_inchar)+ shu + 1]
                #     else:
                #         break
                evert_dic['UNI']=name_uni
            else:
                print('UNI:[]')
                evert_dic['UNI'] = '[]'
            if all_num_inchar != []:
                print('NUM:',cut_max(i,all_num_inchar),mytext[cut_max(i,all_num_inchar)])  #算和uni距离最小的
                name_num=mytext[cut_max(i,all_num_inchar)]
                for x in range(1,3):
                    # print(label_list[cut_max(i,all_uni_inchar)+x][1:])
                    if label_list[cut_max(i,all_num_inchar)][1:]==label_list[cut_max(i,all_num_inchar)+x][1:]:
                        name_num=name_num+mytext[cut_max(i,all_num_inchar)+x]
                    if label_list[cut_max(i,all_num_inchar)][1:]==label_list[cut_max(i,all_num_inchar)-x][1:]:
                        name_num = mytext[cut_max(i,all_num_inchar)-x]+name_num

                # for shu, x in enumerate(label_list[cut_max(i, all_num_inchar):]):
                #     if label_list[1:][shu][1:] == label_list[1:][shu + 1][1:]:
                #         name_num=name_num + mytext[cut_max(i,all_num_inchar)+ shu + 1]
                #     else:
                #         break
                evert_dic['NUM'] = name_num
            else:
                print('NUM: []')
                evert_dic['NUM'] = '[]'
            print(evert_dic)

            if 'B-BAD' in evert_dic:
                dicti['-BAD'].append(evert_dic)
            if 'B-EAT' in evert_dic:
                dicti['-EAT'].append(evert_dic)
        elif ele[1:]!='-EAT' and ele[1:]!='-BAD' and ele[1:] in dicti:
            if label_list[i - 1] == 'O':
                dicti[label_list[i][1:]].append('|')
                dicti[label_list[i][1:]].append(mytext[i])
            else:
                dicti[label_list[i][1:]].append(mytext[i])
    print('222222222222',dicti)

    return dicti



dictionary(mytext=mytext,label_list=label_list)


##能否和在一起写？


    # if 'B-EAT' == ele:
    #     all_uni_inchar = get_char_list(text_bad, label_bad, i, uni_or_num='UNI')
    #     all_num_inchar = get_char_list(text_bad, label_bad, i, uni_or_num='NUM')













# text_bad='抽了三根烟,喝了五瓶呼伦贝尔来的啤酒'
# label_bad=['B-BAD', 'E-BAD', 'S-NUM', 'S-UNI', 'O', 'O', 'B-BAD', 'E-BAD', 'S-NUM', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'S-BAD', 'O']
#
# # label_eat=['S-NUM', 'S-UNI', 'B-EAT', 'E-EAT', 'S-NUM', 'S-UNI', 'B-EAT', 'E-EAT', 'O', 'S-NUM', 'S-UNI', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-EAT', 'I-EAT', 'E-EAT']
# # text_eat='三箱西瓜五斤苹果,一瓶来自天山呼伦贝尔妈妈带的矿泉水'
#
# in_char(text_bad,)
# char_uni_list=[]
# for i,ele in enumerate(label_bad):  #抓uni
#     if ele[1:] =='-NUM':
#         print('entity',i)
#         # print(text_bad[i])
#         if text_bad[i] in in_char(test_text=text_bad,indexd=0):
#             print('entity2',i)
#             char_uni_list.append(i)
# print(char_uni_list)

        # print([x for x in text_bad[i] if x in in_char()])
        # print(i)
# print(test_text[indexd:])


# for i in char:
#     if i in test_text[indexd:]:
#         break
# try:
#     print(test_text[indexd:].index(i))
# except ValueError:
#     print(len(test_text)-1)
#
# print(test_text[:indexd])
#
# for j in char:
#     if j in test_text[indexd:]:




# for i ,ele in enumerate(test_text[:indexd]): #考虑是不是最后一句
#     get_index
#
#
# def count_char(test_text='我是猪，我很胖，我好吃'): #统计句子出现符号次数
#     a=0
#     for i in test_text:
#         if i == '，':
#             a=a+1
#     print(a)
#     return a



# for i ,ele in enumerate(test_text):
#     print(i,ele)
#     if indexd==i:
#         break




# print(get_index(label_eat,'S-UNI'))



# for i ,ele in enumerate(label_eat):
#     if 'B-EAT'== ele:




# a = text_eat[i]
##找出索引为3的逗号内的所有有 NUM和UNI

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
    # if b[i-1][1:]== b[i][1:] and b[i]!='O':
    #     print(b[i-1][1:])
    #     print(a[i-1],a[i])

#output三个list[火龙果，西瓜]【抽了】【烦】 #不断收集资料到填满为止。


# for i,element in enumerate(save):
#     print(element,save[element])
#     save2=''
#     for i in save[element]:
#         save2=save2+i
#         if save2 in ''.join(a):
#             save[element]
f=open('classdata/my.train.txt','r+')
from main import evaluate_line
text_list=[]
label_list=[]
count=0
for i in f:

    b = ''
    for char in i:
        b = b + char + ' '
    add_empty=b.rstrip(' ')


    count=count+1
    if count<=40:
        ii=123
    elif count<=80:
        text_list.append(add_empty.strip())
        label_list.append(0)
    elif count<=120:
        text_list.append(add_empty.strip())
        label_list.append(1)

print(text_list)

print(label_list)
print(len(label_list))
print(len(text_list))   #不用结巴

from keras.preprocessing.text import text_to_word_sequence,one_hot,Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import time
vocab_size = 300
maxlen = 20
print("Start fitting the corpus......")
t = Tokenizer(vocab_size) # 要使得文本向量化时省略掉低频词，就要设置这个参数
X_orig=np.array(text_list)
Y_orig=np.array(label_list)
print('X_orig',X_orig)
print(X_orig.shape)
print(type(X_orig))

t.fit_on_texts(X_orig) # 在所有的评论数据集上训练，得到统计信息!!!中文不能这样写！那要怎么写?自己加空格阿


word_index = t.word_index # 不受vocab_size的影响
print('word_index:',word_index)
print('all_vocab_size',len(word_index))

print("Start vectorizing the sentences.......")
v_X = t.texts_to_sequences(X_orig) # 受vocab_size的影响 每句话 index组成


print("Start padding......")
pad_X = pad_sequences(v_X,maxlen=maxlen,padding='post')
print("Finished!")


small_word_index=word_index


import gensim

model_file='word2vec_wiki100.txt'
print("Loading word2vec model......")
wv_model = gensim.models.KeyedVectors.load_word2vec_format(model_file,binary=False)

embedding_matrix = np.random.uniform(size=(vocab_size+1,100)) # +1是要留一个给index=0
print("Transfering to the embedding matrix......")
# sorted_small_index = sorted(list(small_word_index.items()),key=lambda x:x[1])
for word,index in small_word_index.items():
    try:
        word_vector = wv_model[word]
        embedding_matrix[index] = word_vector
    except:
        print("Word: [",word,"] not in wvmodel! Use random embedding instead.")
print("Finished!")
print("Embedding matrix shape:\n",embedding_matrix.shape)

print(type(pad_X))
print(type(Y_orig))
print(pad_X.shape)
print(Y_orig.shape)
print(Y_orig)
X_train=np.empty(shape=[0, maxlen])
Y_train=np.empty(shape=[0])
X_dev=np.empty(shape=[0, maxlen])
Y_dev=np.empty(shape=[0])

count=0
for i in pad_X:
    count=count+1
    print(i,i.shape,type(i))

    if count % 40 <= 30 and  count % 40 != 0:
        X_train=np.append(X_train, [i], axis=0)
    else:
        X_dev=np.append(X_dev, [i], axis=0)
count=0
for i in Y_orig:
    count=count+1
    if count % 40 <= 30 and  count % 40 != 0:
        Y_train=np.append(Y_train, [i], axis=0)
    else:
        Y_dev=np.append(Y_dev, [i], axis=0)
print('X_train',X_train.shape)
print('Y_train',Y_train.shape)


#下次要弄成后三十条，不能random
from sklearn.model_selection import train_test_split
# np.random.seed = 1
# random_indexs = np.random.permutation(len(pad_X))
# X_train = pad_X[random_indexs]
# Y_train = Y_orig[random_indexs]
# print(Y[:10])
# X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)
# print("X_train:",X_train.shape)
# print("y_train:",y_train.shape)
# print("X_test:",X_test.shape)
# print("y_test:",y_test.shape)
# print(list(y_train).count(1))
# print(list(y_train).count(0))


import keras
from keras.models import Sequential,Model
from keras.layers import Input,Dense,GRU,LSTM,Activation,Dropout,Embedding
from keras.layers import Multiply,Concatenate,Dot



inputs = Input(shape=(maxlen,))
use_pretrained_wv = True

def train_class():
    if use_pretrained_wv:
        wv = Embedding(vocab_size+1,100,input_length=maxlen,weights=[embedding_matrix])      (inputs)
    else:
        wv = Embedding(vocab_size+1,100,input_length=maxlen)(inputs)
    h = LSTM(64)(wv)
    y = Dense(1,activation='sigmoid')(h)

    m = Model(input=inputs,output=y)
    m.summary()
    m.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    m.fit(X_train, Y_train, batch_size=2, epochs=15, validation_data=(X_dev, Y_dev))  ####要用validation_data
        # print('x_train',X_train)
        # print(X_train.shape)

        # np.set_printoptions(threshold=30000)
        # print(X_train)
        # print(Y_train)

    return m

    # X_test=np.array([[ 1  ,6 ,15 ,18 ,14  ,7  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0 ,0]])

def hello():


    query=input('您好，有什么可以帮助您：\n')
    now_text=np.array(list(query))

    print(now_text)
    print(type(now_text))
    v_now=t.texts_to_sequences(now_text)
    print(v_now)
    count2=[]
    for i in v_now:
        count2 = count2 + i
    print(count2)

    pad_now=   pad_sequences([count2],maxlen=maxlen,padding='post')
    print(pad_now)
    modeling=train_class()
    result_list=list(modeling.predict(pad_now))
    # print(m.predict(X_dev))m.predict(pad_now)
    #
    # classis=np.argmax(m.predict(X_dev), axis=1)


    for i in result_list:
        if i <=0.5:
            class_result=input('您需要的服务是修理本公司的产品吗(回答 yes or no )？\n')
            if class_result=='yes':
                print('抱歉，修理产品系统维护中，敬请期待！')

            else:
                hello()
        else:
            body_query=input('您需要的服务是检查身体吗(回答 yes or no )？\n')

            if body_query=='yes':
                keras.backend.clear_session()
                height,weight=evaluate_line(if_ask=False)
                print(height,weight)
                while height==''or weight=='':
                    body_query2=input('对不起我还不够智能，请重新告知完整的身高和体重\n')
                    keras.backend.clear_session()
                    height, weight = evaluate_line(if_ask=True, another_input=body_query2)
                reask =input('确认您的身高是'+height+'您的体重是'+weight+'(回答 yes or no)?\n')
                if reask=='yes':
                    import pymongo
                    client = pymongo.MongoClient(host='localhost', port=27017)
                    db = client.test
                    collection = db.students
                    student = {
                        'id': '20191023',
                        'Height': height,
                        'weight': weight,
                    }
                    result = collection.insert(student)
                    print('已录入数据库，稍后为您服务')
                else:

                    hello()
            else:
                hello()




hello()
# print(type(classis))

# Y_test=np.array(0)
#
# m.evaluate(X_test, Y_test,batch_size=10, verbose=0)

# print("test set")
# scores = m.evaluate(X_test,Y_test,batch_size=1,verbose=0)
# print("")
# print("The test loss is %f" % scores)
# result = m.predict(X_test,batch_size=1,verbose=0)
# print(result)



# X_test = np.array([ 1  ,6 ,15 ,18 ,14  ,7  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0 ,0])
# print(X_test.shape)
# result = m.predict(X_test.reshape(20,),batch_size=1,verbose=0)
# print(result)

# for i in range(10):
#
#     inputtt = eval(input('please input some things \n'))
#
#     c = np.array(inputtt)
#     result = m.predict(c, batch_size=1, verbose=0)
#     print(result)

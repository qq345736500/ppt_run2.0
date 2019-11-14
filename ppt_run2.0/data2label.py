import string
punc =string.punctuation
f= open('mydata/example.test','r+')
new=open('mydata/example.testt','w+')
alist=['一','二','三','四','五','六','七','八','九','零']
cara=[',','，','。','.']
for i in f:
    save = []
    count = 0
    for l in i:
        save.append(l.strip())
        count+=1
        if l in alist or l.isdigit()==True:

            if save[count-1]  in alist or save[count-1].isdigit() == True    :
                if  save[count-2] in alist or save[count-2].isdigit() == True    :
                    new.write(l.strip('\n')+' '+'I-PER')
                    new.write('\n')

                else:
                    new.write(l.strip('\n') + ' ' + 'B-PER')
                    new.write('\n')
        elif l.isalnum()==True:
            new.write(l.strip('\n')+' '+'O')
            new.write('\n')
        elif l in cara:
            new.write(l.strip('\n') + ' ' + 'O')
            new.write('\n')

        else:
            new.write(l.strip('\n'))
            new.write('\n')

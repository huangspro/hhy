import re
a='''
'''
b=''''''
b=re.sub('[\u4e00-\u9fa5]','', b)
b=re.sub('[0-9]','',b)
for i in "i:u:ɜ:ɪɑ:ɔ:æəʊɒʌʃtʃθðŋʒ，：。；？！～、”““（《＊＃’‘·《【［｛「」『』=｝］】》》）”":
    if i in b:
       b=b.replace(i,'')
c=re.split(a,b)
for i in c:
    u='#'+i+'#'
    if u!="##":
       print(u)
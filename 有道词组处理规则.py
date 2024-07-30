import re
a='''
'''
b=''''''
for i in b:
    if i not in ''' abcdefghijklmnopqrstuvwxyzQAWSEDRFTGYHUJIKOLPMNBVCXZ'''+a:
       b=b.replace(i,'')
c=re.split(a,b)
for i in c:
    m=[]
    for p in i:
        if p in '''abcdefghijklmnopqrstuvwxyzQAWSEDRFTGYHUJIKOLPMNBVCXZ''':
           m.append('h')
    if 'h' in m:
        u='#'+i+'#'
        print(u)
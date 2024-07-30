def r(a,b,c):#从第b个字母遍历至第c个字母
    m=[]
    for i in range(int(b)-1,int(c)):
        m.append(a[i])
    return(''.join(m))
def h(a,b):#将字符串中的字符按b个b个的遍历
    m=[]
    for i in range(1,len(a)-b+2):
        m.append(r(a,i,i+b-1))
    return(m)
def j(a):#将字符串中的字符按多个长度进行遍历
    m=[]
    for i in range(3,len(a)):
        m=h(a,i)+m
    return(m)
def k(a,b):#返回两个单词的相似度
    m=0
    for i in j(a):
        if i in b:
           m=m+1
    return(m)
def t(a,b):#返回列表b中每个单词与a单词的相似度，并且按照从小到大的顺序排列
    m={}
    for i in b:
        m.update({i:k(a,i)})
        n=sorted(m.items(), key=lambda m:m[1])
    return(n)
        

#登录---------------------------------------------------------
cc='''
<!DOCTYPE html>
<html>
<head>
<meta content="width=device-width, initial-scale=1">
</head>
<body>
<p>登录界面</p>
<form>
<input id="k" name="zh" type="text">帐号</input><br>
<input name="password" type="text">密码</input><br>
<input style="background-color:skyblue;color:red;"type="submit"></input><br>
</form>
<a style="color:red;background-color:skyBlue;" href="/send">发消息</a>
<script>
document.getElementById('k').addEventListener('blur', function(){
var a=this.value;if(a==="k1"){alert("k1不可作为用户名");}if(a==="k2"){alert("k2不可作为用户名");}});
</script>
</body>
</html>
'''
txt1='''
<!DOCTYPE html>
<html>
<head>
<meta content="width=device-width, initial-scale=1">
</head>
<body>
'''
txt2='''
</body>
</html>
'''
def put1(a):#匹配成功后返回message
    message=open(a+'.txt','r',encoding="utf-8").read()
    return(txt1+'<p>'+message+'</p>'+txt2)
def put2():#匹配失败
    return(txt1+'<p>password is wrong</p>'+txt2)
def put3():#匹配到不存在账号时
    return(txt1+'账号不存在，已自动创建账号'+txt2)
def write1(a):#写入帐号,k1
    c=open('k1.txt','a',encoding='utf-8')
    c.write(a+'\n')
    c.close()
def write2(a):#写入password,k2
    c=open('k2.txt','a',encoding='utf-8')
    c.write(a+'\n')
    c.close()
def find(a,b):#匹配,三种情况
    c=open('k1.txt','r',encoding="utf-8").readlines()
    d=open('k2.txt','r',encoding="utf-8").readlines()
    if a+'\n' in c:
       if c.index(a+'\n')==d.index(b+'\n'):
          return(put1(a))#匹配成功界面
       if c.index(a+'\n')!=d.index(b+'\n'):
          return(put2())#匹配失败页面
    else:#账户不存在页面
       write1(a)
       write2(b)
       f=open(a+'.txt','w',encoding="utf-8")
       f.close()
       return(put3())
    c.close()
    d.close()
#------------------------------------------------------------



#发送---------------------------------------------------------
sendmessage='''
<!DOCTYPE html>
<html>
<head>
<meta content="width=device-width, initial-scale=1">
</head>
<body>
<p>发信件</p>
<form>
<div style="width:500px;height:130px;background-color:lightgreen;">
<input style="width:400px;" type="text" name="zh">本人帐号</input><br>
<input style="width:400px;" type="text" name="password">密码</input><br>
<input style="width:400px;height:50px;" type="text" name="txt">信息内容</input><br>
<input style="width:400px;" type="text" name="tomessage">收件人帐号</input><br>
</div>
<p></p>
<input style="background-color:skyblue;color:red;" type="submit"></input><br>
</form>
</body>
</html>
'''
def send(txt,frommessage,password,tomessage):
    a=open('k1.txt','r',encoding="utf-8").readlines()
    b=open('k2.txt','r',encoding="utf-8").readlines()
    if (frommessage+'\n') in a and (password+'\n') in b:
       if a.index(frommessage+'\n')==b.index(password+'\n'):
          q=open(tomessage+'.txt','a',encoding='utf-8')
          q.write(txt)
          q.close()

#--------------------------------------------------------------


from flask import Flask,request
app = Flask(__name__)
@app.route('/')
def h():
       a=request.args.get("zh")
       b=request.args.get('password')
       if a!=None and b!=None:
          return find(a,b)
       return cc
    
@app.route('/send')
def p():
    a=request.args.get("zh")
    b=request.args.get('password')
    c=request.args.get('txt')
    d=request.args.get('tomessage')
    if b!=None and a!=None:
       send(c,a,b,d)
       return '发送成功'
    return sendmessage
app.run(debug=True,host="0.0.0.0",port=4000)

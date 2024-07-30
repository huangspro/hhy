from flask import Flask,request
import difflib
m=["hello","hekllo",'conduct','context','conducting']
def k(a):
    p=[]
    o='''
'''
    def g(a,b):
        return(difflib.SequenceMatcher(None,a,b).quick_ratio())
    for i in m:
        if g(a,i)>=0.7:
           p.append(i)
    return(o.join(p))
    
def j(a):
    return('''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<h1>与这个单词相似的单词有</h1>
<p>'''+a+'''</p>
</body>
</html>
''')


ooo='''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>单词相似</title>
</head>
<body>
<form enctype="multipart/form-data">
<input type="text" name="f">请输入单词</input>
<input type="submit" >提交</input>
</form>
</body>
</html>
'''

app = Flask(__name__)

@app.route('/')
def uploader():
    r=request.args.get('f')
    if r!=None:
       return j(k(r))
    return ooo
app.run(debug=True,host="0.0.0.0",port=4000)